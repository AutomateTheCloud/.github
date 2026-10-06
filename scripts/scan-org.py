#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Compare the organization's public repositories with profile/README.md.

    python3 scripts/scan-org.py               # check profile/README.md
    python3 scripts/scan-org.py --table-only  # facts for the members-only README

Needs the GitHub CLI (`gh`), signed in. Reads only; changes nothing.

With --table-only it skips the README comparison and instead summarizes the
current modules, the older ones, and the private repositories, which is what
the members-only README in AutomateTheCloud/.github-private states. It always
exits 0 in that mode.

For every public repository it records whether the repository is a current
module (Apache 2.0 LICENSE byte for byte, a CHANGELOG.md, protected main, and
listed on the Terraform Registry) or an older one, then reports where the
README disagrees: repositories missing from it, entries for repositories that
no longer exist or are archived, and current modules filed under "Earlier
modules" or the reverse. It prints each missing repository's GitHub description
as a starting point; the README's descriptions are rewritten, so it does not
compare them. Exits 1 when the README needs an update, 0 when it matches.
"""
import base64
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.request

ORG = "AutomateTheCloud"
README = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "profile", "README.md")
# SHA-256 of https://www.apache.org/licenses/LICENSE-2.0.txt, from the licensing playbook.
APACHE_SHA256 = "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30"
EARLIER = "Earlier modules"
# Repositories that are not modules and never appear in the module index.
NOT_LISTED = {".github"}


def gh(*args, allow_fail=False):
    r = subprocess.run(["gh", "api", *args], capture_output=True, text=True)
    if r.returncode != 0:
        if allow_fail:
            return None
        sys.exit(f"gh api {' '.join(args)} failed:\n{r.stderr}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def license_is_apache(repo):
    f = gh(f"repos/{ORG}/{repo}/contents/LICENSE", allow_fail=True)
    if not f or f.get("type") != "file":
        return False
    return hashlib.sha256(base64.b64decode(f["content"])).hexdigest() == APACHE_SHA256


def registry_names():
    url = f"https://registry.terraform.io/v1/modules/{ORG}?limit=100"
    with urllib.request.urlopen(url, timeout=30) as r:
        mods = json.load(r).get("modules", [])
    # Registry module "vpc" with provider "aws" lives in repository terraform-aws-vpc.
    return {f"terraform-{m['provider']}-{m['name']}" for m in mods}


def readme_entries():
    """Repository name -> (section heading, description) as the README lists them."""
    entries, section = {}, None
    for line in open(README, encoding="utf-8"):
        h = re.match(r"^\*\*(.+?)\*\*\s*$", line) or re.search(r"<summary><b>(.+?)</b></summary>", line)
        if h:
            section = h.group(1)
            continue
        m = re.match(r"^\| \[([^\]]+)\]\(https://github\.com/" + ORG + r"/([^)]+)\) \| (.+?) \|\s*$", line)
        if m:
            entries[m.group(2)] = (section, m.group(3))
    return entries


def main():
    repos = []
    page = 1
    while True:
        batch = gh(f"orgs/{ORG}/repos?type=public&per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1

    table_only = "--table-only" in sys.argv[1:]
    on_registry = registry_names()
    listed = {} if table_only else readme_entries()
    problems, current_mods, older_mods = [], [], []

    print(f"{'repository':42} {'status':8} {'apache':6} {'chlog':5} {'prot':4} {'reg':3}  in README")
    for r in sorted(repos, key=lambda r: r["name"]):
        name = r["name"]
        if name in NOT_LISTED:
            continue
        if r["archived"]:
            print(f"{name:42} archived")
            if name in listed:
                problems.append(f"{name} is archived but still listed under '{listed[name][0]}'")
            continue
        apache = license_is_apache(name)
        changelog = gh(f"repos/{ORG}/{name}/contents/CHANGELOG.md", allow_fail=True) is not None
        protected = gh(f"repos/{ORG}/{name}/branches/{r['default_branch']}/protection",
                       allow_fail=True) is not None
        registry = name in on_registry
        current = apache and changelog and protected and registry
        status = "current" if current else "older"
        section = listed.get(name, ("-", ""))[0]
        yn = lambda b: "yes" if b else "no"
        print(f"{name:42} {status:8} {yn(apache):6} {yn(changelog):5} {yn(protected):4} {yn(registry):3}  {section}")
        (current_mods if current else older_mods).append(name)

        if table_only:
            continue
        if name not in listed:
            problems.append(f"{name} ({status}) is not in the README. GitHub description: "
                            f"{r['description'] or '(none)'}")
            continue
        if current and section == EARLIER:
            problems.append(f"{name} is now a current module but is listed under '{EARLIER}'")
        if not current and section != EARLIER:
            problems.append(f"{name} is not a current module "
                            f"(apache={yn(apache)}, changelog={yn(changelog)}, "
                            f"protected={yn(protected)}, registry={yn(registry)}) "
                            f"but is listed under '{section}'")

    names = {r["name"] for r in repos}
    for name, (section, _) in sorted(listed.items()):
        if name not in names:
            problems.append(f"{name} is listed under '{section}' but is not a public repository")

    print(f"\nRegistry lists {len(on_registry)} modules for {ORG}.")

    if table_only:
        private = gh(f"orgs/{ORG}/repos?type=private&per_page=100")
        print(f"\nCurrent modules: {len(current_mods)}")
        print(f"Older modules: {len(older_mods)}" + (f" ({', '.join(older_mods)})" if older_mods else ""))
        print("Private repositories:")
        for r in sorted(private, key=lambda r: r["name"]):
            if r["name"] == ".github-private":
                continue
            print(f"  {r['name']}: {r['description'] or '(no description)'}, "
                  f"last pushed {r['pushed_at'][:10]}{', archived' if r['archived'] else ''}")
        return

    if problems:
        print(f"\n{len(problems)} thing(s) to update in profile/README.md:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print("\nprofile/README.md matches the organization.")


if __name__ == "__main__":
    main()
