# Crie um algoritimo que calcule a dimenssão e quantos litros de tinta vai usar, levando em consideração 2l pra 1m
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
print(f'A dimensão da parede é de {largura}m x {altura}m e sua área é de {area:.3f}m²')
print(f'para pintar a parede, você precisará de {area/2:.3f}l de tinta')