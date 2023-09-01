# Crie um programa que sorteie uma ordem de 4 nomes

from random import shuffle

n1 = input('Qual o nome do primeiro aluno? ')
n2 = input('Qual o nome do segundo aluno? ')
n3 = input('Qual o nome do terceiro aluno? ')
n4 = input('Qual o nome do quarto aluno? ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')
