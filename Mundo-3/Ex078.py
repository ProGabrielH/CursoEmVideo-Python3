# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista

lista = []
posmin = []
posmax = []

for i in range(0,5):
    num = int(input('Digite um valor: '))
    lista.append(num)

menor = min(lista)
maior = max(lista)

for c, v in enumerate(lista):
    if v == menor:
        posmin.append(c)
    if v == maior:
        posmax.append(c)

print(f'A lista: {lista}')
print(f'O menor valor da lista é {menor} e está nas posições {posmin}')
print(f'O maior valor da lista é {maior} e está nas posições {posmax}')
