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
    else:
        complete_description = " ".join(sys.argv[2:])
        if not os.path.exists("to-do-list.json"):
            task_properties = [add_task("1", complete_description)]
            y = json.dumps(task_properties, indent=4)
            with open("to-do-list.json", "w") as f:
                f.write(y)
            print(f"Task added successfully (ID: 1)")
        else:
            with open("to-do-list.json", "r") as f:
                data = json.load(f)
                if data == []: # If the file is empty but it exists/ Si el archivo está vacío pero existe
                    new_id = "1"
                    task_properties = add_task(new_id, complete_description)
                    data.append(task_properties)
                    y = json.dumps(data, indent=4)
                    with open("to-do-list.json", "w") as f:
                        f.write(y)
                    print(f"Task added successfully (ID: {new_id})")
                    sys.exit(0)
                else:
                    task_list = []
                    for task in data:
                        task_id = int(task["id"])
                        task_list.append(task_id)
                    new_id = str(max(task_list) + 1)
                    task_properties = add_task(new_id, complete_description)
                    data.append(task_properties)
                    y = json.dumps(data, indent=4)
                with open("to-do-list.json", "w") as f:
                    f.write(y)
                print(f"Task added successfully (ID: {new_id})")

elif sys.argv[1] == "update": # Update a new task / Actualizar una tarea
    if len(sys.argv) < 4:
        error_message("Update command requires a valid task ID and a new description.") # El comando Update requiere un ID de tarea valido y una nueva descripción.
    else:
        with open("to-do-list.json", "r") as f:
            data = list(json.load(f))
            task_found = False
            for task in data:
                if task["id"] == sys.argv[2]:
                    new_description = " ".join(sys.argv[3:])
                    task["description"] = new_description
                    task["UpdatedAt"] = datetime.datetime.now().isoformat() + "Z"
                    print(f"Task updated successfully (ID: {sys.argv[2]})")
                    task_found = True
                    y = json.dumps(data, indent=4)
                    with open("to-do-list.json", "w") as f:
                        f.write(y)
                    break
            if not task_found:
                error_message(f"Task with ID {sys.argv[2]} not found.")    

elif sys.argv[1] == "delete": # Delete a task / Eliminar una tarea
    if len(sys.argv) < 3:
        error_message("Delete command requires a valid task ID.") # El comando Delete requiere un ID de tarea valido.
    elif len(sys.argv) > 3:
        error_message("Delete command only requires a valid task ID") # El comando Delete requiere solo un ID de tarea valido.
    else:
        with open("to-do-list.json", "r") as f:
            data = list(json.load(f))
            task_found = False
            for task in data:
                if task["id"] == sys.argv[2]:
                    data.remove(task)
                    print(f"Task deleted successfully (ID: {sys.argv[2]})")
                    task_found = True
                    y = json.dumps(data, indent=4)
                    with open("to-do-list.json", "w") as f:
                        f.write(y)
                    break
            if not task_found:
                error_message(f"Task with ID {sys.argv[2]} not found.")

elif sys.argv[1] == "mark-in-progress":
    if len(sys.argv) < 3:
        error_message("This command requires a valid task ID.") # Este comando requiere un ID de tarea valido.
    elif len(sys.argv) > 3:
        error_message("This command only requires a valid task ID.") # Este comando solo requiere un ID de tarea valido.
    else:
        with open("to-do-list.json", "r") as f:
            data = list(json.load(f))
            task_found = False
            for task in data:
                if task["id"] == sys.argv[2]:
                    task["status"] = "in-progress"
                    task["UpdatedAt"] = datetime.datetime.now().isoformat() + "Z"
                    print(f"Task marked as in-progress (ID: {sys.argv[2]})")
                    task_found = True
                    y = json.dumps(data, indent=4)
                    with open("to-do-list.json", "w") as f:
                        f.write(y)
                    break
            if not task_found:
                error_message(f"Task with ID {sys.argv[2]} not found.")

