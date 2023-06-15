valor_dolar = float(input("Qual o valor do dolar atual?\n"))
quantia = float(input("Qual sua quantia em dolares?\n"))

conversao = quantia * valor_dolar
conversao = round(conversao, 2)

print("Sua quantia em real é de R$", conversao)
input()