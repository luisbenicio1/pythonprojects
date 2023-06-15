lista = []
pares = []
impares = []

for i in range(8):

  numero = int(input("Digite um numero: "))
  lista.append(numero)
  
  if numero % 2 == 0:
     pares.append(numero)
  else:
     impares.append(numero)

print("Lista", lista)
print("Lista de pares", pares)
print("Lista de impares", impares)
