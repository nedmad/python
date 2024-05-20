print("Bem-Vindo a Loja do Matheus Ned")
valor_produto = int(input("Entre com o valor do produto: "))
quantidade_produto = int(input("Entre com a quantidade do produto: "))
resul = valor_produto * quantidade_produto #resultado do valor do produto, multiplicado pela quantidade escolhida
if(resul < 2500):
    #Aqui ira printar o valor da compra sem o desconto
    print(f"Valor sem desconto: {resul}")
elif(resul >= 2500 and resul < 6000):
    descont = resul - (resul * (4 / 100))  #Aqui sera aplicado o valor do desconto de 4%
    print(f"Valor SEM desconto: {resul}")
    print(f"Valor COM desconto: {descont}")
elif(resul >= 6000 and resul < 10000):
    descont =  resul - (resul * (7 / 100))  #Aqui sera aplicado o valor do desconto de 7%
    print(f"Valor SEM desconto: {resul}")
    print(f"Valor COM desconto: {descont}")
else:
    descont = resul - (resul * (11 / 100)) #Aqui sera aplicado o valor do desconto de 11%
    print(f"Valor SEM desconto: {resul}") 
    print(f"Valor COM desconto: {descont}")

