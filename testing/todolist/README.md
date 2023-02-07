# To Do List Application

Now that we have a solid understanding on how to use Flask we can begin creating an application for users. 

This to do list will work just like others and allow people to:

1. Add Items.
2. Delete Items.
3. Mark an Item as Completed.
4. Update Items.

First we will need to focus on data. There will need to be two functions that perform operations on data. The first is to create items in the to do list. When creating items for the to do list we will have:

1. Title
2. Description
3. When it was Created
4. When it is Due

To delete items we must check that the item was deleted. There are two ways to delete items from a list. We can do what is called a soft delete or a hard delete. A soft delete will just flag the item as being deleted but leave it in the list so the user can still  see what they have accomplished.

Items can then be marked as completed and/or updated with new information that follows along with the information that was used to create the item.

### Designing the Database

SQLite relational DB is what is used to store this data in the form of tables. A table needs to be created to store the list created by users. This first table will look like 

```
ToDo_Items 
- Id                 Primary Key
— Title              Text
- Description        Text  
- CreatedOn          Date
- DueDate            Date
- _is_deleted        Boolean
- _is_done           Boolean
```

This would be good if the system was being used for one person. However, this is going to be used by many people and will need to include many users. That means we will need another table to store the users which each have their own ToDo\_Items table.

```
User
- Name            Text
- Email           Email
- Id              Primary KeyToDo_Items
   ...
   ...
   CreatedBy      ForeginKey(User)
```

### Code Structure

The code for this application will be broken into three different sections. There will be:

1. app.py - which is the entry and exit point to the application
2. service.py - which converts the request into a response
3. models.py - which handles all the database functions

## The Code


The main thing we are new to using with this code is SQLite. Using sqlite allows us to track the information that is being used and create our todo database.

```Python
# 1.import sqlite
import sqlite

# 2. create a connection to DB     
conn = sqlite3.connect('todo.db')

# 3. Write your sql query   
query = "<SQLite Query goes here>"

# 4. execute the query
result = conn.execute(query)
```

This code snippet for sqlite is going to be used frequently in the `models.py` file. 


## Tables

Tables are created for the main way we interact with the database. The models.py file is what communicates most with the database. 

The first thing we create is a schema which is where the DB tables are created and maintained. 

This schema is represented as an object where we create the to do table as well as the user because each user is going to have their own to do table.

In this to do model, we will also need to create methods to create, select, delete and update the todo list. Below is the code to create the todo list and it will be up to you to try and code your own code for the update, delete and select methods.

```Python

class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'
        
        result = self.conn.execute(query)        

```

### Service.py

The service.py file contains methods from service because it enables you to test the functions of our to do list.

### View Functions
The functions to view will be the entry point and exit point of the system. 

There are four main decisions that can be made.

1. Type of input that is expected.
2. Type of output to give the user.
3. Authentication of Requests.
4. Logging the requests.

This is all done in the `app.py` file

```Python

@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())
```

Now that all of this is done, you should have your code written and ready to go. We can move onto the final part of running your project.

# Running the ToDoList Flask Application

1. Run app.py in the console. It should be running using the port that was defined. In my case, I have set the port to 8888. 

`127.0.0.1:8888`

2. To create your first request we need to make sure that requests are downloaded on to your machine. To do this we are going to use pip install.

`pip3 install requests`

You can also use postman to do your request testing. The first will use your command line while postman is used or downloaded online.

3. When using requests instead of Postman. You will have to open the python API and create your first request. From here you will then be able to see your output online by adding the `/todo` extension to your link.

```Shell
$ python

>>> import requests
>>> requests.post("http://localhost:8888/todo",
			json={"Title":"This is Mark's ToDoList",
				"Description":"Look at all these things!"})
```

Getting a repsonse of [200] means that your request was successfully completed! Congratulations! Head over to your `/todo/` page of your localhost at the correct port to see the requests. 	
