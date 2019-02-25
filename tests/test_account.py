from flaskr.db import get_db


def test_create_account(client, app):

    expected_account = {
        "account_number": "4",
        "account_name": "Brukskonto",
        "account_nickname": "Min Brukskonto",
        "account_owner_name": "Ola Nordmann",
        "account_type": "DEPOSIT",
        "currency": "NOK",
        "available_balance": "0",
        "booked_balance": "0",
        "status": "open"
    }

    input_data = {
        "account_name": "Brukskonto",
        "account_nickname": "Min Brukskonto",
        "account_owner_name": "Ola Nordmann",
        "account_type": "DEPOSIT",
        "currency": "NOK"
    }
    url = '/v1/accounts'

    assert client.get(url).status_code == 200
    response = client.post(url, json=input_data)
    assert response.status_code == 201  # Created

    # Check that another account has been added to the database
    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM account').fetchone()[0]
        assert count == 4

    assert response.json == expected_account


def test_get_accounts(client):

    expected_result = {
        "accounts": [
            {
                "account_number": "1",
                "account_name": "Brukskonto",
                "account_nickname": "Min Brukskonto",
                "account_owner_name": "Ola Nordmann",
                "account_type": "DEPOSIT",
                "currency": "NOK",
                "available_balance": "10000",
                "booked_balance": "8000",
                "status": "open"
            },
            {
                "account_number": "2",
                "account_name": "Sparekonto",
                "account_nickname": "Min Sparekonto",
                "account_owner_name": "Ola Nordmann",
                "account_type": "SAVING",
                "currency": "NOK",
                "available_balance": "50000",
                "booked_balance": "50000",
                "status": "open"
            },
            {
                "account_number": "3",
                "account_name": "Valutakonto",
                "account_nickname": "Min Valutakonto",
                "account_owner_name": "Ola Nordmann",
                "account_type": "CURRENCY",
                "currency": "USD",
                "available_balance": "5000",
                "booked_balance": "5000",
                "status": "open"
            }
        ]
    }
    url = '/v1/accounts'

    response = client.get(url)
    assert response.status_code == 200
    assert response.json == expected_result
