# Leia um número e, se ele for positivo, imprima seu inverso; caso contrário imprima seu quadrado Inverso. Inverso: 1/número.

num = int(input('Digite um número inteiro: '))

if (num>=0):
    print('Inverso = 1/{0}'.format(num))
else:
    print('Quadrado inverso = 1/({0})²'.format(num))