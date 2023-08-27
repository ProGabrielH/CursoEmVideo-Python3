# Crie um algorítimo que leia quanto dinheiro uma pessoa tem e diga quantos dolares pode comprar
din = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${din:.2f} você pode comprar US${din/4.93:.2}')
