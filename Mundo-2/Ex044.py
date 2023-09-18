# Elabore um programa que vai calcular o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento: - á vista: 10% de desconto. - á vista no cartão: 5% de desconto - em até 2x no cartão: preço normal. -3x
# ou mais no cartão: 20% de juros

valor = 1250
print('O valor do produto é R$1250,00')
tipo = input('Vai ser no cartão? ').lower().strip()

if tipo == 'sim':
    parc = input('Deseja parcelar? ').lower().strip()
    if parc == 'sim':
        nump = int(input('Em quantas vezes? '))
        if nump <= 2:
            print(f'O valor é dé R${valor:.2f}')
        else:
            print(f'O valor tem um acréscimo de 20% de juros, o valor a pagar é {valor + (valor * 0.2)}')
    elif parc == 'não':
        print(f'O valor tem um desconto de 5%, o valor a pagar é: {valor - (valor * 0.05)}')
    else:
        print('ERRO!')
elif tipo == 'não':
    print(f'O valor tem um desconto de 10%, o valor a pagar é: {valor - (valor * 0.1)}')
else:
    print('ERRO!')
