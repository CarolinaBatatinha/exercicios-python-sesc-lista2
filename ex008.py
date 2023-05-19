# Leia um número e imprima se ele é positivo, negativo ou nulo.
num = int(input('Digite um número: '))

if num > 0:
    print('{0} é positivo.'.format(num))
elif num < 0:
    print('{0} é negativo'.format(num))
else:
    print("{0} é nulo.".format(num))