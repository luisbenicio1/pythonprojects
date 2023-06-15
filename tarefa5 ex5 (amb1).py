def classificar_participacao():
    respostas = []
    respostas.append(int(input("Telefonou para a vítima? (1-Sim ou 0-Não): ")))
    respostas.append(int(input("Esteve no local do crime? (1-Sim ou 0-Não): ")))
    respostas.append(int(input("Mora perto da vítima? (1-Sim ou 0-Não): ")))
    respostas.append(int(input("Devia para a vítima? (1-Sim ou 0-Não): ")))
    respostas.append(int(input("Já trabalhou com a vítima? (1-Sim ou 0-Não): ")))

    if sum(respostas) == 2:
        print("Suspeita")
    elif sum(respostas) in [3, 4]:
        print("Cúmplice")
    elif sum(respostas) == 5:
        print("Assassino")
    else:
        print("Inocente")

classificar_participacao()

