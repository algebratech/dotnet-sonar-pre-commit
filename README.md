# dotnet scanner for pre-commit! :fire:

Run **dotnet-sonarscanner** on [pre-commit](https://pre-commit.com) hooks.

### Example .pre-commit-config.yaml

```yaml
repos:
-   repo: https://github.com/algebratech/dotnet-sonar-pre-commit
    rev: v1.0.0
    hooks:
    -   id: dotnet-sonarscanner
        args: [
            '--sonar-project-key=projectKey',
            '--sonar-project-name=projectName',
            '--sonar-organization=organization'
        ]
```
