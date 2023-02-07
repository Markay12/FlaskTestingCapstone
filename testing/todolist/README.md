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



