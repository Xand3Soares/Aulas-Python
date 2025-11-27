import math
co = float (input('Digite o comprimento do cateto oposto:  '))
ca = float (input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print('O comprimento da Hipotenusa é {:.2f}'.format(hipotenusa))