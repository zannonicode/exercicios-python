#tem silva no nome?
name = input('Digite seu nome: ').lower()
s = 'silva' in name
count = name.count('silva')
print ('Você tem "Silva" no nome? {}'.format(s))
print ('quantos "Silva" você tem no nome? {}'.format(count))