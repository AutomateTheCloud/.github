# AutomateTheCloud/.github: working rules

This repository is special to GitHub. Everything in it is public, and parts of it act on every
repository in the organization:

- `profile/README.md` is the public organization page at https://github.com/AutomateTheCloud.
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, and
  `.github/ISSUE_TEMPLATE/` are defaults for every repository in the organization that has no file
  of its own. A change here changes all of them at once.
- `scripts/scan-org.py` compares the organization's repositories with the profile README.

The members-only page is a separate private repository, `AutomateTheCloud/.github-private`, at
`profile/README.md`. Its "What's here" table lists the same repositories and goes stale the same
way, so update both together.

## Ground rules

- Do not commit, push, or change repository or organization settings unless asked. Pushing here
  publishes immediately.
- Sign off every commit with `git commit -s`. Commit messages describe the change only: never
  mention an AI tool or add attribution trailers for one.
- Say what you verified and how. "Links work" means you checked them.

## Updating the profile README

The module index in `profile/README.md` is written by hand, but what belongs in it comes from the
organization. Do not update it from memory or from an old list.

1. **Scan.** Run `python3 scripts/scan-org.py`. It needs the GitHub CLI, signed in, and changes
   nothing. For each public repository it checks four things, and a module counts as **current**
   only when all four hold:
   - `LICENSE` is the Apache 2.0 text byte for byte (by SHA-256),
   - `CHANGELOG.md` exists,
   - the default branch is protected,
   - the module is listed on the Terraform Registry under `AutomateTheCloud`.

   It then lists what the README gets wrong and exits 1, or exits 0 when the README matches.
2. **Apply each finding.**
   - **Missing current module:** add a row to the category it fits (see below).
   - **Missing older module:** add a row under "Earlier modules".
   - **Current module listed under "Earlier modules":** move it up into its category. When that
     leaves "Earlier modules" empty, delete the whole `<details>` block and its intro line.
   - **Older module listed in a category, archived, or deleted:** move it down, or remove the row.
3. **Write each description** from the module's own README and GitHub description, not from the
   module's name. Each one is a single "What it creates" phrase: start with the resource, name
   the AWS service as AWS does, keep a notable secure default if the module has one, and don't
   use marketing words. Compare it with the rows around it.
4. **Check.** Run the scan again until it exits 0. Then confirm every link resolves (`gh api
   repos/AutomateTheCloud/<name>`), and that GitHub renders the file:
   `gh api markdown -f mode=gfm -F text=@profile/README.md`.
5. **Update the members-only README** in `.github-private` to match. Its own `CLAUDE.md` has the
   steps; `python3 scripts/scan-org.py --table-only` prints the facts it needs.

### Categories

Keep the existing order. Put a module in the one category that matches what it mainly creates.

| Category | What goes there |
|---|---|
| Networking | VPCs and what connects them: subnets, gateways, peering, security groups, IP addresses |
| DNS and certificates | Route 53 zones, resolver endpoints and rules, ACM certificates |
| Data and storage | Databases, caches, object storage, file systems, data warehouses |
| Security and keys | KMS keys, key pairs, IAM building blocks, secrets |
| Delivery and operations | Container registries, deployment, queues, Systems Manager, compute services such as ECS |

If a module fits none of them, or a public repository isn't a Terraform module at all, ask before
creating a new section.

### What stays fixed

- The intro, "What we do", and the licensing section change only when the organization does.
  "Our code is released under the Apache License 2.0, and each repository's `LICENSE` file states
  its terms" stays true while older modules are relicensed, so it needs no edit when they are.
- The logo comes from the brand kit's `atc-lockup-horizontal.svg` and
  `atc-lockup-horizontal-dark.svg`. Replace the files in `profile/assets/` with newer kit
  versions; never redraw or edit them.
- No numbers in prose ("our 30 modules"). They go stale silently.

## The community defaults

- `CODE_OF_CONDUCT.md` is the Contributor Covenant 3.0, verbatim except for its two placeholders:
  how to report (email info@automatethe.cloud) and the enforcement note, which was removed to
  accept the recommended process. Don't edit the rest of the text. To change versions, download
  the new text from contributor-covenant.org and fill in the placeholders again.
- `CONTRIBUTING.md` and `SECURITY.md` are the organization-wide versions of the module repos' own
  files. When the reference module (`terraform-aws-s3_bucket`) changes its files, bring the
  general rules across here.
- Issue forms set no labels. GitHub requires a label set by a template to exist in every
  repository that uses the template.
- **Never add `FUNDING.yml`.** It would put a Sponsor button on every repository. Asking for
  donations is regulated charitable solicitation, and that decision belongs to the board.

## Writing

Plain and specific. Say what a thing does before why. Short sentences, no marketing words, and
expand an acronym the first time it appears. "Automate the Cloud" in prose, "Automate the Cloud
Inc." in legal text. American English everywhere.
