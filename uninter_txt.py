#verificar escolha do usuario
def opEscolhida(min, maxi):
    escolha = int(input("Escolha a opcao: \n"))
    while(escolha < min or escolha > maxi):
        escolha = int(input("Escolha a opcao: "))
    
    return escolha

#verificar arquivo existente
def verificar(arquivo):
    try:
        a = open(arquivo, "rt")
        a.close()
    except FileNotFoundError:
        print("Arquivo nao encontrado")
        return False
    else:
        return True

#criar arquivo
def criarArquivo(arquivo):
    try:
        a = open(arquivo, "wt+")
        a.close()
    except:
        print("arquivo nao criado")  
    else:
        print("arquivo criado")
# escrever no arquivo
def escrever(nome, pro, arquivo):
    try:
        a = open(arquivo, "at")
    except:
        print("errrrr")
    else:
        a.write(f'{"-"*13}\n|{nome} - {pro}|\n{"-"*13}')
    finally:
        a.close()   
#ler arquivo

def ler(arquivo):
    try:
        a = open(arquivo, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        print(f'{a.read()}')
    finally:
        a.close()        

arquivo = "game.txt"

if(verificar(arquivo)):
    print("arquivo existe")
    verificar(arquivo)

else:
    print("arquivo nao existe")
    criarArquivo(arquivo)


while(True):
    print('Opcoes para escolher')
    print('1 - criar arquivo')
    print('2 - Ler arquivo')
    print('3 - sair\n')

    escolha = opEscolhida(1, 3)
    if(escolha == 1):
        print("Arquivo cadastrado")
        nomeJogo = input("Nome do jogo: ")
        produtora = input("Produtora do jogo: ")
        escrever(nomeJogo, produtora, arquivo)
    elif(escolha == 2):
        ler(arquivo)
    else:
        print("Saindo..")
        break