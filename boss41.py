ano = int (input ('Digite seu ano de nascimento: '))
idade = 2025 - ano
if idade <= 9:
    print ('Você é da categoria MIRIM')
elif idade <=14 and idade >= 10:
    print ('Você é da categoria INFANTIL')
elif idade <= 19 and idade >= 15:
    print ('Você e´da categoria JUNIOR')
elif idade == 20:
    print ('Você é da categoria SENIOR')
else:
    print ('Você é da categoria MASTER')