elif sys.argv[1] == "mark-done":
    if len(sys.argv) < 3:
        error_message("This command requires a valid task ID.") # Este comando requiere un ID de tarea valido.
    elif len(sys.argv) > 3:
        error_message("This command only requires a valid task ID.") # Este comando solo requiere un ID de tarea valido.
    else:
        with open("to-do-list.json", "r") as f:
            data = list(json.load(f))
            task_found = False
            for task in data:
                if task["id"] == sys.argv[2]:
                    task["status"] = "done"
                    task["UpdatedAt"] = datetime.datetime.now().isoformat() + "Z"
                    print(f"Task marked as done (ID: {sys.argv[2]})")
                    task_found = True
                    y = json.dumps(data, indent=4)
                    with open("to-do-list.json", "w") as f:
                        f.write(y)
                    break
            if not task_found:
                error_message(f"Task with ID {sys.argv[2]} not found.")

elif sys.argv[1] == "list": # List tasks / Listar tareas
    if len(sys.argv) > 2:
        if sys.argv[2] == "done":
            with open("to-do-list.json", "r") as f:
                data = list(json.load(f))
                filtered_tasks = [task for task in data if task["status"] == "done"]
                if filtered_tasks == []:
                    print("No completed tasks found.") # No se encontraron tareas completadas.
                else:
                    print("\nCompleted tasks:")
                    for task in filtered_tasks:
                        print(f"\nID: {task['id']}")
                        print(f"Description: {task['description']}")
                        print(f"Status: {task['status']}")
                        print(f"CreatedAt: {task['CreatedAt']}")
                        print(f"UpdatedAt: {task['UpdatedAt']}\n")
                        print("-" * 20)
        elif sys.argv[2] == "todo": # List only to-do tasks / Listar solo tareas por hacer
            with open("to-do-list.json", "r") as f:
                data = list(json.load(f))
                filtered_tasks = [task for task in data if task["status"] == "todo"]
                if filtered_tasks == []:
                    print("No to-do tasks found.") # No se encontraron tareas por hacer.
                else:
                    print("\nTo-do tasks:")
                    for task in filtered_tasks:
                        print(f"\nID: {task['id']}")
                        print(f"Description: {task['description']}")
                        print(f"Status: {task['status']}")
                        print(f"CreatedAt: {task['CreatedAt']}")
                        print(f"UpdatedAt: {task['UpdatedAt']}\n")
                        print("-" * 20)

        elif sys.argv[2] == "in-progress": # List only in-progress tasks / Listar solo tareas en progreso
            with open("to-do-list.json", "r") as f:
                data = list(json.load(f))
                filtered_tasks = [task for task in data if task["status"] == "in-progress"]
                if filtered_tasks == []:
                    print("No In progress tasks found.") # No se encontraron tareas en progreso.
                else:
                    print("\n In progress tasks:")
                    for task in filtered_tasks:
                        print(f"\nID: {task['id']}")
                        print(f"Description: {task['description']}")
                        print(f"Status: {task['status']}")
                        print(f"CreatedAt: {task['CreatedAt']}")
                        print(f"UpdatedAt: {task['UpdatedAt']}\n")
                        print("-" * 20)
        else:
            error_message("Unknown filter. Use 'done', 'todo', or 'in-progress'.") # Filtro desconocido. Usa 'done', 'todo' o 'in-progress'.
    else:
        with open("to-do-list.json", "r") as f:
            data = list(json.load(f))
            if data == []:
                print("No tasks found.") # No se encontraron tareas.
            else:
                print("\nAll tasks:")
                for task in data:
                    print(f"\nID: {task['id']}")
                    print(f"Description: {task['description']}")
                    print(f"Status: {task['status']}")
                    print(f"CreatedAt: {task['CreatedAt']}")
                    print(f"UpdatedAt: {task['UpdatedAt']}\n")
                    print("-" * 20)
else:
    print("Unknown command.") # Comando desconocido.