from task_manager import TaskManager

def print_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("📝 GERENCIADOR DE TAREFAS")
    print("="*50)
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Ver estatísticas")
    print("6. Sair")
    print("="*50)

def main():
    """Função principal do programa"""
    manager = TaskManager()
    
    while True:
        print_menu()
        choice = input("Escolha uma opção (1-6): ").strip()
        
        if choice == "1":
            title = input("Título da tarefa: ").strip()
            if not title:
                print("⚠️  Título não pode estar vazio.")
                continue
            description = input("Descrição (opcional): ").strip()
            manager.add_task(title, description)
        
        elif choice == "2":
            filter_choice = input("Mostrar todas as tarefas? (s/n, padrão: s): ").strip().lower()
            show_all = filter_choice != "n"
            manager.list_tasks(show_all)
        
        elif choice == "3":
            manager.list_tasks()
            try:
                task_id = int(input("ID da tarefa a marcar como concluída: "))
                manager.mark_completed(task_id)
            except ValueError:
                print("⚠️  ID inválido. Digite um número.")
        
        elif choice == "4":
            manager.list_tasks()
            try:
                task_id = int(input("ID da tarefa a remover: "))
                confirm = input(f"Tem certeza? (s/n): ").strip().lower()
                if confirm == "s":
                    manager.remove_task(task_id)
            except ValueError:
                print("⚠️  ID inválido. Digite um número.")
        
        elif choice == "5":
            manager.get_statistics()
        
        elif choice == "6":
            print("\n👋 Até logo!")
            break
        
        else:
            print("⚠️  Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
