#aprovar emprestimo, nao pode passar de 30% do salario
casa = float (input ('Qual o valor da casa? '))
sal = float (input ('Qual seu salário? '))
tempo = float (input ('em quantos anos deseja pagar a casa?(pode digitar os meses tambem exemplo: 1.7) '))
meses = tempo * 12
emprestimo = casa / meses
mensal = sal * 0.3
if mensal < emprestimo:
    print ('A sua prestação foi NEGADA!')
else:
    print ('A sua prestação foi APROVADA!')