# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número e
# a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial
from math import factorial

num = 0
resp = 'n'

def fatorial(a, b):
    fac = factorial(a)
    if b in 'Ss':
        for i in range(1, a+1):
            if i == a:
                print(i, '=', fac)
            else:
                print(i, 'x ', end='')
    else:
        print(fac)


num = int(input('Digite o número para ser calculado o fatorial: '))
resp = str(input('Deseja ver o cáculo [S/N]: ')).strip().upper()[0]

fatorial(num, resp)
