import json

candidatos = [

    {
        "nombre": "junior",
        "experiencia": 4,
        "ingles": True
    },
    {
        "nombre": "ana",
        "experiencia": 2,
        "ingles": False
    }

]

def guardar_candidatos(candidatos):

    with open("candidatos.json", "w") as archivo:

        json.dump(candidatos, archivo)

#guardar_candidatos(candidatos)

def cargar_candidatos():
    try:

        with open("candidatos.json", "r") as archivo:

            candidatos_cargados = json.load(archivo)
            #print(candidatos_cargados)
            #print(candidatos_cargados[0]["nombre"])
            return candidatos_cargados

    except FileNotFoundError:
        return []


candidatos_cargados = cargar_candidatos()
print(candidatos_cargados)