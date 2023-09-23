# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

lista_peso = []
for i in range(0,5):
    peso = float(input(f'Digite o peso {i+1}: '))
    lista_peso.append(peso)

lista_peso.sort()
print(f'O menor peso foi: {lista_peso[0]:.1f}Kg \nO maior peso foi: {lista_peso[-1]:.1f}Kg')
