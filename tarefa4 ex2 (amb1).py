total_entrevistados = 0
total_sim = 0
total_nao = 0
total_indiferente = 0
total_mulheres_sim = 0
total_homens_nao = 0

while True:
    sexo = input("Digite o sexo do entrevistado (M ou F), ou digite 'sair' para encerrar: ")
    if sexo.lower() == 'sair':
        break
        
    idade = int(input("Digite a idade do entrevistado: "))
    resposta = input("Digite a resposta do entrevistado (S para sim, N para não, ou I para indiferente): ")

    if resposta.upper() == 'S':
        total_sim += 1
        if sexo.upper() == 'F':
            total_mulheres_sim += 1
    elif resposta.upper() == 'N':
        total_nao += 1
        if sexo.upper() == 'M':
            total_homens_nao += 1
    else:
        total_indiferente += 1
    
    total_entrevistados += 1

if total_entrevistados == 0:
    print("Nenhuma entrevista realizada.")
else:
    percentual_nao = (total_nao / total_entrevistados) * 100

    print(f"Foram entrevistadas {total_entrevistados} pessoas.")
    print(f"{total_sim} pessoas disseram sim e {total_nao} pessoas disseram não.")
    print(f"O percentual de pessoas que disseram não é de {percentual_nao:.2f}%.")
    print(f"{total_mulheres_sim} mulheres disseram sim e {total_homens_nao} homens disseram não.")
