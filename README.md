# Accounts

## Requirements
python 3.7.0

pip install flask

pip install python-dotenv

## Deployment

### Development 
`flask run`

### Production
Use a production WSGI server such as nginx.

## Logging
The log files will be written to the logs folder. There is an access log which records calls to the service  and 
an accounts log which logs accounts created or fetched.