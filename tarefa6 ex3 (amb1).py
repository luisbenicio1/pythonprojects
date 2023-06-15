mensagem = input("Digite a mensagem a ser codificada: ")

mensagem_codificada = ""
for letra in mensagem:
    if letra in "AEIOUaeiou":
        mensagem_codificada += str("AEIOUaeiou".index(letra) + 2)
    else:
        mensagem_codificada += letra

print("Mensagem codificada:", mensagem_codificada)