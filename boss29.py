#multa 7R$ acima de 80km
kms = int (input('Você estava andando a quantos km/h no seu autmovel? '))
if kms > 80:
    multa = (kms - 80)*7
    print ('O valor da sua multa foi: {}'.format(multa))
else:
    print ('Você nao estava acima do limite!')
print ('Boa viagem!')