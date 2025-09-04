import sys
import json
import os
import pathlib
import datetime

# Function to add a new task / Función para añadir una nueva tarea
def add_task(id, description):
    return {"id": id,
            "description": description,
            "status": "todo",
            "CreatedAt": datetime.datetime.now().isoformat() + "Z",
            "UpdatedAt": None
    }

# Error handling function / Función de manejo de errores
def error_message(error):
    print(f"ERROR: {error}")
    sys.exit(1)

if len(sys.argv) < 2:
    error_message("At least one argument is required.")
elif sys.argv[1] == "add": # Add a new task / Añadir una nueva tarea
    if len(sys.argv) == 1:
        error_message("Add command requires at least one argument.") # El comando Add requiere al menos un argumento.
    elif len(sys.argv) < 3:
        error_message("The task description is mandatory.") # La descripción de la tarea es obligatoria.
    elif len(sys.argv) > 3:
        error_message("Add command only accepts a description as its sole argument.") # El comando Add solo acepta una descripción como su único argumento.
    else:
        if not os.path.exists("to-do-list.json"):
            task_properties = [add_task("1", sys.argv[2])]
            y = json.dumps(task_properties, indent=4)
            with open("to-do-list.json", "w") as f:
                f.write(y)
            print(f"Task added successfully (ID: 1)")
        else:
            with open("to-do-list.json", "r") as f:
                data = json.load(f)
                task_list = []
                for task in data:
                    task_id = int(task["id"])
                    task_list.append(task_id)
                new_id = str(max(task_list) + 1)
                task_properties = add_task(new_id, sys.argv[2])
                data.append(task_properties)
                y = json.dumps(data, indent=4)
            with open("to-do-list.json", "w") as f:
                f.write(y)
            print(f"Task added successfully (ID: {new_id})")

elif sys.argv[1] == "update":
    print("Se ha eliminado la tarea llamada." + sys.argv[2])
elif sys.argv[1] == "delete":
    print("Mostrando todas las tareas.")
elif sys.argv[1] == "mark-in-progress":
    print("Marcando la tarea como en progreso." + sys.argv[2])
elif sys.argv[1] == "mark-done":
    print("Marcando la tarea como completada." + sys.argv[2])
elif sys.argv[1] == "list":
    if len(sys.argv) == 3:
        if sys.argv[2] == "done":
            print("Mostrando tareas completadas")
        elif sys.argv[2] == "todo":
            print("Mostrando tareas por hacer")
        elif sys.argv[2] == "in-progress":
            print("Mostrando tareas en progreso")
    else:
        print("Mostrando todas las tareas.")
else:
    print("Comando no reconocido.")