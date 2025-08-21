n = int (input ('Digite um número inteiro: '))
choice = int (input('Você quer converter {} para:\n[1]BINÁRIO\n[2]OCTAL\n[3]HEXADECIMAL\nSUA ESCOLHA: '.format(n)))
if choice == 1:
    print ('O número BINÁRIO de {} é: '.format(n),bin(n)[2:])
elif choice == 2:
    print ('O número OCTAL de {} é: '.format(n),oct(n)[2:])
elif choice == 3:
    print ('O número HEXADECIMAL de {} é: '.format(n),hex(n)[2:])
else:
    print ('Escolha uma opção valida (1,2 ou 3)')