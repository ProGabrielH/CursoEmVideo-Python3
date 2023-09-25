# Crie um programa que lia dois valores e mostre um menu na tela 1 - somar 2 - multiplicar 3 - maior 4 - novos números
# 5 - sair do programa

var1 = int(input('Valor 1: '))
var2 = int(input('Valor 2: '))
uso = 0

while not (uso == 5):
    print('\n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR')
    uso = int(input('O que deseja fazer? '))
    if uso == 1:
        print(f'A soma de {var1} e {var2} é equivalente á {var1+var2}')
    elif uso == 2:
        print(f'A multiplicação de {var1} e {var2} é equivalente á {var1*var2}')
    elif uso == 3:
        if var1 > var2:
            print(f'O maior valor é {var1}')
        elif var1 < var2:
            print(f'O maior valore é {var2}')
        else:
            print('Os valores são iguais')
    elif uso == 4:
        var1 = int(input('Valor 1: '))
        var2 = int(input('Valor 2: '))
    elif uso == 5:
        print('Encerrando programa')
    else:
        print('Valor inválido')
