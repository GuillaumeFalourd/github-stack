[![Super Linter](https://github.com/GuillaumeFalourd/github-stack-poc/actions/workflows/super-linter.yml/badge.svg)](https://github.com/GuillaumeFalourd/github-stack-poc/actions/workflows/super-linter.yml) [![Horusec](https://github.com/GuillaumeFalourd/github-stack-poc/actions/workflows/horusec.yml/badge.svg)](https://github.com/GuillaumeFalourd/github-stack-poc/actions/workflows/horusec.yml) [![Gitleaks](https://github.com/GuillaumeFalourd/github-stack-poc/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/GuillaumeFalourd/github-stack-poc/actions/workflows/gitleaks.yml)

# Github Stack POC

Repository used as a [StackSpot](https://www.stackspot.com/) proof of concept using Github.

# Usage

This stack is a proof of concept showing how the STK CLI can be used to create a new repository template with some default and actions workflow files already configured.

This implies files such as:
- `README.md`
- `.gitignore`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `DEVELOPER_GUIDE.md`
- `LICENSE` (only Apache 2.0 supported at the moment)
- `SECURITY.md`
- `.github/ISSUE_TEMPLATE/*` (bug + enhancement md files)
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/*` (security, first interaction, auto-assign, linters...)