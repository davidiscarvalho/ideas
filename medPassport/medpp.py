import pyrebase
from db_config import init_db
from db_model import Data

config = init_db
firebase = pyrebase.initialize_app(config)

db = firebase.database()

"""
data = {"name": "Bill Doe"}

db.child("users").push(data)
print("Data added to realtime db")

db.child("users").child("OwnKey").set(data)
print("Data added to realtime db")

db.child("users").child("OwnKey").update({"name": "John Doe"})
print("Data updated")

users = db.child("users").get()
print(users.val())

all_users = db.child("users").get()

for users in all_users.each():
    print(users.val())
    print(users.key())


db.child("users").child("M2ZnwXUotntENWoZc33").remove()
print("User removed")
"""
