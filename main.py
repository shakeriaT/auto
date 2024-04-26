#Repo pattern = CRUD

#CREATE

#READ

#UPDATE

#DELETE
import os
import pickle as list

db = open("main.py/my_list", "r")
response = db.read()
print(response)

# imports
import list

# CRUD: Create function
def create(obj):
    if not os.path.exists('main.py/my_list'):
        open("main.py/my_list", mode="x")
    with open("main.py/my_list", mode="w") as db:
        list.dump(obj, db)

# CRUD: Read function
def read():
    pass

def update(obj):
    with open("main.py/my_list", mode="a") as db:
        list.dump(obj, db)

events = read()
create(events)