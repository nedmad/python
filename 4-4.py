
lista_livros = []
id_global = 0

def cadastrar_livro(id_global):
    id_global
    print(f"Id do livro: {id_global}")
    titulo = input("Por favor, entre com o Titulo: ")
    autor = input("Por favor, entre com o Autor: ")
    editora = input("Por favor, entre com a Editora: ")
    lista_livros.append({"id": id_global,"titulo":titulo, "autor": autor, "editora":editora})

def consultar_livro():
    global lista_livros
    while(True):
        print("----------------------------------------")
        print("---------Menu de Cosulta do Livro-------")
        print("Escolha a opção desejado")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por id")
        print("3 - Consultar Livro(s) por autor")
        print("4 - Retornar Menu Principal")
        escolha = input("")

        if(escolha == "1"):
            for livro in lista_livros:#Filtra Todos os Livros
                print(f"\nId: {livro['id']}\nTitulo: {livro['titulo']}\nAutor: {livro['autor']}\n{livro['editora']}")
        elif(escolha == "2"):#Filtra por id
            id = int(input("id: "))
            livro = list(filter(lambda val: val["id"] == id, lista_livros))
            print(f"\nId: {livro[0]['id']}\nTitulo: {livro[0]['titulo']}\nAutor: {livro[0]['autor']}\n{livro[0]['editora']}")
        elif(escolha == "3"):#Filtra por autor
            autor = input("Autor: ")
            livro = list(filter(lambda val: val["autor"] == autor, lista_livros))
            print(f"\nId: {livro[0]['id']}\nTitulo: {livro[0]['titulo']}\nAutor: {livro[0]['autor']}\n{livro[0]['editora']}")
        elif(escolha == "4"):#Voltar menu inicial
            break
        else:#Valor invalido
            print("\nOpção Inválida!!")

def remover_livro():
    print("----------------------------------------")
    print("---------Menu Remover Livro-------")
    global lista_livros
    while(True):
        id = int(input("Id do Livro: "))
        livro = list(filter(lambda val: val["id"] == id, lista_livros))#Filtrando o livro pelo id
        if(livro == []):#Caso nao encontre o id escolhido e ele retorne [], continuar com o loop
            print("Id Não Encobtrado!!")
            continue
        else:
            for livr in lista_livros:
                if(livr["id"] == id):
                    lista_livros.remove(livr)
            print("Livro removido com sucesso!")
            break


while(True):
    print("Bem Vindo a Livraria do Matheus Ned")
    print("------------------------------")
    print("---------Menu Principal-------")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    escolha = input("")

    #Opção escolhida entrará em um condição, que chamará a função relacionada
    if(escolha == "1"):#Cadastrar Livro
        id_global += 1
        cadastrar_livro(id_global)
    elif(escolha == "2"):#Consultar Livro
        consultar_livro()
    elif(escolha == "3"):#Remover Livro
        remover_livro()
    elif(escolha == "4"):#Sair
        break
    else:#Valor Inválido
        print("Escolha Inválida!!\n")