from flask import (
    Blueprint, flash, current_app, request, abort
)

from flaskr.db import get_db
from flask import jsonify

bp = Blueprint('account', __name__, url_prefix='/v1')

valid_account_types = ["DEPOSIT", "SAVING", "CURRENCY"]


@bp.route('/accounts', methods=('GET', 'POST'))
def accounts():
    if request.method == 'POST':
        current_app.logger.info('POST called on /v1/accounts with data: \t{}'.format(request.get_json()))

        try:  # reading input data
            account_name = request.get_json()['account_name']
            account_nickname = request.get_json()['account_nickname']
            account_owner_name = request.get_json()['account_owner_name']
            account_type = request.get_json()['account_type']
            currency = request.get_json()['currency']
        except Exception as e:
            current_app.logger.error('An exception occurred: \t{}'.format(e))
            abort(400)

        db = get_db()

        error = validate_account_type(account_type)

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

        current_app.logger.error('An error occurred: \t{}'.format(error))
        return error, 400

    if request.method == 'GET':
        current_app.logger.info('GET called on /v1/accounts')
        db_accounts = get_db().execute(
            select_row_items(),
        ).fetchall()

        accounts_list = []

        for account_row in db_accounts:
            account = account_from_row(account_row)
            accounts_list.append(account)

        result = {'accounts': accounts_list}

        return jsonify(result)


def validate_account_type(account_type):
    error = None
    if account_type not in valid_account_types:
        error = 'Account type {} is not valid'.format(account_type)

    return error


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
