import json
from pathlib import Path
ruta_base = Path(__file__).parent
ruta_json = ruta_base / "candidatos.json"


def cargar_candidatos():
    try:

        with open(ruta_json, "r") as archivo:

            candidatos_cargados = json.load(archivo)
            #print(candidatos_cargados)
            #print(candidatos_cargados[0]["nombre"])
            return candidatos_cargados

    except (FileNotFoundError, json.JSONDecodeError):
        return []


candidatos = cargar_candidatos()

def pedir_experiecia():

     while True:
                       
                 try:
                     experiencia = int(input(f"Cuantos años de experiencia tiene? "))
                     if experiencia >= 0:
                        return experiencia
                         
     
                     else:
                         print("Valor no valido")
     
                 except ValueError:
                     print("Debes introducir un numero")

def pedir_nombre():

         
        nombre = input(f"Ingrese nombre del candidato: ").lower()
     
        while not nombre.replace(" ", "").isalpha():
             print("Nombre inválido. Por favor, ingresa un nombre válido.")
             nombre = input(f"Ingrese nombre del candidato:").lower()
        return nombre

def pedir_ingles():

     respuesta_ingles = input(f"Sabes ingles? (Si/No)").lower()

     while True:
          
          if respuesta_ingles == "si":
               return respuesta_ingles

          elif respuesta_ingles =="no":
               return  respuesta_ingles

          else:
               print("Opcion no valida")
               respuesta_ingles = input(f"Sabes ingles? (Si/No)").lower()


def encontrar_candidato(candidatos, nombre):


        for candidato in candidatos:
             
            if candidato["nombre"] == nombre:
                return candidato

        return None


def actualizar_candidato(candidatos):
    nombre = pedir_nombre()
    candidato_encontrado = encontrar_candidato(candidatos, nombre)

    if candidato_encontrado is not None:
            print("Candidato encontrado")
            candidato_encontrado["experiencia"] = pedir_experiecia()
            candidato_encontrado["ingles"] = pedir_ingles() == "si"
            guardar_candidatos(candidatos)
            print("Candidato actualizado correctamente")



    else:
            print(f"Candidato {nombre} no encontrado")


def agregar_candidato(candidatos):

    nombre = pedir_nombre()

    for candidato in candidatos:
         if candidato["nombre"] == nombre:
            print(f"El candidato '{nombre}' ya esta registrado")
            return

    
                  
    experiencia = pedir_experiecia()  
    respuesta_ingles = pedir_ingles()

    candidato = {
    "nombre": nombre,
    "experiencia": experiencia,
    "ingles": respuesta_ingles == "si"
                }

    
    candidatos.append(candidato)
    guardar_candidatos(candidatos)
    print(f"Candidato agregado correctamente")

def guardar_candidatos(candidatos):

    with open(ruta_json, "w") as archivo:

        json.dump(candidatos, archivo)

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

    nombre = pedir_nombre()
    candidato_a_buscar = encontrar_candidato(candidatos, nombre)

    if candidato_a_buscar:
            print(f"El candidato: {nombre} se encuentra en nuestra base de datos")
            print(f"Nombre: {candidato_a_buscar["nombre"]}")
            print(f"Experiencia: {candidato_a_buscar["experiencia"]}")
            print(f"Ingles: {candidato_a_buscar["ingles"]}")

    else:
        print(f"El candidato: {nombre} no se encuentra en nuestra base de datos")



def eliminar_candidato(candidatos):
    candidato_a_elimincar = pedir_nombre()
    candidato_encontrado = encontrar_candidato(candidatos, candidato_a_elimincar)

    if candidato_encontrado:
            candidatos.remove(candidato_encontrado)   
            guardar_candidatos(candidatos)
            print(f"El candidato: {candidato_a_elimincar} ha sido eliminado")
            return

    else: 
        print(f"El candidato {candidato_a_elimincar} no se encuentra en nuestra base de datos")

def cumple_requisito(candidato):
     return candidato["experiencia"] >= 3 and candidato["ingles"]

def evaluar_candidato(candidatos):

    nombre = pedir_nombre()
    candidato_encontrado = encontrar_candidato(candidatos, nombre)

    if candidato_encontrado:

            if cumple_requisito(candidato_encontrado):
                 print("El candidato cumple los requisitos para Backend")

            else:
                 print("El candidato no cumple con los requisitos")

            return
    else:
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
                    print("6. Actualizar candidato")
                    print("7. Salir")
                    
                    opcion = input("\nSelecciona una opción (1, 2, 3, 4, 5, 6 o 7): ")
        
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
                         actualizar_candidato(candidatos)
                    

                    elif opcion == "7":
                        Salir()
                        break
        
                    else:
                        print("Opción inválida. Por favor, selecciona una opción válida (1, 2, 3, 4, 5, 6 o 7).")
        
        
    elif respuesta == "no":
                print("Gracias por tu tiempo, hasta luego")
        
    else:
                print("Respuesta inválida, por favor ingresa 'si' o 'no'.")
        
Ejecutar_programa()