# Dado três números digitados pelo usuário, e todos diferentes, imprima o maior número.

num1 = int(input('Digite um primeiro número inteiro: '))
num2 = int(input('Digite um segundo número diferente do primeiro número: ')) 
num3 = int(input('Digite um terceiro número diferente do primeiro e do segundo número: '))

if num1 > num2 and num1 > num3:
    print('{0} é o maior número.'.format(num1))
else:
    if num2 > num1 and num2 > num3:
        print('{0} é o maior número.'.format(num2))
    else:
        print('{0} é o maior número.'.format(num3))

