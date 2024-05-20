cardapio = f'{"-"*20}Cardápio{"-"*20}'
print('Bem-Vindo a Loja de Gelados do Matheus Ned')
print(cardapio)
print("-"*len(cardapio))
print(f'---|  Tamanho  |  Cupuaçu(CP)  |  Açaí(AC)   |---')
print(f'---|     P     |    R$ 9.00    |   R$ 11.00  |---')
print(f'---|     M     |    R$ 14.00   |   R$ 16.00  |---')
print(f'---|     G     |    R$ 18.00   |   R$ 20.00  |---')
print("-"*len(cardapio))
valor_total = 0 #Soma de todo o valor a se pagar $

def resposta_input(resul):#func onde será filtrada a resposta do usuário, retonando True ou False
    if((resul == "CP" or resul == "AC" ) or (resul == "P" or resul == "M" or resul == "G")):
        #Aqui filtra o sabor cp/ac, e o tamanho p/m/g
        #retorna False para quebrar o loop
        return False
    else:
        #caso o resul não for nenhuma das opções anteriores, retorna True para continuar com  o loop
        return True
    
def soma(sabor, tamanho):
    global valor_total
    if(sabor == "CP" and tamanho == "P"):# Começo da Escolha do sabor CP e soma de valore a partir do tamanho
        valor_total += 9.00
        print(f'Você um Cupuaçu no tamanho {tamanho}: $ 9.00')
    elif(sabor == "CP" and tamanho == "M"):
        valor_total += 14.00
        print(f'Você um Cupuaçu no tamanho {tamanho}: $ 14.00')
    elif(sabor == "CP" and tamanho == "G"):
        valor_total += 18.00
        print(f'Você um Cupuaçu no tamanho {tamanho}: $ 18.00')
    elif(sabor == "AC" and tamanho == "P"):# Começo da Escolha do sabor AC e soma de valore a partir do tamanho
        valor_total += 11.00
        print(f'Você um Açaí no tamanho {tamanho}: $ 11.00')
    elif(sabor == "AC" and tamanho == "M"):
        valor_total += 16.00
        print(f'Você um Açaí no tamanho {tamanho}: $ 16.00')
    elif(sabor == "AC" and tamanho == "G"):
        valor_total += 20.00
        print(f'Você um Açaí no tamanho {tamanho}: $ 20.00')

    

while(True):
    sabor = input("Entre com o Sabor Desejado (CP/AC): ").upper()

    while(resposta_input(sabor)):#Aqui retornará a resposta da função, True ou False
        print("Sabor inválido. Tente Novamente")
        sabor = input("Entre com o Sabor Desejado (CP/AC): ").upper()

    tamanho = input("Entre com o Tamanho Desejado (P/M/G): ").upper()
    
    while(resposta_input(tamanho)):#Aqui retornará a resposta da função, True ou False
        print("Tamanho inválido. Tente Novamente")
        tamanho = input("Entre com o Tamanho Desejado (P/M/G): ").upper()
    
    soma(sabor, tamanho) #Chama a func para fazer toda a soma dos valore a ser pago

    S_or_N = input("\nDeseja mais alguma coisa? (S/N): ").upper()

    if(S_or_N == "S"):
        continue
    else:
        print(f"\nValor total a ser pago: {valor_total}")
        break



