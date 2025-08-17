#maior e menor número
n1 = int (input('digite um numero: '))
n2 = int (input('digite outro numero: '))
n3 = int (input('digite mais um numero: '))
if n1 >= n2 and n1 >= n3:
    print ('{} é o maior número'.format(n1))
elif n2 >= n1 and n2 >= n3:
    print ('{} é o maior numero'.format(n2))
else:
    print ('{} é o maior número'.format(n3))
if n1 <= n2 and n1 <= n3:
    print ('{} é o menor número'.format(n1))
elif n2 <= n1 and n2 <= n3:
    print ('{} é o menor numero'.format(n2))
else:
    print ('{} é o menor número'.format(n3))
