#  Escreva um programa para calcular o reajuste salarial dos empregados de uma empresa, de acordo com os seguintes critérios:
# a. Os funcionários com salário inferior a 1.000,00 devem ter um reajuste de 55%;
# b. Funcionários com salário de 1.000,00 (inclusive) a 2.500,00 (inclusive) devem ter um reajuste de 33%;
# c. Os funcionários com salário superior a 2.500,00 devem ter um reajuste de 20%;

salarioAtual = float(input('Informe seu salário atualmente em reais (R$): '))

if salarioAtual < 1000:
    salarioReajustado = salarioAtual * 1.55
    print('Seu salário é de R$ {0:.2f} e, a partir do próximo mês, você ganhará R$ {1:.2f}.'.format(salarioAtual, salarioReajustado))
else:
    if salarioAtual >= 1000 and salarioAtual <= 2500:
        salarioReajustado = salarioAtual * 1.33
        print('Seu salário é de R$ {0:.2f} e, a partir do próximo mês, você ganhará R$ {1:.2f}.'.format(salarioAtual, salarioReajustado))

    else:
        salarioReajustado = salarioAtual * 1.2
        print('Seu salario atual é de R$ {0:2f} e, a partir do próximo mês, você ganhará R$ {1:.2f}.'.format(salarioAtual, salarioReajustado))