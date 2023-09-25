# Faça um programa que lia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça digitação
# novamente até ter um valor correto

var = 1

while var == 1:
    sex = input('Qual o seu sexo [M/F]: ').strip().upper()
    if sex == 'M' or sex == 'F':
        print('Entrada válida')
        if sex == 'M':
            print('Usuário do sexo MASCULINO')
        else:
            print('Usuário do sexo FEMININO')
        var = 0
    else:
        print('Entrada inválida, tente novamente')
