import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}


def test_criar_pet():
    status_code = 200
    nome_pet = 'Snoopy'
    tag_esperada = 'vacinado'

    resposta = requests.post(
        url=base_url,
        data=open('D:/python/Pytest_Iterasys/test/database/pet1.json', 'rb'),
        headers=headers
    )

    corpo_resposta = resposta.json()

    print(resposta)
    print(resposta.status_code)
    print(corpo_resposta)

    assert resposta.status_code == status_code
    assert corpo_resposta['type'] == 'unknown'
    # assert corpo_resposta['tags.name'] == tag_esperada
    #TODO: verificar KeyError ao usar a tag 'name'