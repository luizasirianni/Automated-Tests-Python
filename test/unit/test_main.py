import pytest

import main

def testar_soma():
    num1 = 8
    num2 = 10

    resultado_esperado = 18

    resultado_atual = main.somar_dois_numeros(num1, num2)

    assert resultado_atual == resultado_esperado


#Criar um grupo de parametros para utilizar como massa de testes:
@pytest.mark.parametrize('raio,resultado_esperado',[
    #valores:
                             (6, 113.09733552923255), #teste nº 1
                             (3, 28.274333882308138), #teste nº 2
                             (2, 12.566370614359172), #teste nº 3
                             (10, 314.1592653589793) #teste nº 4
                         ])

def testar_area_circulo(raio, resultado_esperado):

    resultado_atual = main.area_circulo(raio)

    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('largura,comprimento,altura,resultado_esperado',[
    (10, 7, 3, 210),
    (7, 1.5, 3, 31.5),
    (12, 8, 6, 576)
])
def testar_volume_paralelograma(largura, comprimento, altura, resultado_esperado):

    resultado_atual = main.volume_paralelograma(largura,comprimento,altura)

    assert resultado_atual == resultado_esperado