import random

def escolher_palavra():
    palavras = ['trabalho', 'datacenter', 'programacao', 'escolas']
    return random.choice(palavras)
def exibir_forca(tentativas):
    estagios = [
        '''
           -----
           |   |
               |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        '''
    ]
    print(estagios[tentativas])
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta:")
    print(' '.join(palavra_oculta))

    while tentativas < 6:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        else:
            letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print(' '.join(palavra_oculta))
        else:
            tentativas += 1
            print(f"A letra '{letra}' não está na palavra.")
            exibir_forca(tentativas)

        if '_' not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra!")
            break

    if '_' in palavra_oculta:
        print(f"Você perdeu! A palavra era '{palavra}'. Tente novamente.")

    print("Obrigado por jogar!")

# Chamada da função principal para iniciar o jogo
jogar()
