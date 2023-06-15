lista = []

for i in range(5):
  numeros = float(input("Digite os numeros: "))
  lista.append(numeros)

min = min(lista)
max = max(lista)

print("Menor numero:", min, "Maior numero:", max)
