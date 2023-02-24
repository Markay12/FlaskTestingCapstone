# helloName.py
from flask import Flask           # import flask

app = Flask(__name__)             # create an app instance

@app.route("/<name>")                   # at the end point /

def hello_name(name):                      # call method hello
	return "Hello " + name


if __name__ == "__main__":        # on running python app.py
   app.run(debug=True)             # run the flask application in debug mode
