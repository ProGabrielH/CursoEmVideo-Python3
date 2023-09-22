# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep as s

print('~' * 20)
print('CONTAGEM PARA OS FOGOS')
print('~' * 20)

for i in range(10,0,-1):
    print(i)
    s(1)

print('FELIZ ANO NOVO')