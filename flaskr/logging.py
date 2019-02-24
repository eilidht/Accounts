import logging
from flask import current_app


def init_logging():
    logger = logging.getLogger('flask')
    hdlr = logging.FileHandler('logs/accounts.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

    # access log from the WSGI
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler('logs/access.log')
    logger.addHandler(handler)
