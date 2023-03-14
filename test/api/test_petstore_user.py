# testes de api precisam de duas bibliotecas:

import pytest  # framework de testes unitarios
import requests  # framework de testes de API - Requests/Responses
import unittest
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


##################################################

# utilização do put
def testar_alterar_usuario():
    username = 'usuarionumero2'

    status_code_esperado = 200
    code_esperado = 200
    tipo_esperado = 'unknown'
    message_esperado = '8989'

    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('D:/python/Pytest_Iterasys/test/database/user2.json', 'rb'),
        headers=headers
    )

    corpo_da_resposta = resposta.json()

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == message_esperado


# utilização delete

def testar_deletar_usuario():
    username = 'xingsling'

    expected_code = 200
    expected_status_code = 200
    expected_type = 'unknown'
    expected_message = username

    response = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )

    # condicionais estilo switch case utilizando o match
    if response.status_code == 200:
        #status code 200 = apagar um usuário já existente
        response_body = response.json()
        print('Usuario deletado com sucesso')
        assert response.status_code == expected_status_code
        assert response_body['code'] == expected_code
        assert response_body['type'] == expected_type
        assert response_body['message'] == expected_message

    elif response.status_code == 400: #fez a chamada sem passar o usuário
        print('Usuario invalido')

    elif 404:
        print('Usuario nao encontrado')

def testar_login_usuario():
    username = 'xingsling'
    password = 'lulu123'
    code_esperado = 200
    status_code_esperado = 200
    type_esperado = 'unknown'
    inicio_message_esperado = 'logged in user session:'

    resposta = requests.get(
        url=f'{base_url}/login?username={username}&password={password}',
        headers=headers
    )

    response_body = resposta.json()
    assert resposta.status_code == status_code_esperado
    assert response_body['code'] == code_esperado
    assert response_body['type'] == type_esperado
    assert response_body['message'].find(inicio_message_esperado) != -1
    #assert (inicio_message_esperado in response_body['message'])
    print('Login efetuado com sucesso')