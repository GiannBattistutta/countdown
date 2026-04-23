from task_manager_en import TaskManager

def print_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("📝 TASK MANAGER")
    print("="*50)
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Show statistics")
    print("6. Exit")
    print("="*50)

def main():
    """Main program function"""
    manager = TaskManager()
    
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            title = input("Task title: ").strip()
            if not title:
                print("⚠️  Title cannot be empty.")
                continue
            description = input("Description (optional): ").strip()
            manager.add_task(title, description)
        
        elif choice == "2":
            filter_choice = input("Show all tasks? (y/n, default: y): ").strip().lower()
            show_all = filter_choice != "n"
            manager.list_tasks(show_all)
        
        elif choice == "3":
            manager.list_tasks()
            try:
                task_id = int(input("ID of the task to mark as completed: "))
                manager.mark_completed(task_id)
            except ValueError:
                print("⚠️  Invalid ID. Please enter a number.")
        
        elif choice == "4":
            manager.list_tasks()
            try:
                task_id = int(input("ID of the task to remove: "))
                confirm = input(f"Are you sure? (y/n): ").strip().lower()
                if confirm == "y":
                    manager.remove_task(task_id)
            except ValueError:
                print("⚠️  Invalid ID. Please enter a number.")
        
        elif choice == "5":
            manager.get_statistics()
        
        elif choice == "6":
            print("\n👋 Goodbye!")
            break
        
        else:
            print("⚠️  Invalid option. Try again.")

if __name__ == "__main__":
    main()
