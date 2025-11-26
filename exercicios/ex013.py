salario = float(input('digite seu salario:'))
aumento = salario +(salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com o aumento ,passa a receber R${:.2f}'.format(salario, aumento))