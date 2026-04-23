import json
import os
from datetime import datetime
from typing import List, Dict

class TaskManager:
    """Gerenciador de tarefas com persistência em JSON"""
    
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Dict] = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        """Carrega tarefas do arquivo JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self) -> None:
        """Salva tarefas no arquivo JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)
    
    def add_task(self, title: str, description: str = "") -> None:
        """Adiciona uma nova tarefa"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Tarefa '{title}' adicionada com sucesso!")
    
    def list_tasks(self, show_completed: bool = True) -> None:
        """Lista todas as tarefas"""
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
            return
        
        tasks_to_show = self.tasks
        if not show_completed:
            tasks_to_show = [t for t in self.tasks if not t["completed"]]
        
        if not tasks_to_show:
            print("Nenhuma tarefa pendente.")
            return
        
        print("\n" + "="*60)
        print(f"{'ID':<4} {'Status':<8} {'Tarefa':<30} {'Descrição':<15}")
        print("="*60)
        
        for task in tasks_to_show:
            status = "✓ Feita" if task["completed"] else "⏳ Pendente"
            description = task["description"][:15] if task["description"] else "-"
            print(f"{task['id']:<4} {status:<8} {task['title']:<30} {description:<15}")
        
        print("="*60 + "\n")
    
    def mark_completed(self, task_id: int) -> None:
        """Marca uma tarefa como concluída"""
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print(f"Tarefa {task_id} já estava concluída.")
                else:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().isoformat()
                    self.save_tasks()
                    print(f"✓ Tarefa '{task['title']}' marcada como concluída!")
                return
        
        print(f"Tarefa com ID {task_id} não encontrada.")
    
    def remove_task(self, task_id: int) -> None:
        """Remove uma tarefa"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed_task = self.tasks.pop(i)
                # Reorganiza os IDs
                for j, t in enumerate(self.tasks, 1):
                    t["id"] = j
                self.save_tasks()
                print(f"✓ Tarefa '{removed_task['title']}' removida!")
                return
        
        print(f"Tarefa com ID {task_id} não encontrada.")
    
    def get_statistics(self) -> None:
        """Mostra estatísticas das tarefas"""
        if not self.tasks:
            print("Nenhuma tarefa para exibir estatísticas.")
            return
        
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        pending = total - completed
        
        print("\n" + "="*40)
        print("📊 ESTATÍSTICAS")
        print("="*40)
        print(f"Total de tarefas: {total}")
        print(f"Tarefas concluídas: {completed}")
        print(f"Tarefas pendentes: {pending}")
        if total > 0:
            percentage = (completed / total) * 100
            print(f"Progresso: {percentage:.1f}%")
        print("="*40 + "\n")
