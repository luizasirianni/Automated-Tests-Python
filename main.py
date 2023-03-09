import math

import pytest

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Não é possível dividir por 0"
def somar_dois_numeros(num1, num2):
    return num1 + num2

def diminuir_dois_numeros(num1, num2):
    return num1 - num2

def area_quadrado(base, altura):
    return base * altura

def area_retangulo(largura, comprimento):
    return largura * comprimento

def area_triangulo(lado1, lado2):
    return lado1 * lado2 / 2

def area_circulo(raio):
    return math.pi * raio**2

# ====================== TESTES ==========================
if __name__ == '__main__':

    resultado = somar_dois_numeros(5,7)
    print(f'a soma eh de {resultado}')

    resultado = diminuir_dois_numeros(7,2)
    print(f'a subtracao eh de {resultado}')

    resultado = dividir_dois_numeros(5, 1)
    print(f'a divisao eh de {resultado}')

    resultado = multiplicar_dois_numeros(1, 4)
    print(f'a multiplicacao eh de {resultado}')

    resultado =area_quadrado(5, 2)
    print(f'a area do quadrado eh {resultado}')

    resultado = area_retangulo(8, 5)
    print(f'a area do retangulo eh {resultado}')

    resultado = area_triangulo(3, 5)
    print(f'a area do triangulo eh {resultado}')

    resultado = area_circulo(6)
    print(f'a area do circulo eh {resultado}')


def testar_soma():
    num1 = 8
    num2 = 2

    resultado_esperado = 10

    resultado_atual = somar_dois_numeros(num1, num2)

    assert resultado_atual == resultado_esperado

def testar_multiplicacao():
    num1 = 10
    num2 = 2

    resultado_esperado = 20

    resultado_atual = multiplicar_dois_numeros(num1,num2)

    assert resultado_atual == resultado_esperado


def testar_subtracao():
    num1 = 16
    num2 = 6

    resultado_esperado = 10
    resultado_atual = diminuir_dois_numeros(num1,num2)

    assert resultado_atual == resultado_esperado

def testar_divisao():
    num1 = 10
    num2 = 2

    resultado_esperado = 5
    resultado_atual = dividir_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_atual
def testar_area_quadrado():
    base = 10
    altura = 10

    resultado_esperado = 100
    resultado_atual = area_quadrado(base, altura)

    assert resultado_atual == resultado_esperado

def testar_area_retangulo():
    comprimento = 8
    largura = 5

    resultado_esperado = 40
    resultado_atual = area_retangulo(comprimento, largura)

    assert resultado_atual == resultado_esperado

def testar_area_triangulo():
    lado1 = 3
    lado2 = 5

    resultado_esperado = 7.5
    resultado_atual = area_triangulo(lado1, lado2)

    assert resultado_atual == resultado_esperado
