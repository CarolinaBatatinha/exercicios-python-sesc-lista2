# Uma empresa de modelo está contratando garotas para iniciar um trabalho de divulgação de produtos de beleza. Para isso, está selecionando garotas que tenham o seguinte perfil:

# a. Idade superior a 18 anos
# b. Cabelos Loiros
# c. Altura superior a 1,75 m
# d. Peso inferior a 60 kg
# e. Seios: 85 a 87 cm
# f. Cintura: 60 cm
# g. Olhos verdes
# h. Quadril = 60 cm

# Você foi escalado por sua empresa para elaborar um algoritmo que permite entrar com os
# valores referentes às características acima e, informar se a garota foi selecionada ou não.

idade = int(input('Digite sua idade: '))
cabeloLoiro = input('Você é loira? (S/N): ').lower()
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))
busto = float(input('Digite a medida do seu busto em cm: '))
cintura = float(input('Digite a medida da sua cintura em cm: '))
olhosVerdes = input('Seus olhos são verdes? (S/N): ').lower()
quadril = float(input('Digite a medida do seu quadril em cm: '))

selecionada = idade > 18 and cabeloLoiro == "s" and altura > 1.75 and peso < 60 and 85 <= busto <= 87 and cintura == 60 and olhosVerdes == "s" and quadril == 60

if selecionada:
    print('Parabéns, você foi selecionada!')
else:
    print('Você não atende aos requisitos.')
