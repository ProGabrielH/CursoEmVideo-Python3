# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos elevai pagar. Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será negado

valor_casa =  float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
parcelas = int(input('Em quantos anos você deseja parcelar? '))

valor_mensal = valor_casa / (parcelas*12)

if valor_mensal <= 0.3 *salario:
    print(f'Empréstimo APROVADO, O valor que deverá ser pago mensalmente durante o prazo de {parcelas} anos é de '
          f'R${valor_mensal:.2f}')
else:
    print(f'Valor mensal é de R${valor_mensal:.2f}, o que excede o limite de 30% do salário por mês. Empréstimo NEGADO')
