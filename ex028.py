# # Calcule a média aritmética de três valores A, B e C, escrevendo o valor e a mensagem apropriada:
# Média > 9 ► Aluno Excelente
# Média <= 9 e média > 8, ► Bom Aluno
# Média <= 8 e média > 7, ► Aluno Regular
# Média <= 7 e média > 6, ► Aluno Aprovado
# Média <= 6 e média > 5, ► Aluno de Exame
# Caso contrário, mostre a mensagem reprovado

notaA = float(input('Digite sua primeira nota: '))
notaB = float(input('Digite sua segunda nota: '))
notaC = float(input('Digite sua terceira nota: '))

media = (notaA + notaB + notaC)/3

if media > 9:
    print('===========================================')
    print('Aluno excelente\nMédia = {}'.format(media))
else: 
    if media <= 9 and media > 8:
        print('===========================================')
        print('Bom aluno\nMédia = {}'.format(media))
    else:
        if media <= 8 and media > 7:
            print('===========================================')
            print('Aluno regular\nMédia = {}'.format(media))
        else: 
            if media <= 7 and media >= 6:
                print('===========================================')
                print('Aluno aprovado\nMédia = {}'.format(media))
            else:
                if media < 6 and media >= 5:
                    print('===========================================')
                    print('Aluno em recuperação\nMédia = {}'.format(media))
                else:
                    print('===========================================')
                    print('Aluno reprovado\nMédia = {}'.format(media))