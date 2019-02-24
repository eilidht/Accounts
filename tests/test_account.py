import pytest
from flaskr.db import get_db
import json


def test_create_account(client, app):

    data = {'account_name': 'Brukskonto', 'available_balance': 0}
    url = '/v1/accounts'

    assert client.get(url).status_code == 200
    client.post(url, json=data)

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM account').fetchone()[0]
        assert count == 3
