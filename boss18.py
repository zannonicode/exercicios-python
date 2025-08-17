import math
ang = float (input('Qual é o angulo? '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print ('com o angulo de {:.2f} graus teremos: \n o seno de {:.2f} graus \n o cosseno com {:.2f} graus \n e a tangente com {:.2f} graus. '.format(ang,sen,cos,tan))