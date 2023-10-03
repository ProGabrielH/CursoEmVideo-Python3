# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a médiade cada um e permita que o usuário possa mostrar notas de cada aluno individualmente

notas = []
alunos = []
resp = 's'
resp2 = 's'

while resp in 'Ss':
    notas.append(str(input('Nome do Aluno: ')).strip().capitalize())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas[:])
    notas.clear()
    while True:
        resp = input('Deseja adicionar outro aluno: [S/N]').strip().upper()[0]
        if resp in 'SsNn':
            break
        else:
            print(f'Erro, {resp} não é uma resposta válida, tente novamente')

print('-'*30)
print(f'Nº {"Nome":<12} {"M":^4}')
for c, i in enumerate(alunos):
    print(f'{c} {alunos[c][0]:-<12} {(alunos[c][1] + alunos[c][2])/2:^4.1f}')

while resp2 in 'Ss':
    aln = int(input('Insira a numeração do aluno: '))
    print(f'\n{alunos[aln]}')
    while True:
        resp2 = input('\nDeseja ver outro aluno em específico? [S/N]').lower().strip()[0]
        if resp2 in 'SsNn':
            break
        else:
            print(f'Erro, {resp2} não é uma resposta válida, tente novamente')
