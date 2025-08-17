# aumento salarial 1250>10%  1250<15%
sal = float(input('Qual seu salário atual? '))
if sal >= 1250:
    dez = sal * 10 / 100
    novo = sal + dez
    print ('Seu novo salário é de:R${:.2f}'.format(novo))
else:
    quinze = sal * 15 / 100
    novo = sal + quinze
    print ('Seu novo salário é de:R${:.2f}'.format(novo))