dias =  int(input ('quantos dias o carro foi alugado? '))
kms = float (input ('quantos km voce andou com o carro? '))
pd = dias*60
pkm = kms*0.15
fin = pd + pkm
print ('o pagamento total é de:{:.2f}. {:.2f} do aluguel diário e {:.2f} de quilometros percorridos'.format(fin,pd,pkm))