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

### Available Templates

```shell
Stack: github-stack-poc
+----------------+--------------------------------------------+------------------+-----------------+
| name           | description                                | types            | version(latest) |
+----------------+--------------------------------------------+------------------+-----------------+
| new-repository | Template to create a new github repository | ['app-template'] | no release      |
+----------------+--------------------------------------------+------------------+-----------------+
```

### Available Plugins

```shell
Stack: github-stack-poc
+---------------------+--------------------------------------------------------+---------+-----------------+
| name                | description                                            | types   | version(latest) |
+---------------------+--------------------------------------------------------+---------+-----------------+
| gha-auto-assign     | Plugin to add a auto-assign github actions workflow    | ['app'] | no release      |
|                     |                                                        |         |                 |
| gha-first-interacti | Plugin to add a first-interaction github actions       | ['app'] | no release      |
| on                  | workflow                                               |         |                 |
|                     |                                                        |         |                 |
| gha-gitleaks        | Plugin to add a gitleaks github actions workflow       | ['app'] | no release      |
|                     |                                                        |         |                 |
| gha-horusec         | Plugin to add a horusec github actions workflow        | ['app'] | no release      |
|                     |                                                        |         |                 |
| gha-super-linter    | Plugin to add a super-linter github actions workflow   | ['app'] | no release      |
|                     |                                                        |         |                 |
| issue-templates     | Plugin to add issue templates to the github repository | ['app'] | no release      |
|                     |                                                        |         |                 |
| pull-request-templa | Plugin to add a pull-request template to the           | ['app'] | no release      |
| te                  | github repository                                      |         |                 |
+---------------------+--------------------------------------------------------+---------+-----------------+
```

### Available Stackfiles

```shell
Stack: github-stack-poc
+---------+-----------------------------------------------+------+
| name    | description                                   | type |
+---------+-----------------------------------------------+------+
| default | Template to create a new repository with some | app  |
|         | Github default and Actions files              |      |
+---------+-----------------------------------------------+------+
```