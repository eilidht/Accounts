from flask import (
    Blueprint, flash, current_app, request
)
from werkzeug.exceptions import abort
import json

from flaskr.db import get_db
from flask import jsonify

bp = Blueprint('account', __name__, url_prefix='/v1')


@bp.route('/accounts', methods=('GET', 'POST'))
def accounts():
    if request.method == 'POST':

        current_app.logger.info('POST called on /accounts',)

        account_nickname = request.get_json()['account_nickname']
        account_owner_name = request.get_json()['account_owner_name']
        account_type = request.get_json()['account_type']
        currency = request.get_json()['currency']

        db = get_db()
        error = None

        # if not account_name:
        #     error = 'Account data is required.'  # TODO test other inputs
        if error is None:
            db.execute(
                'INSERT INTO account (account_nickname, account_owner_name, account_type, currency) VALUES (?,?,?,?)',
                (account_nickname, account_owner_name, account_type, currency)
                # 'INSERT INTO account (account_name, available_balance) VALUES (?, ?)',
                # (account_name, available_balance)
            )
            db.commit()
            # TODO fetch other data too
            account = db.execute(
                'SELECT id, account_name, available_balance FROM account where id = last_insert_rowid()'
                ).fetchone()

            # TODO refactor
            account_as_dict = {'id': account[0],
                               'account_name': account[1],
                               'available_balance': account[2]}

            return jsonify(account_as_dict), 201

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

        return jsonify(result)
