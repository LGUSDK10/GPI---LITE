import json


while True:
    print("="*69)
    print("="*10, "GPI - GERENCIAMENTO DE PROBLEMAS DA INFORMÁTICA", "="*10)
    print("="*69, "\n")
    print("1- Cadastrar problema") #Antônio
    print("2- Exibir problemas")  #Luiz Carlos
    print("3- Pesquisar problema") #Luiz Carlos
    print("4- Editar problema") #Luiz Gustavo
    print("5- Deletar problema") #Luiz Gustavo
    print("6- Gerar relatório") #Enzo
    print("0- Sair\n") #Antonio
    opcao = input("Digite a opção desejada: ")

    if opcao == "0":
        # Saindo do programa
        print("="*69)
        print("Saindo do programa...")
        print("="*69)
        break

    if opcao == "1":
        print("="*69)
        print("="*23, "CADASTRO DE PROBLEMAS", "="*23)
        print("="*69, "\n")
        print("Responda as perguntas abaixo para cadastrar o problema:\n")

        # Carregando os registros existentes
        try:
            with open("dados.json", "r") as arquivo:
                lista_problemas = json.load(arquivo)

        except:
            lista_problemas = []

        # Encontrando o maior ID
        maior_id = 0

        for problema in lista_problemas:
            if problema["id"] > maior_id:
                maior_id = problema["id"]

        id = maior_id + 1

        # Registro do nome, matrícula, tipo, local e grau do problema
        nome = input("Digite o nome do usuário: ")
        print()
        
        nome_problema = input("Digite o nome do problema que você deseja cadastrar: ")  
        print()

        while True:
            print("Escolha o tipo do problema: \n")
            print("1- Hardware;")
            print("2- Software;")
            print("3- Rede;")
            print("4- Outro;\n")
            opcaotipo = input("Digite a opção desejada: ")
            print()

            if opcaotipo > "4" or opcaotipo < "1":
                print("Opção inválida!\n")
                continue
            elif opcaotipo == "4":
                tipo = input("Digite o tipo do problema: ")
                print()
                break
            else:
                if opcaotipo == "1":
                    tipo = "Hardware"
                elif opcaotipo == "2":
                    tipo = "Software"
                elif opcaotipo == "3":
                    tipo = "Rede"
                break

        while True:
            print("Escolha o local do problema:\n")
            print("1- Laboratório de Redes;")
            print("2- Laboratório de Manutenção;")
            print("3- Coordenação/Secretária;")
            print("4- Sala de aula;\n") 
            opcaolocal = input("Digite a opção desejada: ")
            print()

            if opcaolocal > "4" or opcaolocal < "1":
                print("Opção inválida!\n")
                continue
            else:
                if opcaolocal == "1":
                    local = "Laboratório de Redes"
                elif opcaolocal == "2":
                    local = "Laboratório de Manutenção"
                elif opcaolocal == "3":
                    local = "Coordenação/Secretária"
                elif opcaolocal == "4":
                    local = "Sala de aula"
                break

        while True:
            print("Escolha o grau do problema: \n")
            print("1- Simples;")
            print("2- Médio;")
            print("3- Complexo;\n")
            opcaograu = input("Digite a opção desejada: ")
            print()

            if opcaograu > "3" or opcaograu < "1":
                print("Opção inválida!\n")
                continue
            else:
                if opcaograu == "1":
                    grau = "Simples"
                elif opcaograu == "2":
                    grau = "Médio"
                elif opcaograu == "3":
                    grau = "Complexo"
                break

        # Criando o dicionário de cadastro
        cadastro = {
            "id": id,
            "nome": nome,
            "tipo": tipo,
            "local": local,
            "grau": grau
        }

        lista_problemas.append(cadastro)

        # Salvando os registros no arquivo JSON
        with open("dados.json", "w") as arquivo:
            json.dump(lista_problemas, arquivo, indent=4)

        print("Cadastro realizado com sucesso!\n")
        print("O código do seu problema é:", id, "\n")
        print("Dados do problema cadastrado:")
        print("Usuário: ",nome, "| Tipo: ",tipo, "| Local: ",local, "| Grau: ",grau, "\n")

    if opcao == "2":
        print("="*69)
        print("="*23,"EXIBIÇÃO DE PROBLEMAS", "="*23)
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
            print("Nenhum problema cadastrado até o momento.\n")
    
    if opcao == "3":
        print("="*69)
        print("="*23,"PESQUISA DE PROBLEMAS","="*23)
        print("="*69)

        try:
            with open("dados.json", "r") as arquivo:
                lista_problemas = json.load(arquivo)

            if len(lista_problemas) == 0:
                print("Nenhum problema cadastrado até o momento.\n")

            else:
                while True:
                    print("\nEscolha a forma de pesquisa:\n")
                    print("1- Pesquisar por ID;")
                    print("2- Pesquisar por nome;")
                    print("0- Voltar\n")

                    opcaopesquisa = input("Digite a opção desejada: ")

                    if opcaopesquisa == "0":
                        break

                    elif opcaopesquisa == "1":
                        id_pesquisa = int(input("Digite o código do problema: "))
                        encontrou = False

                        for problema in lista_problemas:
                            if problema["id"] == id_pesquisa:
                                print()
                                print("-"*69)
                                print("Problema encontrado:")
                                print("Código:", problema["id"])
                                print("Nome:", problema["nome"])
                                print("Tipo:", problema["tipo"])
                                print("Local:", problema["local"])
                                print("Grau:", problema["grau"])
                                print("-"*69)
                                encontrou = True

                        if encontrou == False:
                            print("Problema não encontrado.")

                    elif opcaopesquisa == "2":
                        nome_pesquisa = input("Digite o nome: ")
                        encontrou = False

                        for problema in lista_problemas:
                            if problema["nome"] == nome_pesquisa:
                                print()
                                print("-"*69)
                                print("Problema encontrado:")
                                print("Código:", problema["id"])
                                print("Nome:", problema["nome"])
                                print("Tipo:", problema["tipo"])
                                print("Local:", problema["local"])
                                print("Grau:", problema["grau"])
                                print("-"*69)
                                encontrou = True

                        if encontrou == False:
                            print("Problema não encontrado.")

                    else:
                        print("Opção inválida!\n")

        except:
            print("Nenhum problema cadastrado.\n")

    if opcao == "4":
        print("="*69)
        print("="*25, "EDIÇÃO DE PROBLEMA", "="*24)
        print("="*69)
        
        print("Responda as perguntas abaixo para editar o problema:\n")
        try:
            id_editar = int(input("Digite o código do problema que deseja editar: "))
        except ValueError:
            # Evita que o programa encerre caso o usuário digite algo que não seja número
            print("Código inválido! Digite apenas números.\n")
            continue

        with open('dados.json', 'r') as arquivo:
            lista_problemas = json.load(arquivo) # Carrega os dados do arquivo JSON para uma lista de dicionários
        encontrado = False  # Controla se o ID procurado foi encontrado
        
        for problema in lista_problemas: # Percorre a lista de problemas cadastrados
            if problema["id"] == id_editar:
                encontrado = True

                print("Problema encontrado!\n")
                print("-"*69)
                print("Dados do problema cadastrado:")
                print("Nome:", problema["nome"])
                print("Tipo:", problema["tipo"])
                print("Local:", problema["local"])
                print("Grau:", problema["grau"])
                print("-"*69)
                print("Escolha o que deseja editar:\n")
                print("1- Usuário;")
                print("2- Tipo;")
                print("3- Local;")
                print("4- Grau;\n")
                opcaoeditar = input("Digite a opção desejada: ")
                print()
                
                if opcaoeditar == "1":
                    problema["nome"] = input("Digite o novo nome do usuário: ")
                    
                elif opcaoeditar == "2":
                    print("Escolha o novo tipo do problema: \n")
                    print("1- Hardware;")
                    print("2- Software;")
                    print("3- Rede;")
                    print("4- Outro;\n")
                    opcaotipoeditar = input("Digite a opção desejada: ")
                    print()
                    if opcaotipoeditar == "1":
                        problema["tipo"] = "Hardware"
                    elif opcaotipoeditar == "2":
                        problema["tipo"] = "Software"
                    elif opcaotipoeditar == "3":
                        problema["tipo"] = "Rede"
                    elif opcaotipoeditar == "4":
                        problema["tipo"] = input("Digite o novo tipo do problema: ")
                        
                elif opcaoeditar == "3":
                    print("Escolha o novo local do problema:\n")
                    print("1- Laboratório de Redes;")
                    print("2- Laboratório de Manutenção;")
                    print("3- Coordenação/Secretária;")
                    print("4- Sala de aula;\n") 
                    opcaolocaleditar = input("Digite a opção desejada: ")
                    print()
                    if opcaolocaleditar == "1":
                        problema["local"] = "Laboratório de Redes"
                    elif opcaolocaleditar == "2":
                        problema["local"] = "Laboratório de Manutenção"
                    elif opcaolocaleditar == "3":
                        problema["local"] = "Coordenação/Secretária"
                    elif opcaolocaleditar == "4":
                        problema["local"] = "Sala de aula"

                elif opcaoeditar == "4":
                    print("Escolha o novo grau do problema: \n")
                    print("1- Simples;")
                    print("2- Médio;")
                    print("3- Complexo;\n")
                    opcaograueditar = input("Digite a opção desejada: ")
                    print()
                    if opcaograueditar == "1":
                        problema["grau"] = "Simples"
                    elif opcaograueditar == "2":
                        problema["grau"] = "Médio"
                    elif opcaograueditar == "3":
                        problema["grau"] = "Complexo"
                break # Como o ID é único, não precisamos continuar percorrendo a lista

        if not encontrado:
            print("Problema não encontrado!\n") # Só aparece se o for terminar sem encontrar o ID
                
        with open('dados.json', 'w') as arquivo:
            json.dump(lista_problemas, arquivo, indent=4) # Salva a lista atualizada novamente no JSON
        print("-"*69)
        print("Problema atualizado com sucesso!\n")
        print("Nome:", problema["nome"])
        print("Tipo:", problema["tipo"])
        print("Local:", problema["local"])
        print("Grau:", problema["grau"])
        print("-"*69)

    if opcao == "5":
        print("="*69)
        print("="*26, "DELETAR PROBLEMA", "="*25)
        print("="*69)
        
        try:
            id_deletar = int(input("Digite o código do problema que deseja deletar: "))
        except ValueError:
            # Trata uma entrada que não seja numérica
            print("Código inválido! Digite apenas números.\n")
            continue

        with open('dados.json', 'r') as arquivo: # Carrega os problemas armazenados no JSON
            lista_problemas = json.load(arquivo)
        encontrado = False
        
        for problema in lista_problemas: # Percorre a lista de problemas cadastrados
            if problema["id"] == id_deletar:
                encontrado = True

                print("Problema encontrado!\n")
                print("-"*69)
                print("Dados do problema cadastrado:")
                print("Nome:", problema["nome"])
                print("Tipo:", problema["tipo"])
                print("Local:", problema["local"])
                print("Grau:", problema["grau"])
                print("-"*69)
                print("Deseja realmente deletar este problema? (S/N)")
                opcao_deletar = input().upper() # Converte a resposta para maiúscula para aceitar "s" ou "S"
                if opcao_deletar == "S":
                    lista_problemas.remove(problema)
                    print("Problema deletado com sucesso!\n")
                else:
                    print("Operação cancelada!\n")
                break

        if not encontrado:
            print("Problema não encontrado!\n")
                
        with open('dados.json', 'w') as arquivo:
            json.dump(lista_problemas, arquivo, indent=4) # Salva o JSON depois da possível exclusão
        print("Operação concluída!\n")