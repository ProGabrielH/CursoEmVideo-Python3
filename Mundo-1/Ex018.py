# Crie um programa que leia o valor de um ângulo e mostre seu valor de seno, cosseno e tangente

from math import cos, sin, tan, radians

angulo = int(input('Qual o valor do ângulo? '))
print(f'Seus valores de seno, coseno e tangente são \nSEN = {sin(radians(angulo)):.2f} \nCOS = {cos(radians(angulo)):.2f} \nTAN = {tan(radians(angulo)):.2f}')
