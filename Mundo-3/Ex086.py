# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a
# matriz na tela, com a formatação correta


matriz = []

for i in range(0, 3):
    valor = int(input(f'Digite um valor para a posição 0:{i} '))
    matriz.append(valor)
for i in range(0, 3):
    valor = int(input(f'Digite um valor para a posição 1:{i} '))
    matriz.append(valor)
for i in range(0, 3):
    valor = int(input(f'Digite um valor para a posição 2:{i} '))
    matriz.append(valor)

print('-='*30)

for i in range(0, 3):
    print(f'[  {matriz[i]}  ]', end=' ')
print('\n')
for i in range(0, 3):
    print(f'[  {matriz[i]}  ]', end=' ')
print('\n')
for i in range(0, 3):
    print(f'[  {matriz[i]}  ]', end=' ')
