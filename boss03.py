n1 = int(input('\033[4mdigite um numero:\033[m '))
n2 = int(input('\033[4mdigite outro numero:\033[m '))
v = n1 + n2
print ('a soma entre \033[34m{}\033[m e \033[31m{}\033[m resultou em \033[0;35;40m {} \033[m'.format(n1, n2, v))