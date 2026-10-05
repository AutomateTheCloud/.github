# Contributing

Contributions are welcome. Every change is reviewed closely before it is merged, because people
build real infrastructure on this code, so please expect questions and requests for changes.

This is the organization-wide guide. If a repository has its own `CONTRIBUTING.md`, follow that
one instead: it lists the exact tools and checks for that repository.

## Before you start

Open an issue first and describe what you want to change and why. Agreeing on the approach before
you write code saves you time. Small fixes, such as typos in the documentation, can go straight to
a pull request.

To report a security problem, do not open an issue. Follow the repository's security policy
instead.

## Making a change

1. Fork the repository and create a branch.
2. Make the change. Keep to one change per pull request.
3. Run the repository's formatting and tests. For Terraform, at least `terraform fmt -recursive`
   and `terraform validate`, plus `terraform test` where the repository has tests.
4. Commit with `git commit -s` (see [Sign your commits](#sign-your-commits)), and open a pull
   request that explains what changed and why.

A pull request is merged only when its checks pass and a maintainer has approved it.

## Sign your commits

Every commit in a pull request must be signed off. Signing off means you agree to the
[Developer Certificate of Origin](https://developercertificate.org/) (DCO): a short statement
that you wrote the change, or otherwise have the right to submit it under the repository's
license. Code written for an employer may belong to the employer, so check before contributing it.

Sign off by committing with `-s`, which adds a line with the name and email from your Git
settings:

```shell
git commit -s -m "Describe the change"
```

The email in the sign-off must match the commit's author email. To sign off commits you have
already made, run `git rebase --signoff main` and force-push the branch.

## Guidelines

- Secure defaults stay secure. A change must not make infrastructure created with only the
  required inputs more open than it was.
- A change that would replace existing resources, or make callers change their code, needs a
  strong reason and a new major version.
- Write in plain, American English, in the same style as the existing documentation.

## Conduct

Everyone taking part is expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

Each repository's `LICENSE` file states its terms. Any contribution you submit for inclusion is
licensed under the same terms as the repository it is submitted to. Your sign-off confirms you
have the right to submit it.
