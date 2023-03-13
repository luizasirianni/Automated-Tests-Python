# testes de api precisam de duas bibliotecas:

import pytest  # framework de testes unitarios
import requests  # framework de testes de API - Requests/Responses

# Passar o endereço da API - URL base
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}


def testar_criar_usuario():
    # configura usuario

    status_code_esperado = 200
    code_esperado = 200
    type_esperado = "unknown"
    message_esperado = "1001"

    # executa

    resposta = requests.post(  # faz a requisição passando:
        url=base_url,  # o endpoint da API (url)
        data=open('D:/python/Pytest_Iterasys/test/database/user1.json', 'rb'),
        # o body JSON  ----- 'rb' dá acesso para ler o arquivo
        headers=headers  # o header com o content-type
    )

    # formatação

    corpo_da_resposta = resposta.json()  # formata como JSON

    print(resposta)  # resposta bruta
    print(resposta.status_code)  # status code
    print(corpo_da_resposta)  # resposta formatada

    # valida

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperado


def testar_consultar_usuario():

    status_code = 200
    id = 1001
    username = 'xingsling'
    firstName = 'Xings'
    lastName = 'Ling'
    email = 'xingsling@gmail.com'
    password = 'lulu1234'
    phone = '351898989'
    userStatus = 0

    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers,
    )

    corpo_da_resposta = resposta.json()  # formata como JSON

    print(resposta)  # resposta bruta
    print(resposta.status_code)  # status code
    print(corpo_da_resposta)  # resposta formatada

    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['firstName'] == firstName
    assert corpo_da_resposta['lastName'] == lastName
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['password'] == password
    assert corpo_da_resposta['phone'] == phone
    assert corpo_da_resposta['userStatus'] == userStatus

