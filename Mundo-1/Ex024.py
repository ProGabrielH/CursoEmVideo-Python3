# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número de 0 a 9999: '))
print(f'Número: {num}')
print(f'Unidade: {num % 10} \nDezena: {num // 10 % 10} \nCentena: {num // 100 % 10} \nMilhar: {num // 1000 % 10}')
