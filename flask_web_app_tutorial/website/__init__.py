'''How to use Flask'''
from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'secret'

	return app
