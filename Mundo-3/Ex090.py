# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).strip()
aluno['média'] = float(input('Média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'

print(f'O aluno {aluno["nome"].capitalize()} teve média {aluno["média"]:.1f}, logo ele foi {aluno["situação"]}')
