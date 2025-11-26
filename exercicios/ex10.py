din = float (input('Quanto você tem na carteira agora: R$'))
dolar = din / 3.27
euro = din / 2.54
print('com R${:.2f} você pode comprar US${:.2f} e {:.2f} Euros'.format(din, dolar, euro))