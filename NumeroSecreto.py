def mostrar_rodape():
    print('______________________________________')
    print(' Bem-vindo ao game! Se divirta')
    print("______________________________________")

def dica_game():
    print('______________________________________')
    print(' A dica do game é: o número secreto está entre 0 e 100')
    print("______________________________________")

import random
num_min = 0
num_max = 100
num_secreto = random.randint(num_min, num_max)
mostrar_rodape()
dica_game()
tentativa = 7


for i in range(tentativa):
 palpite = int(input('Qual é o numero secreto? :'))
 if palpite == num_secreto:
    print('Parabéns, você acertou!!!')
    break
 elif palpite != num_secreto:
     tentativa -= 1
     if palpite > num_secreto:
         print('Seu palpite foi maior que o numero secreto')
         print(f'Você tem mais : {tentativa} tentativas')
     else:
         print('Seu palpite foi menor que o numero secreto')
         print(f'Você tem mais : {tentativa} tentativas')

print('-------------------------------------------')
print(f'O número secreto era : {num_secreto}')
print('-------------------------------------------')

def rodape_fim():
    print('_______________________________________')
    print('Fim do game!')
    print('________________________________________')
rodape_fim()
