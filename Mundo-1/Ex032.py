# leia um programa que diga se o ano informado é bissexto
ano = int(input('Informe um ano para verificar se ele é bissexto? '))
if ano % 4 == 0 and ano % 100 or ano % 400 ==0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
