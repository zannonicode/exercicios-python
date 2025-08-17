#contar quantos A e ver onde tem o primeiro e o ultimo
f = str (input('digite algo: '))
count = f.count('a')
find = f.find('a') +1
rfind = f.rfind('a') +1
print ("Sua frase tem {} A's".format(count))
print ('o primeiro "A" aparece na {} posição'.format(find))
print ('e o ultimo "A" aparece na {} posição'.format(rfind))