
print("\n")
print("========== Desenvlvimento de uma To-Do List ==========")
print("\n")
lista_tarefa: list =  []

while True:
    opcao: str = input('''Opções:
                            \t  \n Adicionar tarefas - Informe uma descrição sobre a tarefa adicionada
                            \t  \n Listar tarefas - Exibe todas as tarefas cadastradas
                            \t  \n Atualizar tarefas - Aqui você pode marcar uma tarefa como concluída ou editar sua descrição
                            \t  \n Remover tarefas - Aqui você pode excluir uma tarefa cadastrada
                            \t  \n Encerra o programa - Digite "X" caso queira fechar o programa e encerrar sua operação
                            \n Digite a opção desejada:  ''')
    
    
    match opcao:
        case "Adicionar":
            item: str = input("Informe a tarefa desejada: ")
            desc: str = input("Informe a descrição - Pendente ou Concluída: ")
            lista_tarefa.append(item)
            lista_tarefa.append(desc)
            print("\n")
        case "Listar":
            print('''===== Itens da lista =====
                  \n Os itens da lista atual são: ''')
            for item_da_lista in lista_tarefa:
                print(item_da_lista)
            print("\n")
        case "Atualizar":
            print('''===== Atualizar tarefas =====''')
            att: str = input("Qual tarefa deseja atualizar? ")
            print("\n")
            input("Deseja concluir ou editar a tarefa? ")
            if "concluir" :
                desc == "Concluída"
                print("Tarefa Concluída.")
            elif "editar":
                nova_desc: str = input("Digite a nova descrição: ")
                desc = nova_desc
                print("Tarefa editada.")
            else:
                print("Opção inválida.")
        case "Remover":
            print('''===== Remover tarefas =====''')
            item_excluido: str = input("Informe a tarefa a ser excluída: ")
            lista_tarefa.remove(item_excluido)
            print("\n")
        case "Encerrar":
            print("===== Programa Encerrado =====")
            break