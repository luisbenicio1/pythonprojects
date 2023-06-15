peso = float(input("Digite o seu peso em kg\n"))
altura = float(input("Digite o sua altura em metros\n"))

imc = peso / (altura * altura)

if (imc < 18.5):
  print("Abaixo do peso")

if (imc >= 18.5 and imc <= 25):
  print("Peso normal")

if (imc >= 25 and imc <= 30):
  print("Acima do peso")

if (imc > 30):
  print("Obeso")
input()
