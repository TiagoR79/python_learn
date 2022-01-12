'''website/ is now a python package because of __init__.py'''
from website import create_app

app = create_app()

'''
	Only if we run this file will we start the webserver!!!! Not only if we import it
	debug=True -> app relaunch on every change in development -> set to false in production
'''
if __name__ == '__main__':
	app.run(debug=True)
