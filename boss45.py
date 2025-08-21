from random import randint
print ('Vamos jogar JOKENPO !')
jgd = int (input('\n[1]Pedra\n[2]Papel\n[3]Tesoura\n\033[32msua jogada: \033[m'))
aleatorio = randint(1,3)
if jgd == 1:
    if aleatorio == 1:
        print ('EMPATE!')
    if aleatorio == 2:
        print ('Você PERDEU!')
    if aleatorio == 3:
        print ('Você GANHOU!')
elif jgd == 2:
    if aleatorio == 1:
        print ('Você GANHOU!')
    if aleatorio == 2:
        print ('EMPATE!')
    if aleatorio == 3:
        print ('Você PERDEU!')
elif jgd == 3:
    if aleatorio == 1:
        print ('Você PERDEU!')
    if aleatorio == 2:
        print ('Você GANHOU!')
    if aleatorio == 3:
        print ('EMPATE!')
else:
    print ('DIGITE UM NÚMERO ENTRE 1 E 3')