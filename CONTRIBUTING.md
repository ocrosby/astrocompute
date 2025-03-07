# Contributing to AstroCompute

First off, thanks for taking the time to contribute! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue [here](https://github.com/ocrosby/astrocompute/issues) and include:
- A clear and descriptive title.
- A detailed description of the issue.
- Steps to reproduce the issue.
- Any relevant logs or screenshots.

### Suggesting Enhancements

If you have an idea for an enhancement, please open an issue [here](https://github.com/ocrosby/astrocompute/issues) and include:
- A clear and descriptive title.
- A detailed description of the enhancement.
- Any relevant examples or mockups.

### Submitting Pull Requests

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

### Coding Standards

- Follow the existing code style.
- Write clear and concise commit messages.
- Ensure your code passes all tests.
- Add tests for your changes.

### Running Tests

To run tests, use the following command:

```shell
invoke test
```

### Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## Conventional Commits

### Quick examples

* `feat: new feature`
* `fix(scope): bug in scope`
* `feat!: breaking change` / `feat(scope)!: rework API`
* `chore(deps): update dependencies`

### Commit types

* `build`: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
* `ci`: Changes to CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
* **`chore`: Changes which doesn't change source code or tests e.g. changes to the build process, auxiliary tools, libraries**
* `docs`: Documentation only changes
* **`feat`: A new feature**
* **`fix`: A bug fix**
* `perf`: A code change that improves performance
* `refactor`:  A code change that neither fixes a bug nor adds a feature
* `revert`: Revert something
* `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* `test`: Adding missing tests or correcting existing tests

### Reminders

* Put newline before extended commit body
* More details at **[conventionalcommits.org](https://www.conventionalcommits.org/)**


## Additional Resources

- [Semantic Versioning 2.0](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Commitlint](https://commitlint.js.org/)
- [Husky](https://typicode.github.io/husky/#/)
- [Automate your GitHub Actions Releases (with Semantic Release)!](https://www.youtube.com/watch?v=mah8PV6ugNY&t=904s)

This file provides guidelines for reporting bugs, suggesting enhancements, submitting pull requests, coding standards, running tests, and includes a link to the project's code of conduct.