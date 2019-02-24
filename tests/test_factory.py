from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_running(client):
    assert client.get('/v1/accounts').status_code == 200
