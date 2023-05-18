#Leia um número e imprima se ele é par ou impar.
num = int(input('Digite um número inteiro: '))

if (num % 2 == 0):
    print('O número {0} é par.'.format(num))
else:
    print('O número {0} é ímpar.'.format(num))