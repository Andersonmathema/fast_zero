from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização do teste)
    response = client.get('/')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert (tudo ok)
    assert response.json() == {'message': 'Olá mundo'}  # Assert


# Exercicio Aula 02
def test_read_ola_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/ola')
    assert response.status_code == HTTPStatus.OK
    texto = """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
    assert response.text == texto
