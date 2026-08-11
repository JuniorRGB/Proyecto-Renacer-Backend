def saludar_usuario():
    print(f" Bienvenido {nombre}")

nombre = input("ingresa tu nombre: ").lower()

saludar_usuario()


def calcular_experiencia(años):
    return años >= 3

experiencia = int(input("Cuantos años de experiencia tienes en desarrollo backend? "))

cumple_experiencia = calcular_experiencia(experiencia)

print(cumple_experiencia)

habilidades = []

def agregar_habilidad(habilidades):
    habilidad = input("Ingrese la nueva habilidad: ").lower()
    
    if habilidad not in habilidades: 
        habilidades.append(habilidad)
        print(f"Habilidad '{habilidad}' agregada correctamente.")

    else:
        print(f"La habilidad '{habilidad}' ya existe en la lista.") 

def mostrar_habilidad(habilidades):
    if len(habilidades) == 0:
        print("No hay habilidades registradas.")
    
    else:
        print("\n----Habilidades Registradas----")
        for indice, habilidad in enumerate(habilidades, start=1):
                print(f"{indice}. {habilidad}")

def buscar_habilidad(habilidades):
    habilidad_a_buscar = input("Ingrese la habilidad a buscar: ").lower()
    if habilidad_a_buscar in habilidades:
        print(f"La habilidad '{habilidad_a_buscar}' se encuentra en la lista.")
    else:
        print(f"La habilidad '{habilidad_a_buscar}' no se encuentra en la lista.")

def eliminar_habilidad(habilidades):
    habilidad_a_eliminar = input("Ingrese la habilidad a eliminar:").lower()
    if habilidad_a_eliminar in habilidades:
        habilidades.remove(habilidad_a_eliminar)
        print(f"la habilidad {habilidad_a_eliminar} ha sido eliminada correctamente.")
    
    else:
        print(f"La habilidad {habilidad_a_eliminar} no se encuentra en la lista.")

def salir():
    print("Saliendo del programa...")
    return True




def Mostrar_menu():
    print(f"Hola {nombre}, bienvenido")
    respuesta = input("Quieres ingresar al menu? (si/no) ").lower()

    if respuesta == "si":
        print("Bienvenido al menu")


        while True:

            print("\n----Gestor de Habilidades----")
            print("1. Agregar habilidad")
            print("2. Mostrar habilidades")
            print("3. Buscar habilidad")
            print("4. Eliminar habilidad")
            print("5. Salir")
            
            opcion = input("\nSelecciona una opción (1, 2, 3, 4 o 5): ")

            if opcion == "1":
                agregar_habilidad(habilidades)

            elif opcion == "2":
                mostrar_habilidad(habilidades)

            elif opcion == "3":
                buscar_habilidad(habilidades)

            elif opcion == "4":
                eliminar_habilidad(habilidades)

            elif opcion == "5":
                salir()
                break

            else:
                print("Opción inválida. Por favor, selecciona una opción válida (1, 2, 3, 4 o 5).")


    elif respuesta == "no":
        print("Gracias por tu tiempo, hasta luego")

    else:
        print("Respuesta inválida, por favor ingresa 'si' o 'no'.")

Mostrar_menu()

