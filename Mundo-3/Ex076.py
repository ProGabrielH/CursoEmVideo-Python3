# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. no final
# mostre uma listagem de preços, organizando os dados em forma tabular

produtos = ('ARROZ 1KG', 9.39, 'FEIJÃO 1KG', 22, 'QUEIJO RALADO 1KG', 158.12, 'TEMPERO', 21.69, 'CHURRASQUEIRA', 99.90,
            'CONTROLE PS5', 349.90, 'LIQUIDIFICADOR', 160.99)

print('-='*30)
print(f'{"PRODUTOS EM PROMOÇÃO":^60}')
print('-='*30)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<47}', end='')
    else:
        print(f'R$ {produtos[i]:>10.2f}')
print('-='*30)
