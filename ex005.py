#Faça um algoritmo para imprimir a média e informar se o aluno foi aprovado ou reprovado e,qual a média obtida.
media = float(input('Digite sua média no semestre: '))
if (media >= 7):
    print('Você foi aprovado!')
    print('Média = {0}'.format(media))
else:
    print('Você foi reprovado.')
    print('Média = {0}'.format(media))