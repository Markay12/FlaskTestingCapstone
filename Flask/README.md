<img align="right" src="https://miro.medium.com/max/1400/1*e2v4HCTyZo8bQqDU7iZqMw.webp" alt="drawing" style="margin-right: 20px" width="250"/>


# Capstone Flask Implementation

![Flask Shield](https://img.shields.io/badge/Flask-1.1.x-blue)

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


## Hello \<Name\>

The next project we are going to do is print hello with your name by changing the URL input.

This is just going to change our firstApp.py code. To begin we want to create a copy of the firstApp.py code. I have named my code helloName.py.

1. Duplicate the firstApp.py code

```Shell
cp firstApp.py helloName.py
```

2. Edit the helloName.py code

We want to change the middle definition section for hello to incorporate your name/input.

The new code will look like:

```Python
@app.route("/<name>")
def hello_name(name):
	return "Hello " + name
```

3. Set Debug to True

The last thing to do is to set debugging to True. This is so our name editing works and shows up in our Flask application. 

To set debugging we now look at the initializer function to run the Python application.

```Python
if __name__ = "__main__":
	app.run(debug = True) 	# The debug = True is our new working addition to this code
```

4. Run the Application and test in your Browser

To run the application do 

```Shell
python3 helloName.py
```

Then follow the link that is provided in your browser and append your name to the end. My name is Mark and the link should look like this.

```Shell
http://127.0.0.1:5000/Mark
```

The output on screen will be Hello Mark!

You have now finished this tutorial and can use debugging tools with Flask!

