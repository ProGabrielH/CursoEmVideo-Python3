# Desenvolva uma lógica que leia peso e algura de uma pessoa, calcule seu imc e mostre seu status: >18.5: abaixo do peso
# entre 18.5 e 25: peso ideal. entre 25 e 30: sobrepeso. 30 a 40: obesidade. acima de 40: obesidade morbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = float(peso / (altura * altura))

print(f'\nSeu IMC é de: {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está acima do peso')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade')
elif imc >= 40:
    print('Você está com obesidade morbida')
