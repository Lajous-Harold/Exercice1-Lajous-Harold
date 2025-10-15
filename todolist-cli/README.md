# ToDoList CLI

This project is a command-line interface (CLI) application for managing a ToDo list. It is structured using the Model-View-Controller (MVC) design pattern and follows object-oriented programming principles.

## Project Structure

```
todolist-cli
├── src
│   └── todolist
│       ├── main.py
│       ├── app.py
│       ├── models
│       │   ├── task.py
│       │   └── recurring_task.py
│       ├── controllers
│       │   └── task_controller.py
│       └── views
│           └── cli_view.py
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

Vous pouvez gérer votre ToDoList avec flask avec postman + :

```sh
python src/todolist/app.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
