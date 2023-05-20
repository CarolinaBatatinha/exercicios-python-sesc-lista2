# Os salários dos empregados de uma empresa sofreram um aumento. Técnicos tiveram um aumento de 50%, gerentes de 30% e os demais de 10%. Faça um programa que calcule o salário reajustado para cada profissão.

cargo = input('Qual o cargo a ser consultado? [1 - TÉCNICO/ 2 - GERENTE / 3 - OUTROS]: ')

if cargo == "1":
    salario = float(input('Digite o valor do último salário recebido em R$: '))
    salarioReajustado = salario * 1.5
    print('O salário do TÉCNICO era de R$ {0:.2f} e passará a ser de R$ {1:.2f}.'.format(salario, salarioReajustado))
else:
    if cargo == "2":
        salario = float(input('Digite o valor do último salário recebido em R$: '))
        salarioReajustado = salario * 1.3
        print('O salário do GERENTE era de R$ {0:.2f} e passará a ser de R$ {1:.2f}.'.format(salario, salarioReajustado))
    else:
        salario = float(input('Digite o valor do último salário recebido em R$: '))
        salarioReajustado = salario * 1.1
        print('O salário dos demais contribuidores era de R$ {0:.2f} e passará a ser de R$ {1:.2f}.'.format(salario, salarioReajustado))
