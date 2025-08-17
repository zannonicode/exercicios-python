# falar 1 e ultimo nome
nome = str(input('Digite seu nome: ')).strip()
n1 = nome.split()[0]
un = nome.split()[-1]
print ('Prazer em conhecer você {} {}'.format(n1, un))