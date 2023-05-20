# Um comerciante está necessitando saber qual é o lucro de cada mercadoria vendida em sua loja. Para isso, está necessitando de um programa que permite informar o valor de custo e de venda de um produto, e imprima uma mensagem considerando a tabela a seguir:
# Lucro                     Mensagens
# Inferior a 10%          “Baixo Lucro”
# Entre 10% e 20%         “Lucro Médio”
# Acima de 20%            “Lucro Alto”

valorCusto = float(input('Qual o valor de custo do produto?: '))
valorVenda = float(input('Qual o valor de venda do produto?: '))

lucro = ((valorVenda - valorCusto) / valorCusto) * 100

if lucro < 10:
    print('Baixo lucro')
else:
    if lucro >= 10 and lucro <=20:
        print('Lucro médio')
    else:
        print('Lucro alto')