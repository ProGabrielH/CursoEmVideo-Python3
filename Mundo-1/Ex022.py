# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = input('Qual o seu nome? ')
divisao = nome.split()
print(f'O nome em maiúsculo: {nome.strip().upper()} \nO nome em minúsculo {nome.strip().lower()}')
print(f'A quantidade de letras: {len(nome.replace(" ", ""))}')
print(f'O primeiro nome, {divisao[0]}, tem {len(divisao[0])} letras')

