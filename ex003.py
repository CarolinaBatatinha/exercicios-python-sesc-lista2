# Repita o exercício anterior sabendo que os números são diferentes, qual é o maior e o menor dos números.

numA = int(input('Digite um número inteiro: '))
numB = int(input('Digite um outro número inteiro: '))

if (numA == numB):
    print('Os números são iguais.')
else:
    print('Os números são diferentes.')
    if (numA > numB):
        print('Maior = {0} \nMenor = {1}'.format(numA, numB))
    else:
        print('Maior = {1}\nMenor = {0}'.format(numA, numB))