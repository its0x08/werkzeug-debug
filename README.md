# Werkzeug Debug-enabled RCE v0.0.1-beta
This is a __python__ script for exploiting __werkzeug debug__ to achieve __RCE__.
It can __read__ a particular file or __execute__ some command.

## Usage
```
git clone https://github.com/its0x08/werkzeug-debug.git
cd werkzeug-debug
python3 main.py example.com whoami
```

## Testing locally
To test it locally you can start the mock Flask server by executing the command below.
```bash
WERKZEUG_DEBUG_PIN=off python3.10 mock_flask.py
```
## TODO

* Add PIN bruteforce
* Add arg parser

## Contributors

If you decide to make a pull request to suggest your changes to the project, please dont forget to add your name to the CONTRIBUTING.md file.

## Pull Requests & Issues
You have a new feature in mind?
The code is buggy, wont run as expected and you happen to know __python__?
Please make a __Pull Request (_PR_)__ suggesting you changes.
Otherwise you can always open an __Issue__ to help imporve this project.

## Enjoy it !
