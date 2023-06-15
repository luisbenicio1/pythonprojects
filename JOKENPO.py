from random import randint

maquina = randint(1,3)
print("Vamos jogar jokenpo!\n")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura\n")
resultado = int(input("Digite sua jogada: "))

if(maquina == 1) and (resultado == 1):
  print("Empate!")
  print("A jogada da maquina foi: ", maquina)
elif(resultado == 1 and maquina == 2):
    print("Maquina wins!")
    print("A jogada da maquina foi: ", maquina)
elif(resultado == 1 and maquina == 3):
    print("Voce venceu!")
    print("A jogada da maquina foi: ", maquina)

if(maquina == 2) and (resultado == 2):
  print("Empate!")
  print("A jogada da maquina foi: ", maquina)
elif(resultado == 2 and maquina == 3):
    print("Maquina wins!")
    print("A jogada da maquina foi: ", maquina)
elif(resultado == 2 and maquina == 1):
    print("Voce venceu!")
    print("A jogada da maquina foi: ", maquina)

if(maquina == 3) and (resultado == 3):
  print("Empate!")
  print("A jogada da maquina foi: ", maquina)
elif(resultado == 3 and maquina == 1):
    print("Maquina wins!")
    print("A jogada da maquina foi: ", maquina)
elif(resultado == 3 and maquina == 2):
    print("Voce venceu!")
    print("A jogada da maquina foi: ", maquina)

  
  
