salario_bruto = float(input("Digite seu salario bruto:\n"))
prestacao = float(input("Digite o valor da prestaçao:\n"))

if (prestacao > (salario_bruto / 100) * 30):
  print("Prestacao Indisponivel")

if (prestacao <= (salario_bruto / 100) * 30):
  print("Prestacao Disponivel")
  input()
