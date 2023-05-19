# Leia um número para verificar se ele é maior do que 20. Caso afirmativo imprima a metade desse número. Caso contrário imprima o seu quadrado.

num = int(input('Digite um número inteiro: '))

if num > 20:
    print('{0} / 2 = {1}'.format(num, (num/2)))

else:
    print('{0}² = {1}'.format(num, (num*num)))