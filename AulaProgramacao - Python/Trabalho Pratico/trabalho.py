print("\n")
print("========== Desenvlvimento de uma To-Do List ==========")
print("\n")

lista_tarefa: list =  []

while True:
    opcao: str = input('''Digite a opção desejada:
                            \t  \n ¬ 1. Adicionar tarefas - Informe uma descrição sobre a tarefa adicionada
                            \t  \n ¬ 2. Listar tarefas - Exibe todas as tarefas cadastradas
                            \t  \n ¬ 3. Atualizar tarefas - Aqui você pode marcar uma tarefa como concluída ou editar sua descrição
                            \t  \n ¬ 4. Remover tarefas - Aqui você pode excluir uma tarefa cadastrada
                            \n Digite a opção desejada:  ''')
    
    match opcao:
        case "1":
            item: str = input("Informe a tarefa desejada, com descrição: ")
            lista_tarefa.append(item)
            print("\n")
        case "2":
            print('''===== Itens da lista =====
                  \n Os itens da lista atual são: ''')
            for item_da_lista in lista_tarefa:
                print(item_da_lista)
            print("\n")
        case "3":
            print('''===== Atualizar tarefas =====
                  \n Deseja concluir ou editar a tarefa?''')