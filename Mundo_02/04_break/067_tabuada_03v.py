
#Exercicio_067 - Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-'*35)
    for i in range (1,11):
        print(f'{num} x {i} = {num*i}')
    print('-'*35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')