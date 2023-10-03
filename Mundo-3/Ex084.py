# Faça um programa que liea nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 1- quantas
# pessoas foram cadastradas. 2- Uma listagem com as pessoas mais pesadas. 3- Uma listagem com as pessoas mais leves

pessoas = list()
dados = list()
menores = list()
maiores = list()
menor = 0
maior = 0
resp = 's'

while resp in 'Ss':
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar? [S/N] ').upper().strip()[0]

for i in range(0, len(pessoas)):
    if i == 0 or pessoas[i][1] <= menor:
        menor = pessoas[i][1]
    if i == 0 or pessoas[i][1] >= maior:
        maior = pessoas[i][1]

for i in range(0, len(pessoas)):
    if pessoas[i][1] == menor:
        menores.append(pessoas[i][0])
    if pessoas[i][1] == maior:
        maiores.append(pessoas[i][0])

print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'As pessoas com o maior peso são {maiores} e pesam {maior}Kg')
print(f'As pessoas com o menor peso são {menores} e pesam {menor}Kg')
