import argparse





def createTaskPlanner():
    tareas = {} # Inicializa un diccionario vacío para almacenar las tareas
    tarea_id = 0
    prioridades_numericas = {
    "Alta": 3,
    "Media": 2,
    "Baja": 1,
    }


    def addTask(name, tag, priority):
        nonlocal tarea_id
        tarea = {
            "id": tarea_id,
            "name": name,
            "tag": tag,
            "priority": priority,
            "completed": False
        }
        tareas[tarea_id] = tarea
        tarea_id += 1
        return "Tarea agregada: " + name


    def removeTask(delete_id):
        try:
            delete_id = int(delete_id)
            tarea = tareas.pop(delete_id, None)
            if tarea:
                return "Tarea eliminada: " + tarea["name"]
            else:
                return "No se encontró ninguna tarea con el ID proporcionado."
        except ValueError:
            return "El valor debe ser un numero entero."

    
    def markTaskAsCompleted(task_id):
        task_id = int(task_id)
   
        if task_id in tareas:
            tareas[task_id]['completed'] = True
            return f"Tarea {tareas[task_id]['name']} ha sido marcada como Completada."
        else:
            return "No hay tareas con ese ID."
    

    def getPendingTasks():
        no_completed = {tarea_id: task for tarea_id, task in tareas.items() if task["completed"] == False}
        return no_completed
    
      
    def getCompletedTasks():
        completed_task = {tarea_id: task for tarea_id, task in tareas.items() if task["completed"] == True}
        return completed_task


    def list_task():
        return tareas


    def getSortedTasksByPriority():
        prioridades_numericas = {
            "Alta": 1,
            "Media": 2,
            "Baja": 3,
            }
        order_by_priority = sorted(tareas.items(), key=lambda x: prioridades_numericas.get(x[1]["priority"], 0))
        return order_by_priority


    def filterTaskByTag(tags):
        filteredByTag = {tarea_id: task for tarea_id, task in tareas.items() if any(tag in task["tag"] for tag in tags)}
        return filteredByTag



    return {
        "add_task": addTask,
        "listar_tareas": list_task,
        "remover_tareas": removeTask,
        "marcar_completada": markTaskAsCompleted,
        "tareas_no_completadas": getPendingTasks,
        "tareas_completadas": getCompletedTasks,
        "tareas_ordenadas_por_prioridad": getSortedTasksByPriority,
        "tareas_filtradas_por_tags" : filterTaskByTag
    }


closure = createTaskPlanner() # esto crea una instancia de el closure para poder acceder a los metodos como si fuera un diccionario



def main():
    print("¡Bienvenido al Gestor de Tareas!")

    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Agregar tarea")
        print("2. Ver la lista de tareas")
        print("3. Remover Tareas por ID")
        print("4. Marcar La Tarea Completada")
        print("5. Lista de Tareas no Completadas")
        print("6. Lista de Tareas Completadas")
        print("7. Tareas Ordenadas Por Prioridad")
        print("8. Filtrar tareas por Tags")
        print("9. Salir")

        opcion = input("Escoge una accion a realizar: ")

        if opcion == "1":
            name = input("Escribe el nombre de la tarea: ")
            tag = input("Escribe la Etiqueta de la tarea: ")
            priority = input("Escribe la Prioridad de la tarea: ")
            resultado = closure["add_task"](name, tag, priority)
            print(resultado)
        elif opcion == "2":
            tarea = closure["listar_tareas"]()
            if tarea:
                print("\nTareas")
                for tarea_id, tarea in tarea.items():
                    print(f"ID: {tarea_id}, Nombre: {tarea['name']}, Etiqueta: {tarea['tag']}, Prioridad: {tarea['priority']}, Completada: {tarea['completed']}")
            else:
                print("\nNo hay tareas registradas")
        elif opcion == "3":
            deleted_id = input("Por Favor ingresa el Id de la Tarea que desea eliminar: ")
            result = closure["remover_tareas"](deleted_id)
            print(result)
        elif opcion == "4":
            task_id = input("Coloca el ID de la Tarea Que quieres marcar como Completada: ")
            completed = closure["marcar_completada"](task_id)
            print(completed)
        elif opcion == "5":
            no_completed = closure["tareas_no_completadas"]()
            if len(no_completed) <= 0:
                print("No Hay tareas pendientes")
            else:
                print(no_completed)
        elif opcion == "6":
            completed_task = closure["tareas_completadas"]()
            if len(completed_task) <= 0:
                print("No Hay tareas Completadas Aun")
            else:
                print(completed_task)
        elif opcion == "7":
            order_by_priority = closure["tareas_ordenadas_por_prioridad"]()
            for tarea_id, tarea in order_by_priority:
                print(f"ID: {tarea_id}, Nombre: {tarea['name']}, Prioridad: {tarea['priority']}, Completada: {tarea['completed']}")
        elif opcion == "8":
            tags_input = input("Escribe las etiquetas de la tarea (separadas por comas o espacios): ")
            # Divide la entrada en una lista de etiquetas
            tags = [tag.strip().lower() for tag in tags_input.split(',') + tags_input.split()]  # Divide por comas o espacios 
            filtered_by_tag = closure["tareas_filtradas_por_tags"](tags_input)
            if not filtered_by_tag:
                print("No Hay Tareas Con esa Tag")
            else:
                print("Tareas filtradas por etiqueta:")
                for tarea_id, tarea in filtered_by_tag.items():
                    print(f"ID: {tarea_id}, Nombre: {tarea['name']}, Etiqueta: {tarea['tag']}, Prioridad: {tarea['priority']}, Completada: {tarea['completed']}")
        elif opcion == "9":
            print("\nHasta Luego")
            break
        else:
            print("Opcion no valida, por favor elige una opcion valida")


if __name__ == '__main__':
    main()