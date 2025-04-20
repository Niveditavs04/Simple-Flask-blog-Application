Description:
The Simple Flask Blog Application is a web-based blog platform developed using Flask, a lightweight WSGI web application framework in Python. This application allows users to create, read, update, and delete blog posts. It serves as a fundamental example of how to build a CRUD (Create, Read, Update, Delete) application using Flask.
Flask is a WSGI application
 A WSGI server is used to run the application, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses.

web server gateway interface
build REST API using flask:
Notion app for notes making
REST?
Endpt. = URL+ DOMAIN +PORT +PATH+ QUERY
HTTP Methods: GET,POST ,PUT , DELETE
              READ CREATE UPDATE DELETE
HTTP HEADERS: AUTHENTICATION TOKEN ,COOKIES

JSON?
JavaScript Object Notation = LANG INDEPENDENT DATA INTERCHANGE FORMAT

windows to wsl = wsl
wsl to windows= ctrl+D
Project Link: Simple Flask Blog Application


Key Features:

User Authentication:

User registration and login functionality.
Password hashing for secure storage.
Session management to maintain user state.
Blog Post Management:

Create new blog posts with a title and content.
Edit existing posts.
Delete posts.
View a list of all posts.
View individual post details.

Database Integration:
Utilizes SQLite for storing user and blog post data.

Template Rendering:

Jinja2 templating engine for rendering HTML pages.
Bootstrap for responsive and modern UI design.

Technical Stack:

Backend: Flask
Frontend: HTML, CSS (Bootstrap), Jinja2
Database: SQLite
Authentication: Flask-Login, Werkzeug for password hashing

Installation and Setup:

1. set up application 
2. connect to db   =In web applications this connection is typically tied to the request. It is created at some point when handling a request, and closed before the response is sent.
3.Blueprints and Views
1.A view function is the code you write to respond to requests to your application. Flask uses patterns to match the incoming request URL to the view that should handle it.
Flaskr will have two blueprints, one for authentication functions and one for the blog posts functions
If the user submitted the form, request.method will be 'POST'. In this case, start validating the input.

request.form is a special type of dict mapping submitted form keys and values. The user will input their username and password.

Validate that username and password are not empty.

If validation succeeds, insert the new user data into the database.

2. Require Authentication in Other Views
Creating, editing, and deleting blog posts will require a user to be logged in. A decorator can be used to check this for each view it’s applied to.


4.Templates
5.blog blueprint

6.here the application gets complete, we can then look up for how to run in production environment
always start with this=
describe the project in .toml file outside flaskr
write command =pip install -e .
7. Steps to Deploy a Flask App on Glitch from GitHub
Create a Glitch Account:

Visit Glitch and sign up for an account (or log in if you already have one).

Import Your GitHub Repository to Glitch: copy url 
Configure the start.sh File
If database error create file: init_db_script.py 
Access Your Deployed App: Once the app is deployed, Glitch will provide you with a live URL like https://your-app-name.glitch.me.



