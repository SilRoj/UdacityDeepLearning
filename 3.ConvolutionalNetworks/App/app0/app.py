
from flask import Flask
from asset import *
app = Flask(__name__)

@app.route('/')
def hello_world():
	return '  Hello from Machine LEarning lab!'

@app.route('/dog-project/')
def projects():
	predictor  = dog_breed_predictor()
	return predictor


# run the app.
#if __name__ == "__main__":
    	# Setting debug to True enables debug output. This line 
    	# should be removed before deploying a production app.
#    	app.debug = True
#    	app.run("0.0.0.0", port=80)
