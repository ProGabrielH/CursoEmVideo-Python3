# Crie um programa que calcule o preço do aluguel de um carro levando 60 reais o dia e 15 centavos o km rodado
dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos kilometros foram rodados? '))
aluguel = (dias * 60) + (km * 0.15)
print(f'O total a pagar é: R${aluguel:.2f}!')
