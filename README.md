# Werkzeug Debug-enabled RCE v0.1.2-beta
This is a __python__ script for exploiting __werkzeug debug__ to achieve __RCE__.
It can __execute__ command on the remote system.

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fits0x08%2Fwerkzeug-debug&countColor=%232ccce4&style=flat-square)
[![Pylint](https://github.com/its0x08/werkzeug-debug/actions/workflows/pylint.yml/badge.svg)](https://github.com/its0x08/werkzeug-debug/actions/workflows/pylint.yml)
[![Semgrep](https://github.com/its0x08/werkzeug-debug/actions/workflows/semgrep.yml/badge.svg)](https://github.com/its0x08/werkzeug-debug/actions/workflows/semgrep.yml)
[![CodeQL](https://github.com/its0x08/werkzeug-debug/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/its0x08/werkzeug-debug/actions/workflows/codeql-analysis.yml)

## Usage
```bash
git clone https://github.com/its0x08/werkzeug-debug.git
cd werkzeug-debug
pip3 install --user -r requirements.txt
python3 main.py example.com whoami
```

## Testing locally
To test it locally you can start the mock Flask server by executing the command below.
```bash
WERKZEUG_DEBUG_PIN=off python3.10 mock_flask.py
```
## TODO

- [ ] Add PIN bruteforce
- [x]  Add arg parser
- [ ]  Add read file functionality
- [ ]  Add reverse shell functionality

## Contributors

If you decide to make a pull request to suggest your changes to the project, please don't forget to add your name to the `CONTRIBUTING.md` file.

## Pull Requests & Issues
You have a new feature in mind?
The code is buggy, wont run as expected and you happen to know __python__?
Please make a __Pull Request (_PR_)__ suggesting you changes.
Otherwise you can always open an __Issue__ to help improve this project.

## Enjoy it !
