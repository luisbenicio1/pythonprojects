import random

temas = {
    'animais': ['cachorro', 'gato', 'elefante', 'leão', 'tigre'],
    'objetos': ['cadeira', 'mesa', 'computador', 'televisão', 'carro'],
    'frutas': ['banana', 'laranja', 'maçã', 'uva', 'manga'],
    'profissão': ['médico', 'engenheiro', 'professor', 'advogado', 'piloto'],
    'carros': ['fusca', 'mustang', 'civic', 'hb20', 'corolla']
}

boneco = [
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          | 
    =========''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          | 
    =========''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         | 
    =========''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    ========='''
]

def selecionar_palavra(tema):
    palavras = temas.get(tema)
    if palavras:
        return random.choice(palavras)
    else:
        print("Tema inválido.")
        return None

def jogo_da_forca():
    tema = input("Escolha o tema (animais, objetos, frutas, profissão, carros): ")
    palavra = selecionar_palavra(tema)

    if not palavra:
        return

    palavra = palavra.lower()  
  
    letras_corretas = []
    letras_erradas = []
    tentativas = 6
    pontos = 0

    while True:

        print(boneco[tentativas])

        for letra in palavra:
            if letra in letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print()

        print("Letras erradas:", ' '.join(letras_erradas))

        letra = input("Digite uma letra: ")
        letra = letra.lower()  

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já digitou essa letra. Tente novamente.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)

            if all(letra in letras_corretas for letra in palavra):
                pontos += 1
                print("Parabéns! Você ganhou! Pontuação atual:", pontos)
                break
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra incorreta. Você tem", tentativas, "tentativas restantes.")

            if tentativas == 0:
                print("Você perdeu! A palavra era:", palavra)
                break

    return pontos

def exibir_pontuacao(pontos):
    print("Pontuação final:", pontos)

pontuacao_total = 0

while True:
    pontuacao_rodada = jogo_da_forca()
    pontuacao_total += pontuacao_rodada

    continuar = input("Deseja jogar novamente? (s/n): ")
    if continuar.lower() != 's':
        break

exibir_pontuacao(pontuacao_total)
