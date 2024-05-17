import random


def validarEscolha(esc):

    if(esc == "pedra" or esc == "tesoura" or esc == "papel"):
        return True
    else:
        return False
        
def escMaquina():
    esc = random.randint(0,2)
    maquina = ["pedra", "papel", "tesoura"]
    return maquina[esc]

def ganhador(j1, j2):
    if((j1 == "tesoura" and j2 == "papel") or (j1 == "pedra" and j2 == "tesoura") or (j1 == "papel" and j2 == "pedra")):
        return "Jogador Ganhou"
    elif(j1 == j2):
        return "Empate"
    else:
        return "Maquina Ganhou"
    


def inicio(pontosJ1, pontosJ2):
    while(True):
        j1 = input("Escolha: pedra, papel,  ou tesoura: ")
        j2 = escMaquina()
        if(validarEscolha(j1)):
            print(f"Escolha do Jogador: {j1}\nEscolha da Maquina {j2}\n------------------")
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
    pontosJ1 = 0
    pontosJ2 = 0
    inicio(pontosJ1, pontosJ2)
    reinicio = reenicio_or_fim()
    print(reinicio+"op 1")

    if(reinicio == "1"):
        continue
    elif(reinicio == "0"):
        print("Saindo .........")
        break
    else:
        reinicio = reenicio_or_fim()
        while(reinicio != "0" or reinicio != "1"):
            print("Escolha invalida!!")
            reinicio = reenicio_or_fim()
            print(reinicio+"op 2")

        continue




        

