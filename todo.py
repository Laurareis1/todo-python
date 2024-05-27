import tasks

def main():
    tasks.load_tasks()
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == '1':
            task = input("Digite a descrição da tarefa: ")
            tasks.add_task(task)
        elif choice == '2':
            tasks.list_tasks()
        elif choice == '3':
            task_id = int(input("Digite o ID da tarefa concluída: "))
            tasks.complete_task(task_id)
        elif choice == '4':
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
