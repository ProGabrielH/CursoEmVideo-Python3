# Crie um programa donde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com parênteses abertos e fechados na ordem correta

exp = input('Digite uma expressão para verificar se faltam parênteses: ')

ap = exp.count('(')
fp = exp.count(')')

if ap == fp:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')
