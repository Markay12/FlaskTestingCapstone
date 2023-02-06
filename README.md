<img align="right" src="https://miro.medium.com/max/1400/1*e2v4HCTyZo8bQqDU7iZqMw.webp" alt="drawing" style="margin-right: 20px" width="250"/>


# Capstone Flask Implementation

## Initial Flask Setup and Trial

To get started with Flask you need to make sure that you have Python installed. Python is a good language for the web application domain.
Python is now used a lot in backend development and has even gotten new installations to work with JavaScript in web development. (Take a look into PyScript).

[PyScript](https://pyscript.net/)

## Requirements 

1. Python 3.7 or greater.
2. A workable IDE that allows for efficient editing of code.
3. Create a project directory.
4. Virtual environment (venv).
5. Install flask with pip.

## First Project

To begin with the first project we make our own directory called testing and add a file.
Our file name is going to be firstApp.py. Below will be the code and setup to get your first app running.

1. Create your new directory and create the new file named firstApp.py.

```Shell
mkdir testing
touch firstApp.py
```

2. Open your code file and edit the contents.

You can use your own code editor for editing the contents of firstApp.py. I will be using vim as that is my current preferred editor.

```Shell
#make sure you are in the correct directory
vim firstApp.py
```

Once in the file we will code our first application.

```Python
# firstApp.py
# 06 Febraury 2023

from flask import Flask		# importing Flask

app = Flask(__name__)		# create an instance of the application

@app.route("/")			# insert a '/' at the end point

def hello():			# call method hello
	return "Welcome to our First Flask Application!"	# this will print out the words Welcome to our First Flask Application

if __name__ == "__main__":	# on running python app.py, run the flask application
	app.run()

```

This is then the outline of our first Flask application.

3. Then we can start our application.

To run the application you can use the command.

```Shell
python firstApp.py
```
