# 3 retas podem formar um triangulo?
r1 = float(input('digite a primeira reta: '))
r2 = float(input('digite a segunda reta: '))
r3 = float(input('digite a terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print ('As retas PODEM formar um triângulo!')
else:
    print ('As retas NÃO PODEM formar um triângulo!')