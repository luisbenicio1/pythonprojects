preco = float(input("Qual o preco do produto?\n"))
desconto = float(input("Qual o valor do desconto?\n"))

valor_desconto = (preco * desconto) / 100
valor_final = preco - valor_desconto

print("Desconto de", desconto, "%", "Em um produto de R$", preco)
print("O valor a pagar é:", valor_final)
print("O valor do desconto é:", valor_desconto)
input()
