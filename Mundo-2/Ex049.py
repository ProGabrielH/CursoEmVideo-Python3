# refaça o desafio 009, mostrando a tabuada de um número que o usuário esclher, só que agora utilizando um laço for

n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 15)
for i in range(1,11):
    print(f'{n} x {i} = {n * i}')
print('-' * 15)