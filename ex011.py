# # Faça um algoritmo para calcular, considerando que o usuário informe a idade (inteira), as seguintes informações sobre o usuário:
# # a. Número de semestres;
# # b. Número de meses;
# # c. Número de semanas;
# # d. Número de dias;
# # e. Número de horas;
# # f. Número de minutos;
# # g. Número de segundos;
# No final deseja-se visualizar todos os cálculos realizados e também se o usuário é infantil, adolescente, jovem ou adulto. A tabela abaixo demonstra as idades que defini essas categorias: 
# Idade Categoria
# Até 12 Infantil
# 13 a 16 Adolescente
# 17 a 20 Jovem
# 21a 50 Adulto
# Acima de 50 Idoso

idade = int(input('Digite a sua idade: '))
semestres = idade // 6 
meses = idade * 12
semanas = idade * 52
dias = idade * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

if idade <= 12:
    categoria = "Infantil"
else:
    if 13 <= idade <= 16:
        categoria = "Adolescente"
    else:
        if 17 <= idade <= 20:
            categoria = "Jovem"
        else:
            if 21 <= idade <= 50:
                categoria = "Adulto"
            else:
                categoria = "Idoso"

print('Número de semestres: {0}'.format(semestres))
print('Número de meses: {0}'.format(meses))
print('Número de semanas: {0}'.format(semanas))
print('Número de dias: {0}'.format(dias))
print('Número de horas: {0}'.format(horas))
print('Número de minutos: {0}'.format(minutos))
print('Número de segundos: {0}'.format(segundos))
print('Categoria: {0}'.format(categoria))

