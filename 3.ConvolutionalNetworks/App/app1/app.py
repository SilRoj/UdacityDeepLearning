

import os
from flask import Flask, render_template, request



app = Flask(__name__, static_url_path='/static', template_folder='templates')

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	file = request.files['image']
	f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
	# add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
	file.filename = "input_file.jpg"
	file.save(f)

	return render_template('index.html')


# run the app.
if __name__ == "__main__":
    	# Setting debug to True enables debug output. This line 
    	# should be removed before deploying a production app.
    	app.debug = True
    	app.run("0.0.0.0", port=8888)
