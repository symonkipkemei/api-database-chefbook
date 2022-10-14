

## Table of contents:
- [Introduction](#intro)
- [Technologies](#tech)
- [project Setup](#projo)
- [Illustrations](#illus)
- [Project Information](#info)
- [Contributing](#contri)
- [Acknowledgments](#know)

<INTRODUCTION>

<h1 id="intro">py-databases</h1>

A cookbook for databases and api based on the examples shared by codingnomads
 
## API Quizes

```
* Exercise 1
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body


* Exercise 2
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

* Exercise 3
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.


* Exercise 4
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.


* Exercise 5
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

* Exercise 6
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

```

## Database Quizes


```
* Exercise 1

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.


* Exercise 2

Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a c of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice


* Exercise 3
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.


* Exercise 4
Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


* Exercise 5
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.




```


<TECHNOLOGIES>

<h1 id="tech">Technologies</h1>

## Builth With
- Python
- mysql

## usage.
Run each exercise to see how it works

<PROJECT-SETUP>

<h1 id="projo">Project Setup</h1>


## Hardware Requirements
- You will need a desktop or a laptop computer
- RAM: A minimum of 4GB RAM is recommended
- Disk Space: You should have at least 5GB free of space on your working hard drive

## Software Requirements

**environment**

The project was created in a wsl 2 (ubuntu/linux environment). 

**Prerequisites**

To get this project up and running locally, you must already have the following installed:
- [python plus the necessary packages installed on your computer](https://www.python.org/downloads/)
- [code editor ](https://code.visualstudio.com/)
- [mysql workbench installed](https://dev.mysql.com/downloads/workbench/)
- mysql server set up on your linux environment()


**simple steps to set up on your local machine**


- $ git clone `$ git clone https://github.com/symonkipkemei/api-database-chefbook.git
- [Set up virtual environment](https://github.com/symonkipkemei/album_search_spotify/wiki/Set-up-virtual-environment/_edit)
- On the terminal, activate the virtual environment ``` source venv/bin/activate ```
- On the terimnal, within the cloned repository, run ```pip install requirements.txt```
- explore the completed examples , try run them by yourself.




<ILLUSTRATIONS>

<h1 id="illus">Illustrations of the game play</h1>

![Image](illustrate/image0.png)
![Image](illustrate/image1.png)
![Image](illustrate/image2.png)




<PROJECT-INFORMATION>

<h1 id="info">Project Information</h1>

## Project Status
- Complete

## Features
- Make it playful

## TODO




<CONTRIBUTING>

<h1 id="contri">🤝 Contributing</h1>

Contributions, issues and feature requests are always welcome!

I love meeting other developers, interacting and sharing.

Feel free to check the [issues page](https://github.com/symonkipkemei/api-database-chefbook e/issues).

### How to Contribute

To get a local copy up and running follow these simple example steps.

```
- Fork the repository
- git clone https://github.com/your_username/api-database-chefbook e
- git checkout develop
- git checkout -b branch name
- git remote add upstream https://github.com/symonkipkemei/api-database-chefbook e
- git pull upstream develop
- git commit -m "commit message"
- git push -u origin HEAD
```


<ACKNOWLEDGMENTS>

<h1 id="know">Acknowledgements</h1>

## Author

👤 **Symon Kipkemei**

- Github: [symonkipkemei](https://github.com/symonkipkemei)
- Twitter: [@symon_kipkemei](https://twitter.com/symon_kipkemei)
- LinkedIn: [Symon kipkemei](https://www.linkedin.com/in/symon-kipkemei/)


## Show your support

Finally, if you've read this far, don't forget to give this repo a ⭐️. They're free . . . .

## Acknowledgments

- [codingnomads](https://codingnomads.co/).
