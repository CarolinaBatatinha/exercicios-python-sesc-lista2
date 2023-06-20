# Suponha que um caixa disponha apenas notas de 100, 10 e 1 Real. Considerando que alguém está pagando uma compra, faça um programa para determinar o número mínimo de notas que o caixa deve fornecer como troco. Imprima também o valor da compra, o valor do troco e a quantidade de cada tipo de nota a ser fornecido como troco. Suponha que o sistema monetário não utilize centavos.

valor_compra = int(input("Digite o valor da compra: "))
valor_pago = int(input("Digite o valor pago: "))
troco = valor_pago - valor_compra

notas_100 = troco // 100
troco %= 100

notas_10 = troco // 10
troco %= 10

notas_1 = troco

print("Valor da compra:", valor_compra)
print("Valor pago:", valor_pago)
print("Troco:", valor_pago - valor_compra)
print("Quantidade de notas de 100:", notas_100)
print("Quantidade de notas de 10:", notas_10)
print("Quantidade de notas de 1:", notas_1)