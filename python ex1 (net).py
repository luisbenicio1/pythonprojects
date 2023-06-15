nome = input("Digite seu nome: ")
while(len(nome) <= 3):
 nome = input("Nome invalido, digite novamente! ")

idade = int(input("Digite sua idade: "))
while(idade < 0 and idade > 150):
  idade = int(input("Idade invalida, digite uma idade valida! "))

salario = float(input("Digite seu salario: "))
while(salario < 0):
  salario = float(input("Salario invalido, digite um salario valido! "))

sexo = input("Digite seu sexo M: Masculino, F: Feminino, X: Prefiro não dizer: ")
while(sexo != "M" and sexo != "F" and sexo != "X"):
  sexo = input("Sexo invalido, digite um sexo valido! ")

estadocivil = input("Digite seu estado civil (S/C/V/D): ")
while(estadocivil != "S" and estadocivil != "C" and estadocivil != "V" and estadocivil != "D"):
  estadocivil = input("Estado civil invalido, digite um estado civil valido! ")

print("Cadastro Realizado com sucesso!")

print("Nome:", nome)
print("Idade:", idade)
print("Salario:", salario)
print("Sexo:", sexo)
print("Estado civil:", estadocivil)


  
