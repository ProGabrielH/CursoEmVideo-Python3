# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre: 1- qual é o total gasto na compra, 2- quantos produtos custam mais de 1000 reais, 3- qual o nome do
# produto mais barato

preco_total = maisdemil = 0
preco_mais_barato = float('inf')

print('=-'*30)
print(f'{"AUTO ATENDIMENTO":^60}')
print('=-'*30)

while True:
    nome = input('\nNome do produto: ').upper()
    preco = float(input('Preço do produto: R$'))
    preco_total += preco
    if preco >= 1000:
        maisdemil += 1
    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome
    while True:
        userresp = input('\nDeseja adicionar mais produtos? [S/N]').strip().upper()[0]
        if userresp in 'SsNn':
            break
    if userresp not in 'Ss':
        break


print(f'\nO total a ser pago é: R${preco_total:.2f} \nA quantidade de produtos mais caros que mil foi: {maisdemil} \nO produto'
      f' mais barato foi: {produto_mais_barato} que custou R${preco_mais_barato:.2f}')
