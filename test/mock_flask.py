'''This file is used to create a Flask debug instance for testing'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	'''Empty method for root route'''
	return None

app.run("127.0.0.1", debug=True, port=80)
