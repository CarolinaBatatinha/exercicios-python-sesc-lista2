# Elaborar um programa que calcule a média ponderada de um aluno da disciplina de Algoritmo. Esta média tem pesos: 4 para a primeira prova e 3 para a segunda prova. Após calculada a média, uma mensagem deve ser apresentada informando a situação do aluno: APROVADO COM MÉDIA ou NECESSITA FAZER SUBSTITUTIVA. Caso o aluno necessite fazer prova substitutiva, o programa deve pedir esta nota e calcular a nova média do aluno. Uma nova mensagem da situação deve informar ALUNO COM MÉDIA ou ALUNO REPROVADO. Obs: A prova substitutiva pode substituir a primeira prova ou a segunda prova, portanto o programa deve verificar quando o aluno fica com maior média, isto é, quando a primeira prova é substituída pela prova substitutiva ou quando a segunda prova é substituída pela prova substitutiva.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
peso1 = 4
peso2 = 3

mediaPonderada = ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)

if mediaPonderada >= 6:
    print('## Média ponderada: {0:.1f} ##\n## Aluno aprovado com média ##'.format(mediaPonderada))
else:
    print('## Média ponderada: {0:.1f} ##\n## Aluno necessita fazer prova substitutiva ##'.format(mediaPonderada))
    substitutiva = float(input('Digite sua nota na prova substitutiva: '))
    notas = [nota1, nota2, substitutiva]    
    maioresNotas = sorted(notas)
    mediaSubstitutiva = (maioresNotas[1] + maioresNotas[2])/ 2
    if mediaSubstitutiva >= 6:
        print('## Após a prova substitutiva, sua média foi de {0:.1f} ##\n## Você está aprovado ##'.format(mediaSubstitutiva))
    else:
        print('## A prova substitutiva, sua média foi de {0:.1f} ##.\n## Você reprovou ##'.format(mediaSubstitutiva))