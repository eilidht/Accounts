# Accounts

## Service Specification
The service interface is defined in the spec/accounts.yml file.

## Setting up your environment
These instructions assume that you are running MacOSX with a functioning python version 3.7.0, although they should be broadly applicable
to Unix and Linux variants. If you are running a Windows based operating system please follow the instructions
on the python website.

`brew install pyenv`

`pyenv install 3.7.0`

## Deployment

### Development 
download
`git clone https://github.com/eilidht/Accounts.git`

`cd Accounts`

`pyenv local 3.7.0`

`export FLASK_APP=flaskr`

`export FLASK_ENV=development`

`mkdir logs`

install
`make install-dev`

install database
`make init_db`

run the app
`make run`

### Production
Use a production WSGI server such as nginx. See the flask docs for more info: 
http://flask.pocoo.org/docs/1.0/tutorial/deploy/

## Logging
The log files will be written to the logs folder. There is an access log which records calls to the service  and 
an accounts log which logs accounts created or fetched.

## Testing
`make test`

### postman
Open postman https://www.getpostman.com/ and import the accounts.post

### python tests
`make test`

## Coverage
`make coverage`
An HTML report allows you to see which lines were covered in each file.
This generates files in the htmlcov directory. 
Open htmlcov/index.html in your browser to see the report.
