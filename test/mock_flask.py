from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	raise

app.run("127.0.0.1", debug=True, port=80)
