
#Exercicio_038 - Escreva um programa que leia dois números e inteiros e compare-os,
# mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O PRIMEIRO número é maior.')
elif num2 > num1:
    print('O SEGUNDO número é maior.')
else:
    print('Não existe número maior, os dois são IGUAIS.')