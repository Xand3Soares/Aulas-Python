from math  import radians,sin,cos,tan
An = float(input('Digite um ângulo: '))
seno = sin(radians(An))
print('o angulo de {} tem o Seno de {:.2f}.'.format(An, seno))
cosseno = cos(radians(An))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(An, cosseno))
tangente = tan(radians(An))
print('O Angulo de {} de tem a TANGENTE de {:.2f}.'.format(An, tangente))