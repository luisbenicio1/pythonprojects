maiores_idade = 0
contador = 1

while contador <= 6:
    idade = int(input("Digite a idade da pessoa " + str(contador) + ": "))
    if idade >= 18:
        maiores_idade += 1
    contador += 1

print("Das 6 pessoas, " + str(maiores_idade) + " são maiores de idade.")
