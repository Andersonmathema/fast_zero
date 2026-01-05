from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():

    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_exe1_deve_retornar_ola_mundo():

    client = TestClient(app)

    response = client.get('/exe1')

    assert '<h1> Olá Mundo </h1>' in response.text
    assert response.status_code == HTTPStatus.OK
