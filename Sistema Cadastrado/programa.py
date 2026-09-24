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
        
        
    if opcao == "6":
        print("=" * 69)
        print("=" * 25, "GERAR RELATÓRIO", "=" * 27)
        print("=" * 69)
        print()

        try:
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                lista_problemas = json.load(arquivo)
        except:
            lista_problemas = []

        houve_alteracao = False

        # Se houver problemas, verifica se algum está sem a descrição
        for problema in lista_problemas:
            descricao = problema.get('problema') or problema.get('descricao') or problema.get('titulo')
            if not descricao or str(descricao).strip() == "N/A":
                print("-" * 69)
                print(f"O problema ID {problema['id']} (Usuário: {problema['nome']}) não tem descrição.")
                nova_desc = input("Digite a descrição/título deste problema: ")
                problema['problema'] = nova_desc
                houve_alteracao = True
                print("Descrição adicionada com sucesso!\n")

        if houve_alteracao:
            with open("dados.json", "w", encoding="utf-8") as arquivo:
                json.dump(lista_problemas, arquivo, indent=4, ensure_ascii=False)

        # Montagem do relatório
        texto_relatorio = "=" * 69 + "\n"
        texto_relatorio += f"{'RELATÓRIO DE PROBLEMAS CADASTRADOS':^69}\n"
        texto_relatorio += "=" * 69 + "\n\n"

        qtde_hardware = 0
        qtde_software = 0
        qtde_rede = 0
        qtde_outro = 0
        qtde_simples = 0
        qtde_medio = 0
        qtde_complexo = 0

        # Função simples só para corrigir a exibição dos acentos na tela/relatório
        def fix_txt(txt):
            if isinstance(txt, str):
                try:
                    return txt.encode('latin1').decode('utf-8')
                except:
                    return txt
            return txt

        if len(lista_problemas) == 0:
            texto_relatorio += "Nenhum problema cadastrado até o momento.\n\n"
        else:
            for problema in lista_problemas:
                desc = fix_txt(problema.get('problema', 'Não informado'))
                nome = fix_txt(problema.get('nome', ''))
                local = fix_txt(problema.get('local', ''))
                tipo = fix_txt(problema.get('tipo', ''))
                grau = fix_txt(problema.get('grau', ''))

                texto_relatorio += f"ID: {problema['id']}\n"
                texto_relatorio += f"Nome do Usuário: {nome}\n"
                texto_relatorio += f"Descrição: {desc}\n"
                texto_relatorio += f"Tipo: {tipo}\n"
                texto_relatorio += f"Local: {local}\n"
                texto_relatorio += f"Grau: {grau}\n"
                texto_relatorio += "-" * 69 + "\n"

                # Estatísticas por Tipo (usa o tipo já corrigido)
                tipo_str = str(tipo).strip().capitalize()
                if tipo_str == "Hardware":
                    qtde_hardware += 1
                elif tipo_str == "Software":
                    qtde_software += 1
                elif tipo_str == "Rede":
                    qtde_rede += 1
                else:
                    qtde_outro += 1

                # Estatísticas por Grau (usa o grau já corrigido)
                grau_str = str(grau).strip().capitalize()
                if grau_str == "Simples":
                    qtde_simples += 1
                elif grau_str in ["Médio", "Medio"]:
                    qtde_medio += 1
                elif grau_str == "Complexo":
                    qtde_complexo += 1

        total_problemas = len(lista_problemas)

        # Cálculo de porcentagens (evita divisão por zero se total_problemas == 0)
        pct_hw = (qtde_hardware / total_problemas * 100) if total_problemas > 0 else 0.0
        pct_sw = (qtde_software / total_problemas * 100) if total_problemas > 0 else 0.0
        pct_rd = (qtde_rede / total_problemas * 100) if total_problemas > 0 else 0.0
        pct_ot = (qtde_outro / total_problemas * 100) if total_problemas > 0 else 0.0

        pct_simples = (qtde_simples / total_problemas * 100) if total_problemas > 0 else 0.0
        pct_medio = (qtde_medio / total_problemas * 100) if total_problemas > 0 else 0.0
        pct_complexo = (qtde_complexo / total_problemas * 100) if total_problemas > 0 else 0.0

        # Resumo Estatístico Final
        texto_relatorio += "\n" + "=" * 69 + "\n"
        texto_relatorio += f"Total de problemas registrados: {total_problemas}\n\n"
        texto_relatorio += "--- POR TIPO DE PROBLEMA ---\n"
        texto_relatorio += f"Hardware: {qtde_hardware} ({pct_hw:.1f}%)\n"
        texto_relatorio += f"Software: {qtde_software} ({pct_sw:.1f}%)\n"
        texto_relatorio += f"Rede: {qtde_rede} ({pct_rd:.1f}%)\n"
        texto_relatorio += f"Outro: {qtde_outro} ({pct_ot:.1f}%)\n\n"
        texto_relatorio += "--- POR GRAU DE COMPLEXIDADE ---\n"
        texto_relatorio += f"Simples: {qtde_simples} ({pct_simples:.1f}%)\n"
        texto_relatorio += f"Médio: {qtde_medio} ({pct_medio:.1f}%)\n"
        texto_relatorio += f"Complexo: {qtde_complexo} ({pct_complexo:.1f}%)\n"
        texto_relatorio += "=" * 69 + "\n"

        # Salva o arquivo relatorio.txt
        with open("relatorio.txt", "w", encoding="utf-8") as arq_relatorio:
            arq_relatorio.write(texto_relatorio)

        # Imprime na tela
        print(texto_relatorio)
        print("Relatório exportado com sucesso para 'relatorio.txt'!\n")
