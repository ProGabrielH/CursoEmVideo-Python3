# Faça um programa que tenha uma função chamada maior()m que receba vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep
def separação():
    print('-'*30)


def maior(*num):
    print(f'Analisando {num}')
    for i in num:
        print(i, end=' ')
        sleep(0.3)
    print(f'\nForam passados {len(num)} valores')
    print(f'O maior valor é: {max(num)}')


separação()
maior(4, 6, 5, 1, 10, 4, 5, 7, 9, 5)
separação()
maior(9, 8, 7, 3)
separação()
maior(1, 6, 5,)
separação()
