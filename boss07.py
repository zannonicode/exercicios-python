n1 = float (input ('qual sua primeira nota?'))
n2 = float (input ('qual sua segunda nota?'))
m = (n1 + n2)/2
f = 18 - (n1 + n2)
print ('a sua média é {:.1f} '.format(m))
print ('e voce precisa tirar {:.1f} para passar de ano'.format(f))