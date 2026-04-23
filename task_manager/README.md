# 📝 Gerenciador de Tarefas

Um projeto simples de terminal em Python que demonstra conceitos de programação importantes como lógica, organização de código e manipulação de arquivos.

## 🎯 Funcionalidades

- ✅ **Adicionar tarefa** - Crie novas tarefas com título e descrição
- 📋 **Listar tarefas** - Veja todas as tarefas ou apenas as pendentes
- ✓ **Marcar como concluída** - Complete suas tarefas
- 🗑️ **Remover tarefa** - Delete tarefas
- 💾 **Persistência em JSON** - As tarefas são salvas automaticamente em `tasks.json`
- 📊 **Estatísticas** - Veja seu progresso

## 📂 Estrutura do Projeto

```
task_manager/
├── main.py              # Interface de linha de comando
├── task_manager.py      # Lógica principal do gerenciador
├── tasks.json           # Arquivo de dados (criado automaticamente)
└── README.md            # Este arquivo
```

## 🚀 Como Usar

### 1. Executar o programa

```bash
cd task_manager
python main.py
```

### 2. Menu de opções

O programa apresenta um menu simples com as seguintes opções:

```
1. Adicionar tarefa        - Crie uma nova tarefa
2. Listar tarefas          - Veja todas as suas tarefas
3. Marcar como concluída   - Marque uma tarefa como feita
4. Remover tarefa          - Delete uma tarefa
5. Ver estatísticas        - Veja seu progresso
6. Sair                    - Saia do programa
```

## 💾 Formato do Arquivo JSON

As tarefas são salvas em `tasks.json` com a seguinte estrutura:

```json
[
  {
    "id": 1,
    "title": "Estudar Python",
    "description": "Aprender sobre classes e módulos",
    "completed": false,
    "created_at": "2026-04-21T10:30:45.123456",
    "completed_at": null
  }
]
```

## 🧠 Conceitos Demonstrados

Este projeto mostra os seguintes conceitos de programação:

1. **Orientação a Objetos** - Classe `TaskManager`
2. **Manipulação de Arquivos** - Leitura e escrita em JSON
3. **Estruturas de Dados** - Listas e dicionários
4. **Entrada/Saída** - Interface com o usuário
5. **Tratamento de Erros** - Validação de entrada
6. **Type Hints** - Anotações de tipos
7. **Organização de Código** - Separação de responsabilidades

## 📝 Exemplo de Uso

```
1. Adicionar tarefa
   → Título: Fazer compras
   → Descrição: Comprar leite e pão

2. Adicionar tarefa
   → Título: Estudar Python
   → Descrição: Capítulo 5

3. Listar tarefas
   → Mostra ambas as tarefas

4. Marcar como concluída
   → ID: 1
   → Tarefa "Fazer compras" marcada como concluída

5. Ver estatísticas
   → Total: 2, Concluídas: 1, Pendentes: 1, Progresso: 50%
```

## 🔧 Requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa necessária (apenas stdlib)

## 📚 Melhorias Possíveis

- Adicionar categorias ou tags nas tarefas
- Implementar prioridades
- Adicionar datas de vencimento
- Criar interface com GUI usando tkinter
- Adicionar testes unitários
- Implementar busca e filtros mais avançados
