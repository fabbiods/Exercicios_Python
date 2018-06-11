 #Subindo script no Github


entregas = [{"Nome":"Fabio","Endereco":"Rua Julio Dantas","Produto":[{"Nome":"Salgadinho","Valor":15}]}]

def cadastro():
    nome = raw_input("Digite o nome: ")
    for entrega in entregas:
        if nome == entrega["Nome"]:
            cadastro_item(entregas.index(entrega))
        else:
            Endereco = raw_input("Digite o endereco")
            entregas.append({"Nome":nome, "Endereco":Endereco, "Produto":[]})
            cadastro_item_new()
    print entregas


def cadastro_item_new():
    new_item = raw_input("Digite o nome do produto: ")
    new_itemValue = raw_input("Digite o valor do produto: ")
    entregas[-1]["Produto"].append({"Nome": new_item, "Valor":new_itemValue})


def cadastro_item(numero):
    while True:
        decisao = raw_input("Deseja cadastrar novo item? sim / nao: ")
        if decisao == "sim":
            new_item = raw_input("Digite o nome do produto: ")
            new_itemValue = raw_input("Digite o valor do produto: ")
            entregas[numero]["Produto"].append({"Nome": new_item, "Valor":new_itemValue})
           
            

        else:
            print "Cadastro finalizado"
            break
    

cadastro()

      
        


