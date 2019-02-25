from flask import (
    Blueprint, flash, current_app, request
)

from flaskr.db import get_db
from flask import jsonify

bp = Blueprint('account', __name__, url_prefix='/v1')


@bp.route('/accounts', methods=('GET', 'POST'))
def accounts():
    if request.method == 'POST':

        current_app.logger.info('POST called on /accounts',)

        account_name = request.get_json()['account_name']
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
                'INSERT INTO account (account_name, account_nickname, account_owner_name, account_type, currency) '
                'VALUES (?,?,?,?,?)',
                (account_name, account_nickname, account_owner_name, account_type, currency)
            )
            db.commit()
            account_row = db.execute(
                select_row_items() +
                ' WHERE id = last_insert_rowid()'
                ).fetchone()

            account = account_from_row(account_row)

            return jsonify(account), 201

        flash(error)
        return 'There was an error when creating the account'

    if request.method == 'GET':
        db_accounts = get_db().execute(
            select_row_items(),
        ).fetchall()

        accounts_list = []

        for account_row in db_accounts:
            account = account_from_row(account_row)
            accounts_list.append(account)

        result = {'accounts': accounts_list}

        return jsonify(result)


def select_row_items():
    return 'SELECT id, ' \
           'account_name, ' \
           'account_nickname, ' \
           'account_owner_name, ' \
           'account_type, ' \
           'currency, ' \
           'available_balance, ' \
           'booked_balance, ' \
           'status ' \
           'FROM account'


def account_from_row(account_row):
    return {'account_number': str(account_row[0]),
            'account_name': account_row[1],
            'account_nickname': account_row[2],
            'account_owner_name': account_row[3],
            'account_type': account_row[4],
            'currency': account_row[5],
            'available_balance': str(account_row[6]),
            'booked_balance': str(account_row[7]),
            'status': account_row[8]}
