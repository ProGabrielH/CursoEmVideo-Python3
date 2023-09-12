# Crie um programa que atribua aumentos de uma empresa, para salários superiores a R$1.250,00 aumente em 10%, para
# salários menores ou iguais, aumente em 15%

salaraio = float(input('Atualmente, qual o valor do salário do funcionário? R$'))
if salaraio <= 1250:
    print(f'O salário com aumento de 15% será de: R${salaraio + (salaraio*0.15):.2f}')
else:
    print(f'O salário com aumento de 10% será de: R${salaraio + (salaraio*0.10):.2f}')
