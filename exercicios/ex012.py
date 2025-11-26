preco = float(input('Qual é o preço do produto? R$'))
cinco = preco - (preco * 5 / 100 )
quinze = preco + (preco * 15 / 100)
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f} e com 15% de desconto vai custar R${} reais'.format(preco, cinco, quinze))


