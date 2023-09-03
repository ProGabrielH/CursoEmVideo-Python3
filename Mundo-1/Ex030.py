# Crie um programa que leia um numero inteiro e mostre na tela se ele é impar ou par
from math import trunc
num = float(input('Informe um número para saber se ele é impar ou par: '))
if trunc(num) % 2 == 0:
    print('O numero informado é PAR!')
else:
    print('O número informado é IMPAR!')
