candidatos = []


def agregar_candidato(candidatos):

    nombre = input(f"Ingrese nombre del candidato: ").lower()

    while not nombre.replace(" ", "").isalpha():
        print("Nombre inválido. Por favor, ingresa un nombre válido.")
        nombre = input(f"Ingrese nombre del candidato:").lower()

    for candidato in candidatos:
         if candidato["nombre"] == nombre:
            print(f"El candidato '{nombre}' ya esta registrado")
            return      

    experiencia = int(input(f"Cuantos años de experiencia tiene? "))
    respuesta_ingles = input(f"Sabes ingles? (Si/No)").lower()

    candidato = {
    "nombre": nombre,
    "experiencia": experiencia,
    "ingles": respuesta_ingles == "si"
                }

    
    candidatos.append(candidato)
    print(f"Candidato agregado correctamente")
        

def mostrar_candidatos(candidatos):

    if len(candidatos) == 0:
         print("No hay candidatos registrados")
         return

    print("\n ------- CANDIDATOS -------")

    for indice, candidato in enumerate(candidatos, start=1):
        print(
        f"{indice}. {candidato["nombre"]} - "
        f"{candidato["experiencia"]} años - "
        f" Ingles: {candidato["ingles"]}"

        )

def buscar_candidato(candidatos):
    candidato_a_buscar = input(f"Ingrese el nombre del candidato a buscar: ").lower()
    for candidato in candidatos:
         
        if candidato["nombre"] == candidato_a_buscar:
            print(f"El candidato: {candidato_a_buscar} se encuentra en nuestra base de datos")
            print(f"Nombre: {candidato["nombre"]}")
            print(f"Experiencia: {candidato["experiencia"]}")
            print(f"Ingles: {candidato["ingles"]}")
            return


    print(f"El candidato: {candidato_a_buscar} no se encuentra en nuestra base de datos")

def eliminar_candidato(candidatos):
    candidato_a_elimincar = input(f"Ingrese el nombre del candidato a eliminar del registro: ").lower()

    for candidato in candidatos:
        if candidato["nombre"] == candidato_a_elimincar:
            candidatos.remove(candidato)
            print(f"El candidato: {candidato_a_elimincar} a sido eliminado")
            return

    print(f"El candidato {candidato_a_elimincar} no se encuentra enn nuestra base de datos")


def cumple_requisito(candidato):
     return candidato["experiencia"] >= 3 and candidato["ingles"]

def evaluar_candidato(candidatos):

    nombre = input("Ingrese el nombre del candidato a evaluar: ").lower()

    for candidato in candidatos:
         if nombre == candidato["nombre"]:

            if cumple_requisito(candidato):
                 print("El candidato cumple los requisitos para Backend")

            else:
                 print("El candidato no cumple con los requisitos")

            return

    print("candidato no encontrado")
 


def Salir():
    print("Saliendo del programa...")


def Ejecutar_programa():
    print(f"Hola, Bienvenido")
    respuesta = input("Desea ingresar al programa? (Si/No) ").lower()

    if respuesta == "si":

        print("Bienvenido al menu")
        
        
        while True:
        
                    print("\n----Gestor de Candidatos----")
                    print("1. Agregar candidato")
                    print("2. Mostrar candidato")
                    print("3. Buscar candidato")
                    print("4. Eliminar candidato")
                    print("5. Evaluar candidato")
                    print("6. Salir")
                    
                    opcion = input("\nSelecciona una opción (1, 2, 3, 4, 5 o 6): ")
        
                    if opcion == "1":
                        agregar_candidato(candidatos)
        
                    elif opcion == "2":
                        mostrar_candidatos(candidatos)
        
                    elif opcion == "3":
                        buscar_candidato(candidatos)
        
                    elif opcion == "4":
                        eliminar_candidato(candidatos)
        
                    elif opcion == "5":
                        evaluar_candidato(candidatos)
                    

                    elif opcion == "6":
                        Salir()
                        break
        
                    else:
                        print("Opción inválida. Por favor, selecciona una opción válida (1, 2, 3, 4, 5 o 6).")
        
        
    elif respuesta == "no":
                print("Gracias por tu tiempo, hasta luego")
        
    else:
                print("Respuesta inválida, por favor ingresa 'si' o 'no'.")
        
Ejecutar_programa()


    