# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule
# e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import date

registro = {}

while True:
    registro['nome'] = str(input('Nome: ')).strip().capitalize()
    anonasc = int(input('Ano de nascimento: '))
    registro['idade'] = date.today().year - anonasc
    registro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    registro['clt'] = int(input('Carteira de trabalho (0 caso não possuir): '))
    if registro['clt'] == 0:
        print(f'Nome: {registro["nome"]}')
        print(f'Idade: {registro["idade"]}')
        print(f'Não possui carteira de trabalho')
        break
    registro['contratação'] = int(input('Ano de contratação: '))
    registro['salário']= float(input('Salário: '))

    print(f'Nome: {registro["nome"]}')
    print(f'Idade: {registro["idade"]}')
    if 15 - (registro['contratação'] - date.today().year) <= 0:
        print('Já possui 15 anos de contribuição com o INSS')
        if registro['sexo'] in 'Mm':
            if 65 - registro['idade'] <= 0:
                print('Já é possível se aposentar')
                break
            else:
                print(f'Irá se aposentar com {registro["idade"]+(65 - registro["idade"])} anos')
                break
        elif registro['sexo'] in 'Ff':
            if 62 - registro['idade'] <= 0:
                print('Já é possível se aposentar')
                break
            else:
                print(f'Irá se aposentar em {registro["idade"]+(62 - registro["idade"])} anos')
                break
    else:
        if registro['sexo'] in 'Mm':
            print(f'Irá se aposentar com '
                  f'{registro["idade"] + (65-registro["idade"]) + 15 - (registro["contratação"] - date.today().year)}'
                  f' anos')
            break
        else:
            print(f'Irá se aposentar com '
                  f'{registro["idade"] + (62 - registro["idade"]) + 15 - (registro["contratação"] - date.today().year)}'
                  f' anos')
            break
