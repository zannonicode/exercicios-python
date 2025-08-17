# calcule viagem mais de 200km so 0.45 cents por km, se nao 0.50
kms = float(input("Você ira viajar quantos km's: "))
if kms >= 200:
    paga = kms * 0.45
    print('a sua viagem custará R${:.2f}.'.format(paga))
else:
    paga = kms * 0.50
    print('a sua viagem custará R${:.2f}.'.format(paga))