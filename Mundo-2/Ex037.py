# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 binário, -2 octal, -3 hexadecimal

print('Conversor de números')
num = int(input('\nInsira um número: '))
print('[ 1 ] - Binário \n[ 2 ] - Octal \n[ 3 ] - Hexadecimal')
tipo = input('Para qual modelo você deseja converter o número? ')

if tipo == '1':
    print(f'{num} convertido para binário é: {bin(num)[2:]}')
elif tipo == '2':
    print(f'{num} convertido para octal é: {oct(num)[2:]}')
elif tipo == '3':
    print(f'{num} convertido para hexadecimal é: {hex(num[2:])}')
else:
    print('Tipo inváildo, insira o número ao lado do tipo que deseja converter')
