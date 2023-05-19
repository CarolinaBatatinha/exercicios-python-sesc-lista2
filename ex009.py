# Faça um algoritmo para verificar se o ano é bissexto.


# ==========    O ANO BISSEXTO OCORRE A CADA 4 ANOS (EXCETO ANOS MÚLTIPLOS DE 100 QUE NÃO SÃO MÚLTIPLOS DE 400)     ==================

ano = int(input('Digite o ano a ser pesquisado: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {0} é bissexto.'.format(ano))
else:
    print('O ano {0} não é bissexto.'.format(ano))   