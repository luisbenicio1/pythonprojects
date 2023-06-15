gabarito = []
respostas = []

nome = (input("Digite seu nome: "))

for i in range(10):
  gab1 = str(input("Determine o gabarito com a/b/c/d/e: "))
  gabarito.append(gab1)

for i in range(10):
  resp1 = str(input("Digite as respostas com a/b/c/d/e: "))
  respostas.append(resp1)

def calcular_pontuacao(gabarito, respostas):
    pontuacao = 0
    for i in range(len(gabarito)):
        if gabarito[i] == respostas[i]:
            pontuacao += 1
    return pontuacao

pontuacao = calcular_pontuacao(gabarito,respostas)

print("Nome do aluno: ", nome)
print("Gabarito: ", gabarito)
print("Respostas: ", respostas)
print("Pontuação final: ", pontuacao)
