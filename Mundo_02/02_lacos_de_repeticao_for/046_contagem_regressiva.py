
#Exercicio_046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro
# de fogos de artifício indo de 10 até 0, com uma pausa de 1 segundo entre elas.


from time import sleep
for i in range(10,-1, -1):
    print(i)
    sleep(0.5)
print('BUM! BUM! POOOW!')