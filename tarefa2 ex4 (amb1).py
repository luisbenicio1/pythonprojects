import math

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação desejada:\n")
print("1: Para adição")
print("2: Para subtração")
print("3: Para multiplicação")
print("4: Para divisão")
print("5: Para raiz quadrada")
print("6: Para potência\n")

op = input("Operação escolhida: ")

if (op == "1"):
  resultado = num1 + num2
  print(f"{num1} + {num2} = {resultado}")

if (op == "2"):
  resultado = num1 - num2
  print(f"{num1} - {num2} = {resultado}")

if (op == "3"):
  resultado = num1 * num2
  print(f"{num1} * {num2} = {resultado}")

if (op == "4"):
  resultado = num1 / num2
  print(f"{num1} / {num2} = {resultado}")

if (op == "5"):
  if (num1 <= 0):
    print("Numero invalido")
  else:
    resultado = math.sqrt(num1)
    print(f"A raíz quadrada de {num1} é {resultado}")

if (op == "6"):
  resultado = num1**num2
  print(f"{num1} elevado a {num2} é {resultado}")

else:
  print("Operação invalida")
input()