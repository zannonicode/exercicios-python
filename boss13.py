sal = float (input('qual o salario do funcionario? '))
amais = sal*15/100
novo = sal + amais
print ('um funcionario que recebe {:.2f} de salario passara a receber {:.2f} com 15% de aumento'.format(sal,novo))