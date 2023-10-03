# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre: 1- quantas pessoas foram cadastradas. 2- a média de idade do
# grupo. 3- uma lista com todas as mulheres. 4- uma lista com todas as pessoas com idade acima da média.

pessoas = []
dados = {}
resp = 's'
smedia = 0

while resp in 'Ss':
    dados['nome'] = str(input('Nome: ')).strip()
    dados['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    dados.clear()
    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SsNn':
            break
        else:
            print('Resposta inválida, tente novamente')

for i in range(0, len(pessoas)):
    smedia += pessoas[i]['idade']

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A média de idade foi {smedia/len(pessoas):.1f} anos')
print(f'As mulheres cadstradas foram: ', end='')
for i in range(0, len(pessoas)):
    if pessoas[i]['sexo'] in 'Ff':
        print(pessoas[i]['nome'].capitalize(), end=' ')
print(f'\nAs pessoas com a idade acima da média são: ', end='')
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > smedia/len(pessoas):
        print(pessoas[i]['nome'].capitalize(), end=' ')
