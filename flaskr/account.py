from flask import (
    Blueprint, flash, current_app, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import json

from flaskr.db import get_db

bp = Blueprint('account', __name__, url_prefix='/v1')


@bp.route('/accounts', methods=('GET', 'POST'))
def accounts():
    if request.method == 'POST':

        # import ipdb
        # ipdb.set_trace()

        current_app.logger.info('POST called on /accounts',)

        account_name = request.get_json()['account_name']
        available_balance = int(request.get_json()['available_balance'])

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

        result = {'accounts': accounts}

        return json.dumps(result)
