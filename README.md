# Task Tracker CLI

## 📋 Descripción

**Task Tracker CLI** es una aplicación de línea de comandos (CLI) sencilla para ayudarte a gestionar tus tareas. Permite seguir aquellas tareas que necesitas hacer, las que estás trabajando actualmente y las que ya has completado.

El objetivo principal de este proyecto es poner en practica y demostrar habilidades de backend tales como la implementación de lógica, manejo de archivos, validación de datos, y programación modular, sin depender de ningún tipo de framework o herramienta externa.

## 🛠️ Tecnologías

Para el desarrollo de esta aplicación de línea de comandos (CLI) se ha utilizado Python y modulos nativos de dicho lenguaje de programación.

## 🚀 Características principales

- **Añadir, actualizar y eliminar tareas**: Gestión completa del ciclo de vida de cada tarea de manera confiable y eficiente.
- **Marcar tareas como en progreso o completadas**: Permite un seguimiento claro del estado de cada actividad, optimizando la organización y priorización del trabajo.
- **Listar tareas por estado**: Filtrado inteligente por todo, in-progress, done o todas las tareas, facilitando el control y la planificación.
- **Las tareas se almacenan en un archivo JSON en el directorio actual**: Persistencia de datos simple y transparente, asegurando portabilidad y trazabilidad de las tareas.
- **Manejar errores de manera robusta**: Validación de entradas y control de errores para evitar fallos y así garantizar una experiencia confiable para el usuario.

## ⚙️ Como usar el sistema

1. Clonar el repositorio

```bash
git clone https://github.com/DrBayo01/Task-Tracker-CLI.git
cd task-tracker-cli
```

2. Ejecutar la aplicación desde la linea de comandos

```bash
# Agregar una tarea
python task_cli.py add "Comprar alimentos"

# Actualizar una tarea existente
python task_cli.py update 1 "Comprar alimentos y cocinar la cena"

# Eliminar una tarea
python task_cli.py delete 1

# Cambiar estado de las tareas
python task_cli.py mark-in-progress 1 # en progreso
python task_cli.py mark-done 1 # hecha, terminada

# Listar tareas
python task_cli.py list # <-- listar todas las tareas
python task_cli.py list done # <-- listar las tareas con el estado "done" (hechas, terminadas)
python task_cli.py list todo # <-- listar las tareas con el estado "todo" (por hacer)
python task_cli.py list in-progress # <-- listar las tareas con el estado "in-progress" (en progreso)
```
