# Aprimore o desafio anterior, mostrando no final: 1- a soma de todos os valores pares digitados. 2- a soma dos valores
# da terceira coluna. 3- O maior valor da segunda linha

soma = 0
somacol3 = 0
maior = []
matriz = []

for i in range(0, 3):
    valor = int(input(f'Digite um valor para a posição 0:{i} '))
    matriz.append(valor)
    if valor % 2 == 0:
        soma += valor
for i in range(0, 3):
    valor = int(input(f'Digite um valor para a posição 1:{i} '))
    matriz.append(valor)
    maior.append(valor)
    if valor % 2 == 0:
        soma += valor
maior.sort()
for i in range(0, 3):
    valor = int(input(f'Digite um valor para a posição 2:{i} '))
    matriz.append(valor)
    if valor % 2 == 0:
        soma += valor

print('-=' * 30)

print(' '*17, end='')
for i in range(0, 3):
    print(f'[  {matriz[i]}  ]', end='')
print('\n')
print(' '*17, end='')
for i in range(0, 3):
    print(f'[  {matriz[i]}  ]', end='')
print('\n')
print(' '*17, end='')
for i in range(0, 3):
    print(f'[  {matriz[i]}  ]', end='')
print('\n')
print('-=' * 30)

print(f'A soma dos valores pares: {soma}')
print(f'A soma dos valores da terceira coluna: {matriz[2] + matriz[5] + matriz[8]}')
print(f'O maior valor da segunda linha: {maior[-1]}')
