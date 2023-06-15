lista = []

for i in range(4):
  notas = float(input("Digite as notas: "))
  lista.append(notas)

somatotal = sum(lista)
media = somatotal / 4

if (media >= 7):
  print("Aprovado, nota final:", media)
else:
  print("Reprovado, nota final:", media)
