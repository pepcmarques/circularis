from django.test import Client


def test_to_pass():
    assert 1 == 1


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
