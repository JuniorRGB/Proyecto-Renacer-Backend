habilidades = []

#habilidades.append("PostgreSQL")
#for habilidad in habilidades:
#    print(habilidad)

#print(len(habilidades))


while True:
    print("\n----Gestor de Habilidades----")
    print("1. Agregar habilidad")
    print("2. Mostrar habilidades")
    print("3. Buscar habilidad")
    print("4. Eliminar habilidad")
    print("5. Salir")

    opcion = input("\nSelecciona una opción (1, 2, 3, 4 o 5): ")

    if opcion == "1":
        habilidad = input("Ingrese la nueva habilidad: ").lower()

        if habilidad not in habilidades: 
            habilidades.append(habilidad)
            print(f"Habilidad '{habilidad}' agregada correctamente.")

        else:
            print(f"La habilidad '{habilidad}' ya existe en la lista.") 
            
    elif opcion == "2":
        if len(habilidades) == 0:
            print("No hay habilidades registradas.")

        else:
            print("\n----Habilidades Registradas----")
            for indice, habilidad in enumerate(habilidades, start=1):
                print(f"{indice}. {habilidad}")

    elif opcion == "3":
        habilidad_a_buscar = input("Ingrese la habilidad a buscar: ").lower()
        if habilidad_a_buscar in habilidades:
            print(f"La habilidad '{habilidad_a_buscar}' se encuentra en la lista.")
        else:
            print(f"La habilidad '{habilidad_a_buscar}' no se encuentra en la lista.")

    elif opcion == "4":
        habilidad_a_eliminar = input("Ingrese la habilidad a eliminar:").lower()
        if habilidad_a_eliminar in habilidades:
            habilidades.remove(habilidad_a_eliminar)
            print(f"la habilidad {habilidad_a_eliminar} ha sido eliminada correctamente.")

        else:
            print(f"La habilidada {habilidad_a_eliminar} no se encuentra en la lista.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, selecciona una opción válida (1, 2, 3, 4 o 5).")




