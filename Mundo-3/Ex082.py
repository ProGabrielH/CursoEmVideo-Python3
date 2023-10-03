# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores impares digitados, espectivamente. No final, mostre o centeudo das três
# listas geradas

vals = list()
pares = list()
impares = list()

while True:
    num = int(input('Digite um valor: [999 para finalizar] '))
    if num == 999:
        break
    else:
        vals.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Lista normal: {vals}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos impares: {impares}')
