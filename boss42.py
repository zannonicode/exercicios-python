r1 = float(input('digite a primeira reta: '))
r2 = float(input('digite a segunda reta: '))
r3 = float(input('digite a terceira reta: '))
if r1 == r2 and r1 == r3 and r2 == r3:
    print ('Pode formar um triângulo, e ele sera equilatero!')
elif r1 == r2 or r1 == r3 or r2 == r3 and r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print ('pode formar um triângulo, e ele sera isoceles')
elif r1 != r2 and r1 != r3 and r2 != r3 and r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print ('pode formar um triangulo, e ele sera escaleno')
else:
    print ('Não pode formar um triângulo')