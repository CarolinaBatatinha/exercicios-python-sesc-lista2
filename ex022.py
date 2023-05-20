# Faça um algoritmo para ler três números e ordene-os em ordem crescente.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

numeros = [num1, num2, num3]
ordemCrescente = sorted(numeros)

print('Os números em ordem crescente são {}.'.format(ordemCrescente))

