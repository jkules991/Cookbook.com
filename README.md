# Cookbook.com
This repository is my deliverable for the DevOps Core Fundamental Project.

## Contents:
* [Project Description](#Project-Description)  
* [Database Design](#Database-Design)
* [Risk Assessment](#Risk-Assessment)
* [App Summary](#App-Summary)
* [Testing](#Testing)

## Project Description:  
This is a project to deliver a functional CRUD app. The requirements were to use Flask and to store data on a MySQL database with at least two tables connected by a relationship. I chose to create a Cookbook app that would allow the user to store Recipes in the database, view them, edit them and delete them. 

## Database Design:
I designed 2 tables. Table called “Recipes” and a table called “Instructions”. The “Instructions” table contains the foreign key “recipe_id” which is connected to the “Recipes” table primary key called “id”.  

![EDR](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/edr.png)   


## Risk Assessment:
As per the requirements I conducted a Risk assessment in which I name some of the possible security issues this app might be a target of.
As far as mitigation is concerned, I found that SQL alchemy provided a lot of protection regarding database risks. It acts as a buffer between the users and the database, and also allows us to use environmental keys and connections.
Given that at the moment we don’t have any “Log in” functionality and don’t store any critical user data, the impact to any other form of breaches would be minimal.
   

![RISK_ASSESSMENT](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/Threat%20assement.png)  
  


# App Summary:  
The app starts at the “Homepage” where we have two options, to “Add a Recipe” or to “Find your Recipes”.

![HOMEPAGE](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/Homepage.png)

Clicking Add a Recipe takes us to the “create” page where we input the information for the “Recipes” table. After clicking “Submit” we are redirected to the “create2” page where we input the information for the “Instructions” table. Then we are redirected back to the “Homepage”


![CREATE](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/Create2.png)						![CREATE2](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/Create2.png) 

When we click on the “Find your Recipes” from the “Homepage”, we are redirected to the search page where we see a dropdown option list to choose which attribute to search by.

![SEARCH](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/Search.png)					![SEARCH_BY_NAME](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/search%20by%20name.png)

When we submit the request, we are presented with all the Recipes with all the information except the primary and foreign keys, that have the queried attribute.
Underneath each Recipe are buttons that will perform a function. The “Edit” button and the “Delete” button.

![SEARCH_RESULTS](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/Search%20results.png)

The delete button will automatically delete the selected Recipe entry and print that the entry was deleted, while the edit button redirects us to the “Edit Page” where we can replace any data.

![DELETED](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/Deleted.png)							![EDIT](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/edit%20recipe%20page.png)


## Testing:  
I performed Unit testing as required. I tested the GET method for all pages and every functionality except the UPDATE functionality. Only the test for the CREATE functionality failed, as it needed a variable from a previous function, however the function does work as intended.

![TESTING](https://github.com/jkules991/cookbook.com/blob/aba685ca75963f26b1b4128a2c5ce5758cf0123f/pictures/Testing.png)