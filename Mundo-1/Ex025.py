# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Qual o seu nome completo? ')
pnome = nome.capitalize().split()
if 'Silva'in nome:
    print(f'{pnome[0]}, seu nome possui "Silva"')

else:
    print(f'{pnome[0]}, seu nome não possui "Silva"')
