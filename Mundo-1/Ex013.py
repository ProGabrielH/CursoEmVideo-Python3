# Crie um algoritimo que faça o aumento do salário de um empregado
salario = float(input('Qual o salário do funcionário? R$'))
aumento = float(input('Em quantos % deseja aumentar o salário? '))
print(f'O funcionário deixará de receber R${salario:.2f} e recenerá um aumento de {aumento:.0f}%, assim recebendo '
      f'R${salario + (aumento/100 * salario):.2f}')
