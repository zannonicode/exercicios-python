#advinhar numero
from random import randint
num = randint(1, 5)
chute = int (input ('Qual seu palpite? '))
if chute == num:
    print ('Parabéns, você acertou.')
else:
    print ('Você errou, o número era: {}.'.format(num))
print ('Foi 1 bom jogo!')