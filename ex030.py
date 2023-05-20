# # O Palmeiras deseja aumentar o salário de seus jogadores e comissão técnica para motivá-los na tentativa de subir para a primeira divisão. O ajuste salarial deve obedecer à seguinte tabela:
# Categoria                           Salário Atual                       Ação
# Equipe técnica                          -                            Aumento de 15%
# Jogadores                           0 a R$ 9.000,00                  Aumento de 20%
#                                     9.001,00 a 13.000                Aumento de 10%
#                                     13.001 a 18.000                  Aumento de 5%
#                                     acima de 18.000                  Sem aumento

# Preparar um algoritmo para ler o nome e o salário atual de cada jogador ou técnico e imprimir seu nome, salário atual e salário reajustado.

categoria = input('Digite sua categoria [1 - Equipe Técnica/ 2 - Jogador]: ')

if categoria == "1":
    salario = float(input('Digite o seu salário atual: '))
    salarioReajustado = salario * 1.15
    print('Atualmente seu salário é de R$ {0:.2f}, mas você passará a receber R$ {1:.2f}.'.format(salario, salarioReajustado))
else:
    salario = float(input('Digite o seu salário atual: '))
    if salario <= 9000:
        salarioReajustado = salario * 1.2
        print('Atualmente seu salário é de R$ {0:.2f}, mas você passará a receber R$ {1:.2f}.'.format(salario, salarioReajustado))
    else:
        if salario >= 9001 and salario <= 13000:
            salarioReajustado = salario * 1.1
            print('Atualmente seu salário é de R$ {0:.2f}, mas você passará a receber R$ {1:.2f}.'.format(salario, salarioReajustado))
        else:
            if salario > 13000 and salario <= 18000:
                salarioReajustado = salario * 1.05
                print('Atualmente seu salário é de R$ {0:.2f}, mas você passará a receber R$ {1:.2f}.'.format(salario, salarioReajustado))
            else:
                print('Seu salário não foi reajustado e você continuará a receber R$ {0:.2f}.'.format(salario))
                
