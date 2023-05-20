# Faça um algoritmo para determinar o maior e o menor de quatro números lidos
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
num4 = int(input('Digite outro número: '))

maior = max(num1, num2, num3, num4)
menor = min(num1, num2, num3, num4)

print('O maior número é {0} e o menor número é {1}'.format(maior, menor))