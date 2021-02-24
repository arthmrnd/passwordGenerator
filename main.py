import random
from string import digits, punctuation, ascii_letters

exi = 1
while (exi == 1):
    print('Gerador de palavras chaves \n')
    tam = int(input('Qual tamanho da senha desejada?\n'))

    symbols = ascii_letters + digits + punctuation
    secure_random = random.SystemRandom()
    senha = "".join(secure_random.choice(symbols) for i in range(tam))

    print('Senha gerada - ' + senha)
    print('\nCaso deseje uma outra senha digite 1\nCaso contrario digite 0\n')
    exi = int(input())

print('Obrigado por usar este software')
