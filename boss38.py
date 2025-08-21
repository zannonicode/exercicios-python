#comparar se é menor maior ou igual
n1 = float (input ('Digite um número: '))
n2 = float (input('Digite outro número: '))
if n1 > n2:
    print ('O número {} é o maior!'.format(n1))
elif n1 < n2:
    print ('O número {} é o maior!'.format(n2))
elif n1 == n2:
    print ('Os dois números sao iguais!')