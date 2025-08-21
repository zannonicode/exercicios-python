alt = float(input('digite a altura em METROS: '))
peso = float(input('digite a peso em KG: '))
imc = peso / (alt * alt)
if imc < 18.5:
    print ('Você esta abaixo do peso!')
elif 18.5 <= imc < 25:
    print ('Você esta no peso ideal!')
elif 25 <= imc < 30:
    print ('Você esta acima do peso!')
elif 30 <= imc < 40:
    print ('Você tem obesidade!')
else:
    print ('Você tem obesidade mórbida!')