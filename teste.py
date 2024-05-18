import random

pontosJ1 = 0
pontosJ2 = 0

def validarEscolha(esc):

    if(esc == 1 or esc == 3 or esc == 2):
        return True
    else:
        return False
        
def escMaquina():
    esc = random.randint(0,2)
    return esc

def ganhador(j1, j2):

    if((j1 == 3 and j2 == 2) or (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1)):
        return "Jogador Ganhou"
    elif(j1 == j2):
        return "Empate"
    else:
        return "Maquina Ganhou"
    


def inicio():
    global pontosJ1, pontosJ2
    while(True):
        j1 = int(input("Escolha: pedra - 1, papel - 2, tesoura - 3: "))
        j2 = escMaquina()
        esc_element = ["Pedra", "Papel", "Tesoura"]
        if(validarEscolha(j1)):
            print(f"Escolha do Jogador: {esc_element[j1-1]}\nEscolha da Maquina {esc_element[j2-1]}\n------------------")
            resul = ganhador(j1, j2)
            if(resul == "Jogador Ganhou"):
                pontosJ1 += 1
            elif(resul == "Maquina Ganhou"):
                pontosJ2 += 1
            else:
                print(f'Potos Jogador: {pontosJ1}\nPontos Maquina: {pontosJ2}')
                break
            print(f'Potos Jogador: {pontosJ1}\nPontos Maquina: {pontosJ2}')
            break
                    
        else:
            print("Escolha invalida!!")



def reenicio_or_fim():
    reenicio = input("Deseja Iniciar\n1 - sim\n0 - nao\n")
    return reenicio


while(True):
    inicio()
    reinicio = reenicio_or_fim()
    print(reinicio+"op 1")

    if(reinicio == "1"):
        continue
    elif(reinicio == "0"):
        print("Saindo .........")
        break
    else:
        reinicio = reenicio_or_fim()
        while(reinicio != "0" and reinicio != "1"):
            print("Escolha invalida!!")
            reinicio = reenicio_or_fim()
            print(reinicio+" op 2 ")

        if(reinicio == "0"):
            print("Saindo ....")
            break    

            continue




        

