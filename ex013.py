# Faça um algoritmo para calcular o valor da conta de energia elétrica de uma casa, considerando a tabela a seguir. A conta deve ser calculada proporcionalmente, ou seja, se o usuário gastou 55 KHW, ele pagará 50 KWH ao preço de R$ 1,00 e 5 ao preço de R$ 1,30.
# KWH              Valor
# 0 – 50          R$ 1,00
# 51 – 100        R$ 1,30
# 101 - 150       R$ 1,60
# Acima de 150    R$ 2.00

consumoEnergia = float(input('Informe o consumo de energia: '))

if consumoEnergia <= 50:
    valor = consumoEnergia * 1.00
    print('Valor da conta: R$ {:.2f}'.format(valor))
else:
    if consumoEnergia >= 51 and consumoEnergia <= 100:
        valor = ((consumoEnergia - 50)* 1.3)  + (50 * 1)
        print('Valor da conta: R$ {:.2f}'.format(valor))
    else:
        if consumoEnergia >= 101 and consumoEnergia <= 150:
            valor = ((consumoEnergia - 100)* 1.6) + (50 * 1.3) + (50 * 1)
            print('Valor da conta: R$ {:.2f}'.format(valor))
        else:
            valor = ((consumoEnergia - 150) * 2) + 50 * 1.6 + (50 * 1.3) + (50 * 1)
            print('Valor da conta: R$ {:.2f}'.format(valor))