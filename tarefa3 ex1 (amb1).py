print("Responda com 'Sim' ou 'Não' para as seguintes perguntas:")

mamifero = input("O animal é um mamífero? ")
if mamifero.lower() == "sim":
    quadrupede = input("O animal é quadrúpede? ")
    if quadrupede.lower() == "sim":
        carnívoro = input("O animal é carnívoro? ")
        if carnívoro.lower() == "não":
            herbívoro = input("O animal é herbívoro? ")
            if herbívoro.lower() == "sim":
                print("O animal escolhido foi o cavalo.")
        else:
            print("Não foi possível identificar o animal escolhido.")
    else:
        print("Não foi possível identificar o animal escolhido.")
else:
    voa = input("O animal é capaz de voar? ")
    if voa.lower() == "sim":
        penas = input("O animal possui penas? ")
        if penas.lower() == "sim":
            print("O animal escolhido foi o pinguim.")
        else:
            print("O animal escolhido foi a águia.")
    else:
        aquatico = input("O animal é aquático? ")
        if aquatico.lower() == "sim":
            mamifero = input("O animal é um mamífero? ")
            if mamifero.lower() == "sim":
                print("O animal escolhido foi a baleia.")
            else:
                print("O animal escolhido foi o crocodilo.")
        else:
            patas = input("O animal possui patas? ")
            if patas.lower() == "sim":
                casco = input("O animal possui casco? ")
                if casco.lower() == "sim":
                    print("O animal escolhido foi a tartaruga.")
                else:
                    print("O animal escolhido foi o homem.")
            else:
                voa = input("O animal é capaz de voar? ")
                if voa.lower() == "sim":
                    penas = input("O animal possui penas? ")
                    if penas.lower() == "sim":
                        print("O animal escolhido foi o pato.")
                    else:
                        print("O animal escolhido foi o morcego.")
                else:
                    print("O animal escolhido foi o macaco.")
input()