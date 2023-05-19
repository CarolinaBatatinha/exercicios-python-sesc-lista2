# Faça um algoritmo para calcular o valor da conta de água, considerando a seguinte tabela de gastos:
#m³                           #Cada m³
#0 – 10                       #R$ 1,20
#11 – 20                      #R$ 1,50
#Acima de 20                  #R$ 2,00

consumoAgua = float(input('Informe o consumo de água em m³: '))

if consumoAgua >= 0 and consumoAgua <=10:
    print('Valor da conta: R$ {0:.2f}'.format(consumoAgua * 1.2))
else:
    if consumoAgua >= 11 and consumoAgua <= 20:
        print('Valor da conta: R$ {0:.2f}'.format(consumoAgua * 1.5))
    else:
        print('Valor da conta: R$ {0:.2f}'.format(consumoAgua * 2))
