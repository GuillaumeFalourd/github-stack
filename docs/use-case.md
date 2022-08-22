# Use case

1. You can create your template after importing this stack by using:

```shell
stk create app <APP-NAME> github-stack/new-repository
```

2. Then, after entering the APP after using `cd <APP-NAME>` you'll be able to add plugin using for example:

```shell
stk apply plugin github-stack/pull-request-template
```

3. Repeat this process for any plugin you would like to add the template.

# Stackfile

Note that you can create the template and apply all available plugins at once using the following command:

```shell
stk create app <APP-NAME> --stackfile github-stack/default
```

* * *

# Available Templates

```shell
Stack: github-stack
+----------------+--------------------------------------------+------------------+-----------------+
| name           | description                                | types            | version(latest) |
+----------------+--------------------------------------------+------------------+-----------------+
| new-repository | Template to create a new GitHub repository | ['app-template'] | no release      |
+----------------+--------------------------------------------+------------------+-----------------+
```

## Available Plugins

```shell
Stack: github-stack
+---------------------+--------------------------------------------------------+---------+-----------------+
| name                | description                                            | types   | version(latest) |
+---------------------+--------------------------------------------------------+---------+-----------------+
| gha-auto-assign     | Plugin to add a auto-assign GitHub actions workflow    | ['app'] | no release      |
|                     |                                                        |         |                 |
| gha-devsecops       | Plugin to add a devsecops GitHub actions workflow      | ['app'] | no release      |
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

# Available Stackfiles

```shell
Stack: github-stack
+---------+-----------------------------------------------+------+
| name    | description                                   | type |
+---------+-----------------------------------------------+------+
| default | Template to create a new repository with some | app  |
|         | GitHub default and Actions files              |      |
+---------+-----------------------------------------------+------+
```
