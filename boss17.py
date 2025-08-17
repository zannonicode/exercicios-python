from math import hypot
co = float (input ('valor do caeteto oposto ?'))
ca = float (input ('valor do cateto adjacente'))
hypot = hypot(co, ca)
print ('o valor da hipotenusa é: {:.2f}'.format(hypot))