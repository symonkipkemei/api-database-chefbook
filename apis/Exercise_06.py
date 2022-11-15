'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
import json
import requests
from pprint import pprint


base_url_users = "http://demo.codingnomads.co:8080/tasks_api/users"
base_url_tasks = "http://demo.codingnomads.co:8080/tasks_api/tasks"

def create_new_account():
    email = input("insert your email: ")
    first_name = input("insert your first name: ")
    last_name = input("insert your last name: ")

    file = {
        email,
        first_name,
        last_name
    }

    response = requests.post(base_url_users,json=file)
    
    return response.status_code
    

def view_tasks():
    response = requests.get(base_url_tasks)
    pprint(response.json())

    return response.status_code

def view_completed_tasks():
    param = {
        "completed" : "true"
    }
    response = requests.get(base_url_tasks,param)

    pprint(response.json())

    return response.status_code


def check_status(status_code):
    if status_code == 200:
        print( "succesful")
    elif status_code == 201:
        print( "new resource created")
    else:
        print("there was an error")
    

def create_task():

    id = input("insert userid: ")
    name = input("insert name of task : ")
    description = input("insert description of project: ")
    completed_status = input("complete (y) incomplete (n): ")
    if completed_status == "y":
        complete = True
    elif completed_status == "n":
        complete = False
    else:
        print("wrong input")

    json_complete = json.dumps(complete)

    file = {
        "userId": id,
        "name" : name,
        "description" : description,
        "completed" : json_complete
    }

    json_file = json.dumps(file)

    response = requests.post(base_url_tasks,json=file)

    print(response.status_code)

    return response.status_code


def update_task():
    id = int(input("insert userid: "))
    name = input("insert new task name : ")
    description = input("insert new description of project: ")
    completed_status = input("insert complete (y) incomplete (n): ")

    json_complete = json.dumps(completed_status)
    json_id = json.dumps(id)

    file = {
        "userId":json_id,
        "name" : name,
        "description" : description,
        "completed" : json_complete
    }

    response = requests.put(base_url_tasks + "/162",json=file)
    print(response.status_code)

    return response.status_code


def delete_task():
    response = requests.delete(base_url_tasks + "/161")
    pprint(f"response code : {response.status_code}")

    return response.status_code

status = update_task()
check_status(status)