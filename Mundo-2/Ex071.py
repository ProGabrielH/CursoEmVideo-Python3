# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado e o programa vai informar quantas cédulas de cada valor serão entregues. Considere que o caixa possui
# cédulas de 50, 20, 10 e 1.

print('=-'*30)
print(f'{"BANCO SAVE THE BEES":^60}')
print('=-'*30)

while True:
    valor = float(input('\nInsira o valor a ser sacado: R$'))
    print('\nEJETANDO:')
    if  valor//100>0:
        print(f'\n{valor//100:.0f} notas de R$100')
    valor = valor - (100*(valor//100))
    if valor//50> 0:
        print(f'{valor//50:.0f} notas de R$50')
    valor = valor - (50*(valor//50))
    if valor//20> 0:
        print(f'{valor//20:.0f} notas de R$20')
    valor = valor - (20*(valor//20))
    if valor//10 > 0:
        print(f'{valor//10:.0f} notas de R$10')
    valor = valor - (10*(valor//10))
    if valor//2 > 0:
        print(f'{valor//2:.0f} notas de R$2')
    valor = valor - (2*(valor//2))
    if valor//1 > 0:
        print(f'{valor//1:.0f} moedas de R$1')
    valor = valor - (1*(valor//1))
    if valor//0.50 > 0:
        print(f'{valor//0.50:.0f} moedas de R$0,50')
    valor = valor - (0.50*(valor//0.50))
    if valor//0.25 > 0:
        print(f'{valor//0.25:.0f} moedas de R$0,25')
    valor = valor - (0.25*(valor//0.25))
    if valor//0.10 > 0:
        print(f'{valor//0.10:.0f} moedas de R$0,10')
    valor = valor - (0.10*(valor//0.10))
    if valor//0.05 > 0:
        print(f'{valor//0.05:.0f} moedas de R$0,05')
    valor = valor - (0.05*(valor//0.05))
    if valor//0.01 > 0:
        print(f'{valor//0.01:.0f} moedas de R$0,01')
    valor = valor - (0.01*(valor//0.01))
    while True:
        userr = input('\nDeseja fazer mais um saque? [S/N] ').upper().strip()[0]
        if userr in 'SsNn':
            break
    if userr in 'Nn':
        break
print('\nObrigado pela preferência')
