# Contributing

First of all, thank you for considering contributing to this project!

There are several ways to contribute:

* Spread the word about the project
* Suggest features
* Tell us how you use the project / contribute to examples project
* Contribute support for new clients
* Contribute test cases
* Submit bugs and issues

## Workflow

### Git workflow

The project follows a simple git trunk based workflow:

* 'master' branch which is the current latest stable version
* we develop in feature branches which then get tested and merged into master

### Branch naming

Branch naming is as follows:

```sh
git branch feature/issue-42/add-new-client-support
git branch feature/no-ref/refactor-consensus-tasks
```

'issue' refers to a Github issue.

### Commit messages

They should begin with on of the three below prefixes, be short and descriptive. We like keeping it simple.

```sh
git commit -m 'feat: add support for Teku consensus and validator'
git commit -m 'fix: update type in geth docker compose template'
git commit -m 'refactor: refactor execution deployment tasks'
```

### Versioning

We use Semantic Versioning 2.0.0 -> [https://semver.org/](https://semver.org/).

### Will you accept my pull request if it doesn't follow the above?

Yes. Ultimately we want this be a community driven project, if you have written code you want to contribute we'll happily review it and merge it.

### Testing

We take testing seriously. Ideally your pull request would be tested against project's test suite. See [Testing](https://slingnode.gitbook.io/slingnode.ethereum/testing) for details. However, we will test all pull requests before merging them.
