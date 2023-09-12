# Crie um programa que leia a dinstância de uma viagem e calcule a passagem. O valor é de 0.50 cents por km em uma
# viagem até 200km, acima disso é 0.45 cents por km.
dist = float(input('Por favor, informe a distância da viagem: '))
if dist > 200:
    print(f'Viagens com distância acima de 200km tem cobrança de R$0,45 por KM! \nPreço da passagem: R${dist*0.45:.2f}')
else:
    print(f'Viagens com distância abaixo ou igual a 200km tem cobrança de R$0,50 por KM! \nPreço da passagem: R${dist*0.50:.2f}')
