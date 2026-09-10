import json

while True:
    print("="*10, "GPI - GERENCIAMENTO DE PROBLEMAS DA INFORMÁTICA", "="*10, "\n")
    print("1- Cadastrar problema\n") #Antônio
    print("2- Exibir problemas\n")  #Luiz Carlos
    print("3- Pesquisar problema\n") #Luiz Carlos
    print("4- Editar problema\n") #Luiz Gustavo
    print("5- Deletar problema\n") #Luiz Gustavo
    print("6- Gerar relatório\n") #Enzo
    print("0- Sair\n") #Antonio
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("="*69)
        nome = input("Digite seu problema: ")
        print("Escolha o local do problema:")
        print("1- Laboratório de Redes;")
        print("2- Laboratório de Manutenção;")
        print("3- Coordenação/Secretária;")
        print("3- Sala de aula;")
        local = input("Digite a opção desejada: ")
    
        while True:
            print("Escolha o grau do problema:")
            print("1- Simples;")
            print("2- Médio;")
            print("3- Complexo;")
            grau = input("Digite a opção desejada: ")
            if grau > "3" or grau < "1":
                print("Opção inválida!")
                continue
            else:
                break
        
            




    