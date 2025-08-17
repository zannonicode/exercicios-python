from random import shuffle
n1 = str (input('nome do primeiro aluno: '))
n2 = str (input('nome do segundo aluno: '))
n3 = str (input('nome do terceiro aluno: '))
n4 = str (input('nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print ('a ordem de alunos são: {}'.format(lista))
