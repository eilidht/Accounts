from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import simplejson

from flaskr.db import get_db

bp = Blueprint('account', __name__, url_prefix='/v1')




@bp.route('/accounts', methods=('GET', 'POST'))
def accounts():
    if request.method == 'POST':
        # account_data = request.body()  # TODO use input data

        account_name = 'a test account'
        available_balance = 1000

        db = get_db()
        error = None

        if not account_name:
            error = 'Account data is required.'  # TODO test other inputs
        if error is None:
            db.execute(
                'INSERT INTO account (account_name, available_balance) VALUES (?, ?)',
                (account_name, available_balance)
            )
            db.commit()
            return 'account created'

        flash(error)
        return 'There was an error when creating the account'

    if request.method == 'GET':
        db_accounts = get_db().execute(
            'SELECT id, account_name, available_balance FROM account',
        ).fetchall()

        accounts = []

        for account in db_accounts:
            account_as_dict = {'id': account[0],
                               'account_name': account[1],
                               'available_balance': account[2]}
            accounts.append(account_as_dict)

        return simplejson.dumps(accounts)
