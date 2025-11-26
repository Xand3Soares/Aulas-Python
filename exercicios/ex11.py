larg = float (input('digite a largura da parede:'))
altura = float (input('digite a altura da parede:'))
área = altura * larg
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, altura, área))
tinta = área / 2
print('Para pintar a sua parede, você precisa de {}l de tinta.'.format(tinta))