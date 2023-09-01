# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite qualquer frase: ').strip()

print(f'A letra "A" aparece {frase.lower().count("a")+1} \nAparece pela primeira vez na {frase.lower().find("a")+1}ª posição'
      f'\nE pela ultima vez na {frase.lower().rfind("a")+1}ª posição')
print(len(frase))