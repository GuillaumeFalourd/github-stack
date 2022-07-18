# About

This plugin will add the following workflow to the repository where it is applied:

```yaml
name: First Interaction

on:
  pull_request:
  issues:
    types: opened

jobs:
  first-interaction:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/first-interaction@v1
        with:
          repo-token: {{ '${{ secrets.GITHUB_TOKEN }}' }}
          issue-message: "{{issue_message}}"
          pr-message: "{{pr_message}}"
```

[Action reference](https://github.com/actions/first-interaction)