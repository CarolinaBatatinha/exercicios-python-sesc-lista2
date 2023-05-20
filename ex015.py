# Desenvolva um algoritmo para calcular quantos reais serão necessários para encher o tanque de um veiculo para se realizar uma viagem. O usuário deverá informar o tipo de combustível do veículo, o número total de km a ser percorrido e o consumo médio do veículo. A tabela de preços dos combustíveis utilizada no cálculo é apresentada abaixo:
# Combustível         Preço
# Gasolina            22.25
# Álcool              11.5
# Diesel              11.65

tanque = int(input('Qual a capacidade do tanque de combustível do veículo em litros?: '))
tipoCombustivel = input('Qual o tipo de combustível do veículo?: ').lower()
percurso = float(input('Qual a distância total a ser percorrida em km?: '))
consumoMedio = float(input('Qual o consumo médio do veículo?: '))

if tipoCombustivel == "gasolina":
    gasolina = tanque * 22.25
    print('Seu veículo usa {0} e seu tanque comporta {1} litros de combustível.'.format(tipoCombustivel, tanque))
    print('Sua viagem percorrerá {0}km e o consumo médio do seu carro é de {1} km/L.'.format(percurso, consumoMedio))
    print('Será necessário pagar R$ {0:.2f} para encher o tanque do seu veículo.'.format(gasolina))
else:
    if tipoCombustivel == "alcool":
        alcool = tanque * 11.5
        print('Seu veículo usa {0} e seu tanque comporta {1} litros de combustível.'.format(tipoCombustivel, tanque))
        print('Sua viagem percorrerá {0}km e o consumo médio do seu carro é de {1} km/L.'.format(percurso, consumoMedio))
        print('Será necessário pagar R$ {0:.2f} para encher o tanque do seu veículo.'.format(alcool))
    else:
        diesel = tanque * 11.65
        print('Seu veículo usa {0} e seu tanque comporta {1} litros de combustível.'.format(tipoCombustivel, tanque))
        print('Sua viagem percorrerá {0}km e o consumo médio do seu carro é de {1} km/L.'.format(percurso, consumoMedio))
        print('Será necessário pagar R$ {0:.2f} para encher o tanque do seu veículo.'.format(diesel))



