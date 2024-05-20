
dados = [
        {"nome":"ned", "idade":34, "genero":"masculino"},
        {"nome":"kali", "idade":12, "genero":"masculino"},
        {"nome":"paki", "idade":98, "genero":"masculino"},
        {"nome":"jessica", "idade":34, "genero":"feminino"},
        {"nome":"maria", "idade":12, "genero":"feminino"},
        {"nome":"juliana", "idade":98, "genero":"feminino"},
        {"nome":"kely", "idade":13, "genero":"feminino"}
         ]
mulheres_menor = []
media = []
homens_acima = []
def media_total():
    global dados, mulheres_menor, media, homens_acima
    soma_idades = 0
    for dado in dados:
        soma_idades +=dado["idade"]
    numero_pessoas = len(dados)
    media_idade = soma_idades / numero_pessoas
    return media_idade
def mulheres():
    for cadastros in dados:
        if(cadastros["genero"] == "feminino" and cadastros["idade"] < 30):
            mulheres_menor.append(cadastros["nome"])

def homens_acima_media():
    for homem in dados:
        if(homem["genero"] == 'masculino' and homem["idade"] > 30):
            homens_acima.append(homem["nome"])
            

def finalizando():
        mulheres()
        homens_acima_media()
        print('-'*20)
        print(f'Total de cadastros {len(dados)}\n')
        print(f'Mulheres om menos de 30 anos {mulheres_menor}\n')
        print(f'Media de idades: {media_total()}\n')
        print(f'Homens acima de 30 anos {homens_acima}\n')
        print('-'*20)
        print('Saindo ......')

while(True):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    genero = input("Genero: ")
    dados.append({"nome":nome, "idade":idade, "genero":genero})
    esc = int(input("Deseja fazer outro cadastro?\n1 - Sim\n2 - Nao\n"))

    if(esc == 1):
        continue
    elif(esc == 2):
        finalizando()
        break
    else:
        print("Escolha inválida!!")
        esc = int(input("Deseja fazer outro cadastro?\n1 - Sim\n2 - Nao\n"))
        while(esc != 1 and esc != 2):
            print("Escolha inválida!! -------")
            esc = int(input("Deseja fazer outro cadastro?\n1 - Sim\n2 - Nao\n"))
            
        if(esc == 2):
            finalizando()
            break


    
