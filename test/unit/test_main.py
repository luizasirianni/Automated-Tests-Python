import pytest

import main

def testar_soma():
    num1 = 8
    num2 = 10

    resultado_esperado = 18

    resultado_atual = main.somar_dois_numeros(num1, num2)

    assert resultado_atual == resultado_esperado

def testar_area_circulo():
    raio = 6

    resultado_esperado = 113.09733552923255

    resultado_atual = main.area_circulo(raio)

    assert resultado_atual == resultado_esperado

