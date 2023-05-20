# Faça um programa para ler 3 números reais e imprimi-los em ordem crescente. Se os números forem iguais, o cálculo o programa não deve ordená-los.

num1 = float(input('Digite um número real: '))
num2 = float(input('Digite outro número real: '))
num3 = float(input('Digite outro número real: '))

numeros  = [num1, num2, num3]
ordemCrescente = sorted(numeros)

if num1 == num2 and num1 == num3:
    print('Os números são iguais.')
else:
    print('Os números em ordem crescente são {}.'.format(ordemCrescente))
