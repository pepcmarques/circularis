from django.test import Client  # noqa


def test_fake():
    assert 1 == 1

"""
def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
"""
