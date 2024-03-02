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

tutorial app
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
7. test coverage
