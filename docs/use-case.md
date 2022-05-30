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