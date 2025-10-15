""" Importation des modules Flask nécessaires """
from flask import Flask, request, jsonify

""" Importation du controleur TaskController """
from controllers.task_controller import TaskController

app = Flask(__name__)
controller = TaskController() 

@app.route('/tasks', methods=['GET'])
def get_tasks():  # Récupérer toutes les tasks
    tasks = controller.list_tasks()
    if not tasks:
        return jsonify({"message": "Aucune tâche dans la liste."})
    payload = [
        {
            "title": t.title,
            "description": getattr(t, "description", None),
            "completed": getattr(t, "completed", False),
        }
        for t in tasks
    ]
    return jsonify(payload)

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json or {}
    title = data.get('title')
    description = data.get('description', None)
    if not title:
        return jsonify({"error": "Le titre est requis."}), 400
    controller.add_task(title, description or "")
    return jsonify({"message": "Tâche ajoutée !"})

@app.route('/delete-task/<int:idx>', methods=['DELETE'])
def delete_task(idx):
    # idx 1-based côté API → 0-based côté contrôleur
    ok = controller.remove_task(idx - 1)
    if not ok:
        return jsonify({"error": "Index de tâche invalide."}), 400
    return jsonify({"message": "Tâche supprimée !"})

@app.route('/mark-as-completed/<int:idx>', methods=['PUT'])
def mark_as_completed(idx):
    ok = controller.complete_task(idx - 1)
    if not ok:
        return jsonify({"error": "Index de tâche invalide."}), 400
    return jsonify({"message": "Tâche marquée comme complétée !"})

if __name__ == "__main__":
    app.run(debug=True)
