
#Exercicio_040 - Crie um programa que leia duas notas de um aluno e cálcule sua média,
# mostrando uma mensagem no final de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.0: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {media}')
if media < 5:
    print('O aluno está REPROVADO.')
elif media >=5 and media <7:
    print('O aluno está em RECUPERAÇÃO')
elif media >= 7:
    print('O aluno está APROVADO.')