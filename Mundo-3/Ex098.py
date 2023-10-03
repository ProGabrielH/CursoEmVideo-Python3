# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a
# contagem. Seu programa tem que realizar três contagens através da função criada. 1- de 1 até 10, de 1 em 1. 2- de 10
# até 0, de 2 em 2. 3- uma contagem personalizada
from time import sleep


def separação():
    print('-'*30)


def contador(a, b, c):
    if c < 0 and b > a:
        for i in range(b, a, c):
            print(i, end=' ')
            sleep(0.3)
    elif c < 0 and a > b:
        for i in range(a, b, c):
            print(i, end=' ')
            sleep(0.3)
    elif b < a:
        for i in range(a, b, 0-c):
            print(i, end=' ')
            sleep(0.3)
    else:
        for i in range(a, b+1, c):
            print(i, end=' ')
            sleep(0.3)


separação()
print('Contagem de 1 a 10 de 1 por 1')
for i in range(1, 11):
    print(i, end=' ')
    sleep(0.3)
print()
separação()
print('Contagem de 0 a 10 de 2 em 2')
for i in range(10, 0, -2):
    print(i, end=' ')
    sleep(0.3)
print()
separação()
inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
print()
separação()
