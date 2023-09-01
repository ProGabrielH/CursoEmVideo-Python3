# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = input('Qual o nome da sua cidade? ').lower()

if 'santo'in city:
    print('A sua cidade possui "Santo"')
elif 'santa'in city:
    print('A sua cidade possui "Santa"')
else:
    print('A sua cidade não possui "Santo" ou "Santa"')
