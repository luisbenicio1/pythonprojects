print("Insira 3 valores como A,B,C: ")
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if (a < b + c and b < a + c and c < a + b):
  if (a == b == c):
    print("Triangulo Equilatero")
  elif (a == b or a == c or b == c):
    print("Triangulo isósceles")
  else:
    print("Triangulo escaleno")

else:
  print("Não compoem um triangulo")
input()