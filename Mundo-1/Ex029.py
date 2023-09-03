# Escreva um programa que receba a velocidade de um carro, e multe-o se estiver acima de 80, sendo 7 reais para cada km acima
vel = int(input('A que velocidade o carro passou no velocímetro? '))
if vel > 80:
    print(f'Velocidade acima do limite da via, multa de R${(vel-80)*7:.2f}!')
else:
    print('Velocidade abaixo do limite da via, sem multa!')
