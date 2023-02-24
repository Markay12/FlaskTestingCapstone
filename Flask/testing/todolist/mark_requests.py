## requests test file to add todolist items automatically
import requests


requests.post("http://127.0.0.1:8888/todo", 
                  json={"Title":"Get Groceries", 
                        "Description":"Go to Trader Joes, Fry's and Costco Today"})

requests.post("http://127.0.0.1:8888/todo",
                  json={"Title":"Go to Class",
                        "Description":"Go to DAT401, BIO799, EEE499 Classes"})

requests.post("http://127.0.0.1:8888/todo",
                  json={"Title":"Finish Capstone Project",
                        "Description":"Work on .NET and Flask Applications with Unity Editor"})


