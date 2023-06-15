maiores_idade = 0

for i in range(1, 7):
  idade = int(input("Digite a idade da pessoa " + str(i) + ": "))
  if idade >= 18:
    maiores_idade += 1

print("Das 6 pessoas, " + str(maiores_idade) + " são maiores de idade.")
