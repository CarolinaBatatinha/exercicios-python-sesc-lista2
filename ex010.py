#Faça um algoritmo para calcular a conta de energia elétrica de uma casa. O valor de cada KWH é 1.5. Quando a casa é de uma aposentada, a conta tem um desconto de 15%.

perfilUsuario = str(input('O cliente é aposentado? (S/N): '))
energiaConsumida = float(input('Digite o consumo de energia de uma casa: '))
aPagar = float(energiaConsumida * 1.5)
perfilUsuario.upper()

if perfilUsuario == "S":
    print('O cliente é aposentado e pagará R$ {0:.2f} na fatura da conta de luz.'.format(aPagar - (aPagar * .15)))
else:
    print('O cliente não é aposentado e pagará R$ {0:.2f} na fatura da conta de luz.'.format(aPagar))
