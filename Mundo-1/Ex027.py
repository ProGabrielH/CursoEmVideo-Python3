# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo: ')
nomed = nome.title().split()

print(f'Primeiro nome: {nomed[0]} \nÚltimo nome: {nomed[-1]}')