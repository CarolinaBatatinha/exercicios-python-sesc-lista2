# Faça um algoritmo para ler três números e ordene-os em ordem decrescente.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

numeros = [num1, num2, num3]
ordemDecrescente = sorted(numeros, reverse=True)

print('Os números em ordem decrescente são {}.'.format(ordemDecrescente))