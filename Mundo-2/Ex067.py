# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo

print('=-'*30)
print(f'{"TABUADA":^50}')
print('=-'*30)

while True:
    num = int(input('Digite o número: [Negativo para cancelar] '))
    if num > 0:
        print('-' * 30)
        for i in range(1, 11):
            print(f'{num} X {i} = {num*i}')
        print('-' * 30)
    else:
        break
print('FINALIZANDO A TABUADA')