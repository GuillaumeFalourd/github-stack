# About

This plugin will add the following workflow to the repository where it is applied:

```yaml
name: GitlLeaks

on: [push, pull_request, workflow_dispatch]

concurrency:
  group: {{ '${{ github.workflow }}' }}-{{ '${{ github.ref }}' }}
  cancel-in-progress: true

jobs:
  GitLeaks:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
        with:
          fetch-depth: '0'
      - name: gitleaks-action
        uses: zricethezav/gitleaks-action@master
```

[Action reference](https://github.com/zricethezav/gitleaks-action)