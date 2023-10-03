# Crie um programa que vai gerar cindo número aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)

print(f'A lista: {tupla}')
print(f'O maior valor: {sorted(tupla)[-1]}')
print(f'O menor valor: {sorted(tupla)[0]}')
