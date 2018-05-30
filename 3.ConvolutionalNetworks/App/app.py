from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello from Flask!'

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line 
    # should be removed before deploying a production app.
    app.debug = True
    app.run("0.0.0.0", port=80)
