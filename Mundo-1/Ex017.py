# Crie um programa que receba o cateto oposto e adjacente e calcule a hipotenusa de um triangulo retangulo

import math

cato = float(input('Qual o comprimento do cateto oposto em centimetros? '))
cata = float(input('Qual o comprimento do cateto adjacente em centimetros? '))
hip2 = math.pow(cato, 2) + math.pow(cata, 2) # mais fácil usar o comando "hypot" que vem dentro da biblioteca math
print(f'O valor da hipotenusa nesse triangulo é de {math.sqrt(hip2):.2f}cm')
