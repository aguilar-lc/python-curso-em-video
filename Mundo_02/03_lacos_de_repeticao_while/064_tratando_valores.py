
#Exercicio_064 - Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.



num = 0
c = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    c = c + 1
    soma = soma + num
    num = int(input('Digite um número [999 para parar]: '))
print('FIM')