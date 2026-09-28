import json
import time

# -------- Equipe COSMOBYTE --------
# GPI LITE - GERENCIAMENTO DE PROBLEMAS DA INFORMÁTICA

# Código desenvolvido para obtenção de nota na disciplina de Programação II - 2026.2
# Alunos envolvidos: Antônio V., Enzo, Luiz Carlos e Luiz Gustavo
# Tema central: Versão simplificada (protótipo) do sistema que desenvolveremos na disciplina de Desenvolvimento de projetos I
while True:
    print("="*69)
    print("="*10, "GPI LITE - GERENCIAMENTO DE PROBLEMAS DA INFORMÁTICA", "="*10)
    print("="*69, "\n")
    print("1- Cadastrar problema") # Membro responsável: Antônio V.
    print("2- Exibir problemas")  # Membro responsável: Luiz Carlos
    print("3- Pesquisar problema") # Membro responsável: Luiz Carlos
    print("4- Editar problema") # Membro responsável: Luiz Gustavo
    print("5- Deletar problema") # Membro responsável: Luiz Gustavo
    print("6- Gerar relatório") # Membro responsável: Enzo
    print("0- Sair\n") # Membro responsável: Antônio V.
    opcao = input("Digite a opção desejada: ")

    if opcao == "0":
        # Saída do programa
        print("="*69)
        print("Saindo do programa...")
        print("="*69)
        time.sleep(1.5)
        break

    if opcao == "1":
        # Cadastra os dados do problema no sistema e salva no arquivo JSON
        # Membro responsável pela explicação: Antônio V.
        print("="*69)
        print("="*23, "CADASTRO DE PROBLEMAS", "="*23)
        print("="*69, "\n")
        print("Responda às perguntas abaixo para cadastrar o problema:\n")

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

        # Registro do nome, problema, tipo, local e grau
        nome = input("Digite o nome do usuário: ")
        print()
        while not nome.strip(): # Verifica se o nome não está vazio ou contém apenas espaços
            print("O nome não pode ficar vazio!")
            nome = input("Digite seu nome: ")
            print()
        
        nome_problema = input("Digite o nome do problema que você deseja cadastrar: ")  
        print()
        while not nome_problema.strip(): # Verifica se o nome do problema não está vazio ou contém apenas espaços
            print("O nome não pode ficar vazio!")
            nome_problema = input("Digite o nome do problema que você deseja cadastrar: ")
            print()

        # Verificando se o mesmo usuário já cadastrou o mesmo problema
        problema_cadastrado = False

        for problema in lista_problemas:
            if problema["nome"] == nome and problema["nomeproblema"] == nome_problema:
                problema_cadastrado = True

        if problema_cadastrado:
            print("Este problema já foi cadastrado para este usuário!\n")
            time.sleep(2)
            continue

        while True: # Tipos de problemas comuns já definidos; outros tipos podem ser digitados manualmente
            print("Escolha o tipo do problema: \n")
            print("1- Hardware;")
            print("2- Software;")
            print("3- Rede;")
            print("4- Outro;\n")
            opcaotipo = input("Digite a opção desejada: ")
            print()

            if opcaotipo > "4" or opcaotipo < "1":
                print("Opção inválida!\n")
                time.sleep(1)
                continue
            elif opcaotipo == "4":
                tipo = input("Digite o tipo do problema: ")
                while not tipo.strip(): # Verifica se o tipo do problema não está vazio ou contém apenas espaços
                    print("O tipo do problema não pode ficar vazio!")
                    tipo = input("Digite o tipo do problema: ")
                print()
                break
            else:
                # Substituindo a opção numérica pelo tipo correspondente
                if opcaotipo == "1":
                    tipo = "Hardware"
                elif opcaotipo == "2":
                    tipo = "Software"
                elif opcaotipo == "3":
                    tipo = "Rede"
                break

        while True: # Locais comuns no instituto já definidos
            print("Escolha o local do problema:\n")
            print("1- Laboratório de Redes;")
            print("2- Laboratório de Manutenção;")
            print("3- Coordenação/Secretária;")
            print("4- Sala de aula;\n") 
            opcaolocal = input("Digite a opção desejada: ")
            print()

            if opcaolocal > "4" or opcaolocal < "1":
                print("Opção inválida!\n")
                time.sleep(1)
                continue
            else:
                # Substituindo a opção numérica pelo local correspondente
                if opcaolocal == "1":
                    local = "Laboratório de Redes"
                elif opcaolocal == "2":
                    local = "Laboratório de Manutenção"
                elif opcaolocal == "3":
                    local = "Coordenação/Secretária"
                elif opcaolocal == "4":
                    local = "Sala de aula"
                break

        while True: # Graus de complexidade do problema já definidos
            print("Escolha o grau do problema: \n")
            print("1- Simples;")
            print("2- Médio;")
            print("3- Complexo;\n")
            opcaograu = input("Digite a opção desejada: ")
            print()

            if opcaograu > "3" or opcaograu < "1":
                print("Opção inválida!\n")
                time.sleep(1)
                continue
            else:
                # Substituindo a opção numérica pelo grau correspondente
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
            "nomeproblema": nome_problema,
            "tipo": tipo,
            "local": local,
            "grau": grau
        }

        lista_problemas.append(cadastro)

        # Salvando os registros no arquivo JSON
        with open("dados.json", "w") as arquivo:
            json.dump(lista_problemas, arquivo, indent=4)

        print("Cadastro realizado com sucesso!\n")

        # Exibição dos dados cadastrados no terminal
        time.sleep(1)
        print("-"*69)
        print("Dados do problema cadastrado:")
        print("Código:", cadastro["id"])
        print("Nome:", cadastro["nome"])
        print("Nome do problema:", cadastro["nomeproblema"])
        print("Tipo:", cadastro["tipo"])
        print("Local:", cadastro["local"])
        print("Grau:", cadastro["grau"])
        print("-"*69)
        time.sleep(2)


    if opcao == "2":  # Verifica se a opção escolhida pelo usuário foi 2
        # Exibe todos os problemas cadastrados
        # Membro responsável pela explicação: Luiz Carlos
        print("="*69)  
        print("="*23,"EXIBIÇÃO DE PROBLEMAS", "="*23) 
        print("="*69)  
        time.sleep(0.5)  # Faz o programa esperar 0,5 segundo

        try:  # Tenta executar os comandos que podem apresentar erro
            with open("dados.json", "r") as arquivo:  # Abre o arquivo dados.json para leitura
                lista_problemas = json.load(arquivo)  # Lê os dados do arquivo e transforma em lista

            if len(lista_problemas) == 0:  # Verifica se a lista está vazia
                print("Nenhum problema cadastrado.\n") 
                time.sleep(1.5)  # Espera 1,5 segundo
            else:  # Executa caso existam problemas cadastrados
                for problema in lista_problemas: 
                    print("Código:", problema["id"])  
                    print("Nome:", problema["nome"])  
                    print("Nome do problema:", problema["nomeproblema"])  
                    print("Tipo:", problema["tipo"])  
                    print("Local:", problema["local"])  
                    print("Grau:", problema["grau"]) 
                    print("-"*69) 

        except:  # Executa caso aconteça algum erro na leitura do arquivo
            print("Nenhum problema cadastrado até o momento.\n")  
            time.sleep(1.5)  # Espera 1,5 segundo
    
    if opcao == "3":  
        # Pesquisa os problemas cadastrados por código ou nome
        # Membro responsável pela explicação: Luiz Carlos
        print("="*69) 
        print("="*23,"PESQUISA DE PROBLEMAS","="*23)  
        print("="*69) 
        time.sleep(0.5)  # Faz o programa esperar 0,5 segundo

        try:  # Tenta executar os comandos que podem apresentar erro
            with open("dados.json", "r") as arquivo:  # Abre o arquivo dados.json para leitura
                lista_problemas = json.load(arquivo)  # Lê os dados do arquivo e transforma em lista

            if len(lista_problemas) == 0:  # Verifica se a lista está vazia
                print("Nenhum problema cadastrado até o momento.\n")  
                time.sleep(1.5)  # Espera 1,5 segundo

            else:  # Executa caso existam problemas cadastrados
                while True:  # Mantém o menu de pesquisa funcionando até o usuário escolher voltar
                    print("\nEscolha a forma de pesquisa:\n")  #
                    print("1- Pesquisar por código;")  
                    print("2- Pesquisar por nome;")  
                    print("0- Voltar\n")  

                    opcaopesquisa = input("Digite a opção desejada: ")  # Recebe a opção escolhida pelo usuário

                    if opcaopesquisa == "0":  # Verifica se o usuário escolheu voltar
                        break  # Encerra o while e volta para o menu anterior

                    elif opcaopesquisa == "1":  # Verifica se o usuário escolheu pesquisar pelo código

                        try:  # Tenta converter o código digitado para número
                            id_pesquisa = int(input("Digite o código do problema: "))  # Recebe o código e transforma em inteiro
                        except ValueError:  # Trata o erro caso o usuário não digite um número
                            print("Código inválido! Digite apenas números.\n")  # Mostra uma mensagem de erro
                            time.sleep(1)  # Espera 1 segundo
                            continue  # Volta para o início do while

                        encontrou = False  # Começa considerando que nenhum problema foi encontrado

                        for problema in lista_problemas:  # Percorre todos os problemas cadastrados
                            if problema["id"] == id_pesquisa:  # Compara o código cadastrado com o código pesquisado
                                print() 
                                print("-"*69)
                                print("Problema encontrado:")  
                                print("Código:", problema["id"])  
                                print("Nome:", problema["nome"])  
                                print("Nome do problema:", problema["nomeproblema"])  
                                print("Tipo:", problema["tipo"])  
                                print("Local:", problema["local"])  
                                print("Grau:", problema["grau"])
                                print("-"*69)  

                                encontrou = True  # Informa que um problema foi encontrado

                        if encontrou == False:  # Verifica se nenhum problema foi encontrado
                            print("Problema não encontrado.")  

                        time.sleep(1.5)  # Espera 1,5 segundo

                    elif opcaopesquisa == "2":  # Verifica se o usuário escolheu pesquisar pelo nome

                        nome_pesquisa = input("Digite o nome: ")  # Recebe o nome que será pesquisado

                        while not nome_pesquisa.strip():  # Verifica se o nome está vazio ou contém apenas espaços
                            print("O nome não pode ficar vazio!")  # Mostra uma mensagem de erro
                            nome_pesquisa = input("Digite o nome: ")  # Pede o nome novamente

                        encontrou = False  # Começa considerando que nenhum problema foi encontrado

                        for problema in lista_problemas:  # Percorre todos os problemas cadastrados
                            if problema["nome"] == nome_pesquisa:  # Compara o nome cadastrado com o nome pesquisado
                                print() 
                                print("-"*69)
                                print("Problema encontrado:") 
                                print("Código:", problema["id"])  
                                print("Nome:", problema["nome"])  
                                print("Nome do problema:", problema["nomeproblema"])  
                                print("Tipo:", problema["tipo"])  
                                print("Local:", problema["local"]) 
                                print("Grau:", problema["grau"])  
                                print("-"*69)  

                                encontrou = True  # Informa que um problema foi encontrado

                        if encontrou == False:  # Verifica se nenhum problema foi encontrado
                            print("Problema não encontrado.")  # Informa que não encontrou o problema

                        time.sleep(1.5)  # Espera 1,5 segundo

                    else:  # Executa caso o usuário digite uma opção que não existe
                        print("Opção inválida!\n")  # Informa que a opção é inválida
                        time.sleep(1)  # Espera 1 segundo

        except:  # Executa caso aconteça algum erro na leitura do arquivo
            print("Nenhum problema cadastrado.\n")  # Informa que não existem problemas cadastrados
            time.sleep(1.5)  # Espera 1,5 segundo


    if opcao == "4":
        # Edita os dados do problema cadastrado
        # Membro responsável pela explicação: Luiz Gustavo
        print("="*69)
        print("="*25, "EDIÇÃO DE PROBLEMA", "="*24)
        print("="*69)
        
        print("Responda às perguntas abaixo para editar o problema:\n")

        try:
            id_editar = int(input("Digite o código do problema que deseja editar: "))
        except ValueError:
            # Evita que o programa encerre caso o usuário digite algo que não seja número
            print("Código inválido! Digite apenas números.\n")
            time.sleep(1)
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
                print("Nome do problema:", problema["nomeproblema"])
                print("Tipo:", problema["tipo"])
                print("Local:", problema["local"])
                print("Grau:", problema["grau"])
                print("-"*69)

                while True:
                    print("Escolha o que deseja editar:\n")
                    print("1- Usuário;")
                    print("2- Nome do problema;")
                    print("3- Tipo;")
                    print("4- Local;")
                    print("5- Grau;\n")
                    opcaoeditar = input("Digite a opção desejada: ")
                    print()

                    if opcaoeditar == "1":
                        novo_nome = input("Digite o novo nome do usuário: ")
                        while not novo_nome.strip():
                            print("O nome não pode ficar vazio!")
                            novo_nome = input("Digite o novo nome do usuário: ")
                        problema["nome"] = novo_nome
                        break
                        
                    elif opcaoeditar == "2":
                        novo_nome_problema = input("Digite o novo nome do problema: ")
                        while not novo_nome_problema.strip():
                            print("O nome do problema não pode ficar vazio!")
                            novo_nome_problema = input("Digite o novo nome do problema: ")
                        problema["nomeproblema"] = novo_nome_problema
                        break

                    elif opcaoeditar == "3":
                        while True:
                            print("Escolha o novo tipo do problema: \n")
                            print("1- Hardware;")
                            print("2- Software;")
                            print("3- Rede;")
                            print("4- Outro;\n")
                            opcaotipoeditar = input("Digite a opção desejada: ")
                            print()

                            if opcaotipoeditar == "1":
                                problema["tipo"] = "Hardware"
                                break
                            elif opcaotipoeditar == "2":
                                problema["tipo"] = "Software"
                                break
                            elif opcaotipoeditar == "3":
                                problema["tipo"] = "Rede"
                                break
                            elif opcaotipoeditar == "4":
                                tipo_novo = input("Digite o novo tipo do problema: ")
                                while not tipo_novo.strip():
                                    print("O tipo do problema não pode ficar vazio!")
                                    tipo_novo = input("Digite o novo tipo do problema: ")
                                problema["tipo"] = tipo_novo
                                break
                            else:
                                print("Opção inválida!\n")
                                time.sleep(1)
                        break
                        
                    elif opcaoeditar == "4":
                        while True:
                            print("Escolha o novo local do problema:\n")
                            print("1- Laboratório de Redes;")
                            print("2- Laboratório de Manutenção;")
                            print("3- Coordenação/Secretária;")
                            print("4- Sala de aula;\n") 
                            opcaolocaleditar = input("Digite a opção desejada: ")
                            print()

                            if opcaolocaleditar == "1":
                                problema["local"] = "Laboratório de Redes"
                                break
                            elif opcaolocaleditar == "2":
                                problema["local"] = "Laboratório de Manutenção"
                                break
                            elif opcaolocaleditar == "3":
                                problema["local"] = "Coordenação/Secretária"
                                break
                            elif opcaolocaleditar == "4":
                                problema["local"] = "Sala de aula"
                                break
                            else:
                                print("Opção inválida!\n")
                                time.sleep(1)
                        break

                    elif opcaoeditar == "5":
                        while True:
                            print("Escolha o novo grau do problema: \n")
                            print("1- Simples;")
                            print("2- Médio;")
                            print("3- Complexo;\n")
                            opcaograueditar = input("Digite a opção desejada: ")
                            print()

                            if opcaograueditar == "1":
                                problema["grau"] = "Simples"
                                break
                            elif opcaograueditar == "2":
                                problema["grau"] = "Médio"
                                break
                            elif opcaograueditar == "3":
                                problema["grau"] = "Complexo"
                                break
                            else:
                                print("Opção inválida!\n")
                                time.sleep(1)
                        break

                    else:
                        print("Opção inválida! Escolha uma opção de 1 a 5.\n")
                        time.sleep(1)

                break # Como o ID é único, não precisamos continuar percorrendo a lista

        if not encontrado:
            print("Problema não encontrado!\n") # Só aparece se o for terminar sem encontrar o ID
            time.sleep(1.5)
        else:
            with open('dados.json', 'w') as arquivo:
                json.dump(lista_problemas, arquivo, indent=4) # Salva a lista atualizada novamente no JSON

            print("-"*69)
            print("Problema atualizado com sucesso!\n")
            print("Nome:", problema["nome"])
            print("Nome do problema:", problema["nomeproblema"])
            print("Tipo:", problema["tipo"])
            print("Local:", problema["local"])
            print("Grau:", problema["grau"])
            print("-"*69)
            time.sleep(2)

    if opcao == "5":
        # Deleta determinado problema cadastrado
        # Membro responsável pela explicação: Luiz Gustavo
        print("="*69)
        print("="*24, "DELEÇÃO DE PROBLEMA", "="*24)
        print("="*69)
        
        try:
            id_deletar = int(input("Digite o código do problema que deseja deletar: "))
        except ValueError:
            # Trata uma entrada que não seja numérica
            print("Código inválido! Digite apenas números.\n")
            time.sleep(1)
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
                print("Nome do problema:", problema["nomeproblema"])
                print("Tipo:", problema["tipo"])
                print("Local:", problema["local"])
                print("Grau:", problema["grau"])
                print("-"*69)
                print("Deseja realmente deletar este problema? (S/N)")
                opcao_deletar = input().upper() # Converte a resposta para maiúscula para aceitar "s" ou "S"

                if opcao_deletar == "S":
                    lista_problemas.remove(problema)
                    print("Problema deletado com sucesso!\n")
                    time.sleep(1.5)
                else:
                    print("Operação cancelada!\n")
                    time.sleep(1.5)

                break

        if not encontrado:
            print("Problema não encontrado!\n")
            time.sleep(1.5)
        else:
            with open('dados.json', 'w') as arquivo:
                json.dump(lista_problemas, arquivo, indent=4) # Salva o JSON depois da possível exclusão

            print("Operação concluída!\n")
            time.sleep(1)

    if opcao == "6":
        # Exporta os dados cadastrados no JSON para o arquivo relatorio.txt e exibe na tela
        # Membro responsável pela explicação: Enzo
        
        # Desenha o cabeçalho da opção no terminal.
        print("=" * 69)
        print("=" * 23, "GERACAO DE RELATORIO", "=" * 24)
        print("=" * 69)
        print()

        try:
            # Abre o arquivo de cadastros para leitura usando a codificação UTF-8.
            with open("dados.json", "r", encoding="utf-8") as arquivo:
                # Converte o conteúdo JSON em uma lista de problemas.
                lista_problemas = json.load(arquivo)
        except:
            # Se ocorrer um erro ao abrir ou ler o JSON, considera que não há cadastros.
            lista_problemas = []

        # Se a lista estiver vazia, informa que não há dados para incluir no relatório.
        if len(lista_problemas) == 0:
            print("Nenhum problema cadastrado ate o momento para gerar o relatorio.\n")
            # Aguarda antes de voltar ao menu.
            time.sleep(1.5)
        else:
            # Informa que o relatório está sendo preparado.
            print("Gerando relatorio...")
            time.sleep(1)

            # Cria dicionários para contar problemas por tipo, grau e local.
            contagem_tipo = {}
            contagem_grau = {}
            contagem_local = {}

            # Guarda o número total de cadastros, usado nas porcentagens.
            total_problemas = len(lista_problemas)

            # Percorre os cadastros para contar quantas vezes cada categoria aparece.
            for problema in lista_problemas:
                # Obtém o tipo como texto e soma uma ocorrência à contagem correspondente.
                tipo = str(problema["tipo"])
                if tipo in contagem_tipo:
                    contagem_tipo[tipo] = contagem_tipo[tipo] + 1
                else:
                    contagem_tipo[tipo] = 1

                # Obtém o grau e atualiza sua contagem.
                grau = str(problema["grau"])
                if grau in contagem_grau:
                    contagem_grau[grau] = contagem_grau[grau] + 1
                else:
                    contagem_grau[grau] = 1

                # Obtém o local e atualiza sua contagem.
                local = str(problema["local"])
                if local in contagem_local:
                    contagem_local[local] = contagem_local[local] + 1
                else:
                    contagem_local[local] = 1

            # Abre o relatório para escrita; o modo "w" substitui o relatório anterior.
            with open("relatorio.txt", "w", encoding="utf-8") as arq_relatorio:

                # Exibe o título do relatório no terminal.
                print("=" * 69)
                print("                 RELATORIO DE PROBLEMAS CADASTRADOS                  ")
                print("=" * 69)
                print()

                # Grava o mesmo título no arquivo de relatório.
                arq_relatorio.write("=====================================================================\n")
                arq_relatorio.write("                 RELATORIO DE PROBLEMAS CADASTRADOS                  \n")
                arq_relatorio.write("=====================================================================\n\n")

                # Percorre novamente os cadastros para apresentar seus dados completos.
                for problema in lista_problemas:
                    # Converte os campos do cadastro para texto para montar as linhas.
                    p_id = str(problema["id"])
                    p_nome = str(problema["nome"])
                    p_nomeprob = str(problema["nomeproblema"])
                    p_tipo = str(problema["tipo"])
                    p_local = str(problema["local"])
                    p_grau = str(problema["grau"])

                    # Mostra os dados deste problema no terminal.
                    print("Codigo:", p_id)
                    print("Nome:", p_nome)
                    print("Nome do problema:", p_nomeprob)
                    print("Tipo:", p_tipo)
                    print("Local:", p_local)
                    print("Grau:", p_grau)
                    print("-" * 69)

                    # Grava os mesmos dados no arquivo, uma informação por linha.
                    arq_relatorio.write("Codigo: " + p_id + "\n")
                    arq_relatorio.write("Nome: " + p_nome + "\n")
                    arq_relatorio.write("Nome do problema: " + p_nomeprob + "\n")
                    arq_relatorio.write("Tipo: " + p_tipo + "\n")
                    arq_relatorio.write("Local: " + p_local + "\n")
                    arq_relatorio.write("Grau: " + p_grau + "\n")
                    # Separa visualmente um cadastro do próximo.
                    arq_relatorio.write("---------------------------------------------------------------------\n")

                # Inicia a seção de estatísticas no terminal.
                print("\n" + "=" * 69)
                print("                      PORCENTAGEM E ESTATISTICAS                     ")
                print("=" * 69)
                print("Total de registros: " + str(total_problemas) + "\n")

                # Grava o título da seção e o total de problemas no arquivo.
                arq_relatorio.write("\n=====================================================================\n")
                arq_relatorio.write("                      PORCENTAGEM E ESTATISTICAS                     \n")
                arq_relatorio.write("=====================================================================\n")
                arq_relatorio.write("Total de registros: " + str(total_problemas) + "\n\n")

                # Exibe e grava a quantidade e a porcentagem de cada tipo.
                print("--- PORCENTAGEM POR TIPO ---")
                arq_relatorio.write("--- PORCENTAGEM POR TIPO ---\n")
                for chave in contagem_tipo:
                    # Recupera quantos problemas pertencem a este tipo.
                    qtd = contagem_tipo[chave]
                    # Calcula a porcentagem e a corta para duas casas decimais.
                    porcentagem = (qtd * 10000 // total_problemas) / 100
                    # Monta a linha com categoria, porcentagem, quantidade e total.
                    linha = str(chave) + ": " + str(porcentagem) + "% (" + str(qtd) + " de " + str(total_problemas) + ")"
                    print(linha)
                    arq_relatorio.write(linha + "\n")

                # Exibe e grava a quantidade e a porcentagem de cada grau.
                print("\n--- PORCENTAGEM POR GRAU ---")
                arq_relatorio.write("\n--- PORCENTAGEM POR GRAU ---\n")
                for chave in contagem_grau:
                    qtd = contagem_grau[chave]
                    porcentagem = (qtd * 10000 // total_problemas) / 100
                    linha = str(chave) + ": " + str(porcentagem) + "% (" + str(qtd) + " de " + str(total_problemas) + ")"
                    print(linha)
                    arq_relatorio.write(linha + "\n")

                # Exibe e grava a quantidade e a porcentagem de cada local.
                print("\n--- PORCENTAGEM POR LOCAL ---")
                arq_relatorio.write("\n--- PORCENTAGEM POR LOCAL ---\n")
                for chave in contagem_local:
                    qtd = contagem_local[chave]
                    porcentagem = (qtd * 10000 // total_problemas) / 100
                    linha = str(chave) + ": " + str(porcentagem) + "% (" + str(qtd) + " de " + str(total_problemas) + ")"
                    print(linha)
                    arq_relatorio.write(linha + "\n")

            # Confirma que o relatório terminou de ser gravado e aguarda antes do menu.
            print("\nRelatorio exportado com sucesso para 'relatorio.txt'!\n")
            time.sleep(3)

# Utilização de IA para testes do código, buscas por erros e sugestões de melhorias e novas estruturas.
# A lógica, organização e estética do código foram desenvolvidas pelos membros.
# Agradecemos a todos pela atenção!
# Atenciosamente, equipe COSMOBYTE!