# Desenvolva um programa que lai o nome, idade e sexo de 4 pessoas. No final do programa mostre: A média de idade do
# grupo, Qual o nome do homem mais velho, Quantas mulheres tem menos de 20 anos.

idade_mulheres = []
idade_homens = []
idade_geral = []
for i in range(0,4):
    nome = input('\nQual o seu nome: ')
    sexo = input('Qual o seu sexo [F] [M]: ').upper().strip()
    idade = int(input('Qual sua idade:'))
    idade_geral.append(idade)
    if sexo == 'M':
        idade_homens.append(idade)
    elif idade < 20:
        idade_mulheres.append(idade)
idade_homens.sort()
print(f'O homem mais velho tem {idade_homens[-1]}anos \nExistem {len(idade_mulheres)} mulheres com menos de 20 anos')
print(f'A média de idade é {sum(idade_geral)/4}')
