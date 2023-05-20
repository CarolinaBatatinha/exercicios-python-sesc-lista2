# Dado três números digitados pelo usuário, e todos diferentes, imprima o número central.

num1 = int(input('Digite um primeiro número inteiro: '))
num2 = int(input('Digite um segundo número diferente do primeiro número: ')) 
num3 = int(input('Digite um terceiro número diferente do primeiro e do segundo número: '))

if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
    print('O número central é {0}.'.format(num1))
else:
    if num2 < num1 and num2 > num3 or num2 > num1 and num2 < num3:
        print('O número central é {0}.'.format(num2))
    else:
        print('O número central é {0}.'.format(num3))