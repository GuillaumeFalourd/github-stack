# About

This plugin will add the following workflow to the repository where it is applied:

```yaml
name: Auto Author Assign

on:
  pull_request_target:
    types: [opened, reopened]

concurrency:
  group: {{ '${{ github.workflow }}' }}-{{ '${{ github.ref }}' }}
  cancel-in-progress: true

permissions:
  pull-requests: write

jobs:
  assign-author:
    runs-on: ubuntu-latest
    steps:
      - uses: toshimaru/auto-author-assign@v1.3.7
```

[Action reference](https://github.com/toshimaru/auto-author-assign)