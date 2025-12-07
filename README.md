### turnKnob

<img width="1920" height="1440" alt="turn-knob-workspace" src="https://github.com/user-attachments/assets/9913e0f1-f5e8-4b3b-a209-5dd21447048b" />

TURN KNOB is a free, city-wide directory that helps artists effortlessly find and filter recording studios by gear, space, and vibe - all while giving studios a simple way to get discovered and fully booked.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app turn_knob
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/turn_knob
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

agpl-3.0
