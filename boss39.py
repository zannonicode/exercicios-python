ano = int(input('Digite seu ano de nascimento: '))
idade = 2025 - ano
if idade < 18:
    print ('Você ainda vai ter que se alistar ao exército')
elif idade == 18:
    print ('Está na hora de se alistar!')
else:
    print ('Já passou a hora de se alistar!')