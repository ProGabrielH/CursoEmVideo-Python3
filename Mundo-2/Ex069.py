# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# ao usuário se quer ou não continuar. no final mostre: 1- quantos tem mais de 18 anos, 2- quantos homens foram
# cadastrados, 3- quantas mulheres tem menos de 20 anos

maiores = homens = mdmenores = 0
print('=-'*30)
print(f'{"CADASTRO DE USUÁRIO":^60}')
print('=-'*30)

while True:
    print('\n')
    print('-'*60)
    print(f'{"NOVO USUÁRIO":^60}')
    print('-'*60)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
        if sexo in 'FfMm':
            break
        else:
            print('Entrada inválida')
    if idade >= 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mdmenores += 1
    respuser = input('Deseja cadastrar um novo usuário? [S/N] ').strip().upper()[0]
    if respuser not in 'Ss':
        break
print(f'\nForam cadastrados {maiores} usuários com mais de 18 anos \nForam cadastrados {homens} usuários do sexo masculino'
      f'\nForam cadastradas {mdmenores} usuários do sexo feminino com menos de 20 anos')
print('Obrigado por usar nosso sistema')
