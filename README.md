[![Super Linter](https://github.com/GuillaumeFalourd/github-stack/actions/workflows/super-linter.yml/badge.svg)](https://github.com/GuillaumeFalourd/github-stack/actions/workflows/super-linter.yml) [![Horusec](https://github.com/GuillaumeFalourd/github-stack/actions/workflows/horusec.yml/badge.svg)](https://github.com/GuillaumeFalourd/github-stack/actions/workflows/horusec.yml) [![Gitleaks](https://github.com/GuillaumeFalourd/github-stack/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/GuillaumeFalourd/github-stack/actions/workflows/gitleaks.yml)

# GitHub Stack

Repository used as a [StackSpot](https://www.stackspot.com/) proof of concept using GitHub.

# Usage

```shell
stk import stack https://github.com/GuillaumeFalourd/github-stack
```

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

### Available Templates

```shell
Stack: github-stack
+----------------+--------------------------------------------+------------------+-----------------+
| name           | description                                | types            | version(latest) |
+----------------+--------------------------------------------+------------------+-----------------+
| new-repository | Template to create a new GitHub repository | ['app-template'] | no release      |
+----------------+--------------------------------------------+------------------+-----------------+
```

### Available Plugins

```shell
Stack: github-stack
+---------------------+--------------------------------------------------------+---------+-----------------+
| name                | description                                            | types   | version(latest) |
+---------------------+--------------------------------------------------------+---------+-----------------+
| gha-auto-assign     | Plugin to add a auto-assign GitHub actions workflow    | ['app'] | no release      |
|                     |                                                        |         |                 |
| gha-first-interacti | Plugin to add a first-interaction GitHub actions       | ['app'] | no release      |
| on                  | workflow                                               |         |                 |
|                     |                                                        |         |                 |
| gha-gitleaks        | Plugin to add a gitleaks GitHub actions workflow       | ['app'] | no release      |
|                     |                                                        |         |                 |
| gha-horusec         | Plugin to add a horusec GitHub actions workflow        | ['app'] | no release      |
|                     |                                                        |         |                 |
| gha-super-linter    | Plugin to add a super-linter GitHub actions workflow   | ['app'] | no release      |
|                     |                                                        |         |                 |
| issue-templates     | Plugin to add issue templates to the GitHub repository | ['app'] | no release      |
|                     |                                                        |         |                 |
| pull-request-templa | Plugin to add a pull-request template to the           | ['app'] | no release      |
| te                  | GitHub repository                                      |         |                 |
+---------------------+--------------------------------------------------------+---------+-----------------+
```

### Available Stackfiles

```shell
Stack: github-stack
+---------+-----------------------------------------------+------+
| name    | description                                   | type |
+---------+-----------------------------------------------+------+
| default | Template to create a new repository with some | app  |
|         | GitHub default and Actions files              |      |
+---------+-----------------------------------------------+------+
```
