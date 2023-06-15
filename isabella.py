import math

num = float(input("Digite um número real não negativo: "))

if num < 0:
  exit()

if num != 5:
  raiz = math.sqrt(num)
  print(f"A raiz quadrada de {num} é {raiz}.")

if num == 5:
  raiz = math.pow(num, 1 / 3)
  print(f"A raiz cúbica de {num} é {raiz}.")

input()