from django.test import Client


def test_status_cod(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
