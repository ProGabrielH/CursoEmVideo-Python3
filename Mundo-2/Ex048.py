# Faça um programa que calcule a soma entre todos os números ímpares que múltiplos de 3 e que se encontram entre o
# intervalo 1 e 500
s = 0

for i in range(1,500):
    if i%2 != 0 and i%3 == 0:
        s += i

print(s)