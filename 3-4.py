servico = 0 #Serviço escolhido
paginas = 0 #Quantidade de páginas
extra = 0 #Serviço extra
valor_disc = 0 #Valor do desconto



def escolha_servico():
    global servico
    print("DIG - Digitalização")
    print("ICO - Impressão Colorida")
    print("IPB - Impressão Preto e Branco")
    print("FOT - Fotocópia")
    escolha_Do_Servico = input("").upper()
    if(escolha_Do_Servico == "DIG"):
        servico = 1.10
    elif(escolha_Do_Servico == "ICO"):
        servico = 1.00
    elif(escolha_Do_Servico == "IPB"):
        servico = 0.40
    elif(escolha_Do_Servico == "FOT"):
        servico = 0.20
    return escolha_Do_Servico    

def num_pagina():
    global valor_disc, paginas
    try:
        paginas = int(input("Entre com o número de páginas: "))
        
    except: 
        print("Não aceitamos Palavras, apenas Números")#caso o usuári o coloque alguma outra coisa que não seja número, este print retorna
        return True
    else:
        if(paginas >= 20 and paginas < 200):
            valor_disc = 15 / 100 #15% de disconto
        elif(paginas >= 200 and paginas < 2000):
            valor_disc = 20 / 100 #20% de disconto
        elif(paginas >= 2000 and paginas < 20000):
            valor_disc = 25 / 100 #20% de desconto
        elif(paginas > 20000):#Limite de páginas abaixo de 20000
            print("Não aceitamos tantas páginas de uma vez")
            print("Por favor, entre com o número de páginas novamente\n")
            return True
        else:
            return True

def servico_extra():
    global extra
    print("\nDeseja adiconar algum serviço extra?")
    print("1 - Encadernação Simples - R$ 15.00 ")
    print("2 - Encadernação Capa Dura- R$ 40.00 ")
    print("0 - Não desejo mais nada")
    escolha_extra = input("")
    return escolha_extra

print("Bem-vindo a Copiadora Do Matheus Ned")
escolha = escolha_servico()
while(escolha != "DIG" and escolha != "ICO" and escolha != "IPB" and escolha != "FOT"):#filtração, caso o usuário coloque outra opção além das apresentadas
    print("Escolha inválida, entre com o tipo de serviço novamente")
    escolha = escolha_servico()

paginas_return = num_pagina()
while(paginas_return):
    paginas_return = num_pagina()

while(True):
    escolha_extra = servico_extra()
    if(escolha_extra != "0" and escolha_extra != "1" and escolha_extra != "2"):#filtração, caso o usuário coloque outra opção além das apresentadas
        continue
    elif(escolha_extra == "1"):
        extra = 15.00
        break
    elif(escolha_extra == "2"):
        extra = 40.00
        break
    else:
        break
total = (servico * paginas) + extra
total = total - (total * valor_disc) #total a pagar com desconto ou sem desconto    
print(f"Total: R$ {total} (serviços: {servico} páginas: {paginas} + extra: {extra})")   
      



    
