print("1: À vista em dinheiro ou cheque, recebe 10% de desconto")
print("2: À vista no cartão de crédito, recebe 5% de desconto")
print("3: Em 2 vezes, preço normal de venda sem juros")
print("4: Em 3 vezes, preço normal de venda mais juros de 10%")

valor = float(input("Digite o valor do produto:"))
escolha = float(input("Digite qual opção você deseja:"))

if (escolha <= 4):

  if (escolha == 1):
    valor_descontado = valor * 0.1
    valor_final = valor * 0.9
    print("Total a pagar é de:   R$", valor_final)

  if (escolha == 2):
    valor_descontado = valor * 0.05
    valor_final = valor * 0.95
    print("Total a pagar é de: R$", valor_final, "// Com juros de 5%")

  if (escolha == 3):
    valor_divido = valor / 2
    print("Duas parcelas de:", valor_divido, "No total:", valor)

  if (escolha == 4):
    valor_juros = valor * 0.1
    valor_final = valor + valor_juros
    valor_divido = valor_final / 3
    print("Tres parcelas de: R$", valor_divido,
          "// No total com juros de 10%:", valor_final)

else:
  print("Opção Invalida!")
input()
