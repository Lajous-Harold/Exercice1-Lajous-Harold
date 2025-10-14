# ToDoList CLI

This project is a command-line interface (CLI) application for managing a ToDo list. It is structured using the Model-View-Controller (MVC) design pattern and follows object-oriented programming principles.

## Project Structure

```
todolist-cli
├── src
│   └── todolist
│       ├── __init__.py
│       ├── main.py
│       ├── models
│       │   ├── __init__.py
│       │   ├── task.py
│       │   └── recurring_task.py
│       ├── controllers
│       │   ├── __init__.py
│       │   └── task_controller.py
│       ├── views
│       │   ├── __init__.py
│       │   └── cli_view.py
│       ├── storage
│       │   ├── __init__.py
│       │   └── json_storage.py
│       └── utils
│           ├── __init__.py
│           └── validators.py
├── tests
│   ├── __init__.py
│   ├── test_task.py
│   └── test_controller.py
├── pyproject.toml
├── setup.cfg
├── requirements.txt
├── .gitignore
└── README.md
```

## Features

- **Task Management**: Add, remove, complete, and list tasks from the command line.
- **MVC Architecture**: Clear separation between models, views (CLI), and controllers.
- **Object-Oriented**: All logic is encapsulated in Python classes.
- **Data Persistence**: Tasks are saved and loaded automatically from a JSON file.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd todolist-cli
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

You can gérer votre ToDoList directement depuis le terminal avec les commandes suivantes :

```sh
# Ajouter une tâche
python src/todolist/main.py add "Titre de la tâche" "Description optionnelle"

# Lister toutes les tâches
python src/todolist/main.py list

# Supprimer une tâche (par son numéro)
python src/todolist/main.py remove <id>

# Marquer une tâche comme complétée
python src/todolist/main.py complete <id>

# Afficher l'aide
python src/todolist/main.py help
```

Les tâches sont sauvegardées dans un fichier `tasks.json` à la racine du projet.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
