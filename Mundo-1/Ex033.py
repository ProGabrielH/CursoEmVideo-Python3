# Faça um programa que leia 3 números e mostre qual o menor e qual é o maior.
lista = []

for i in range(0, 3):
    elem = int(input('Insira um número para a lista: '))
    lista.append(elem)

lista.sort()
print(f'Menor valor da lista: {lista[0]} \nMaior valor da lista: {lista[-1]}')
