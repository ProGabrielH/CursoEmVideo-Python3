# Crie um programa que sorteie um de 4 nomes escolhidos

import random

n1 = input('Qual o nome do primeiro aluno? ')
n2 = input('Qual o nome do segundo aluno? ')
n3 = input('Qual o nome do terceiro aluno? ')
n4 = input('Qual o nome do quarto aluno? ')
print(f'O aluno que vai limpar o quadro é: {random.choice([n1, n2, n3, n4])}')
