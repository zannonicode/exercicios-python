pn = float (input('Digite o valor do produto: '))
pag = int (input('[1] à vista (dinheiro ou cheque) \n[2] à vista (cartão) \n[3] até 2x (cartão) \n[4] 3x ou mais (cartão) \n \033[1;31mDigite a forma de pagamento:\033[m '))
if pag == 1:
    dezp = pn * 10 / 100
    total = pn - dezp
    print ('O valor total é de {:.2f}'.format(total))
elif pag == 2:
    cincop = pn * 5 / 100
    total = pn - cincop
    print ('O valor total é de {:.2f}'.format(total))
elif pag == 3:
    print ('O valor total é de {:.2f}'.format(pn))
elif pag == 4:
    mes = int (input('Digite em quantos meses ira pagar ( 3 ou MAIS): '))
    if mes < 3 :
        print ('Voce deve digitar a opção TRÊS se deseja menos de 3 meses')
    else:
        juros = pn * 20 / 100
        total = pn + juros
        print ('O pagamento total é de: {:.2f}'.format(total))
else:
    print ('Escolha uma opção valida (1,2,3 ou 4)')