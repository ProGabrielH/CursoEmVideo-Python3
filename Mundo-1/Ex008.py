# Crie um algoritimo que receba um numéro em metro e faça as conversões
metro = float(input('Digite uma distância em metros: '))
print(f'A medida de {metro}m corresponde a')
print(f'{metro/1000}km \n{metro/100}hm \n{metro/10}dam \n{metro*10}dm \n{metro*100}cm \n{metro*1000}mm')