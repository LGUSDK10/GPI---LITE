
    if opcao == "2":
        print("="*69)
        print("="*25,"EXIBINDO PROBLEMAS", "="*24)
        print("="*69)

        try:
            with open("dados.json", "r") as arquivo:
                lista_problemas = json.load(arquivo)

            if len(lista_problemas) == 0:
                print("Nenhum problema cadastrado.\n")
            else:
                for problema in lista_problemas:
                    print("ID:", problema["id"])
                    print("Nome:", problema["nome"])
                    print("Tipo:", problema["tipo"])
                    print("Local:", problema["local"])
                    print("Grau:", problema["grau"])
                    print("-"*69)

        except:
            print("Nenhum problema cadastrado.\n")
    
    if opcao == "3":
        print("="*69)
        print("="*25,"PESQUISAR PROBLEMA","="*24)
        print("="*69)

        try:
            with open("dados.json", "r") as arquivo:
                lista_problemas = json.load(arquivo)

            if len(lista_problemas) == 0:
                print("Nenhum problema cadastrado.\n")

            else:
                while True:
                    print("1- Pesquisar por ID")
                    print("2- Pesquisar por nome")
                    print("0- Voltar\n")

                    opcaopesquisa = input("Digite a opção desejada: ")

                    if opcaopesquisa == "0":
                        break

                    elif opcaopesquisa == "1":
                        id_pesquisa = int(input("Digite o ID do problema: "))
                        encontrou = False

                        for problema in lista_problemas:
                            if problema["id"] == id_pesquisa:
                                print("\nProblema encontrado:")
                                print("ID:", problema["id"])
                                print("Nome:", problema["nome"])
                                print("Tipo:", problema["tipo"])
                                print("Local:", problema["local"])
                                print("Grau:", problema["grau"])
                                encontrou = True

                        if encontrou == False:
                            print("Problema não encontrado.")

                    elif opcaopesquisa == "2":
                        nome_pesquisa = input("Digite o nome: ")
                        encontrou = False

                        for problema in lista_problemas:
                            if problema["nome"] == nome_pesquisa:
                                print("\nProblema encontrado:")
                                print("ID:", problema["id"])
                                print("Nome:", problema["nome"])
                                print("Matrícula:", problema["matricula"])
                                print("Tipo:", problema["tipo"])
                                print("Local:", problema["local"])
                                print("Grau:", problema["grau"])
                                encontrou = True

                        if encontrou == False:
                            print("Problema não encontrado.")

                    else:
                        print("Opção inválida!\n")

        except:
            print("Nenhum problema cadastrado.\n")  