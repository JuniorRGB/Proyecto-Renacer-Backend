import json

candidato = {

    "nombre": "junior",
    "experiencia": 4,
    "ingles": True

}

with open("candidato.json", "w") as archivo:

    json.dump(candidato, archivo)

with open("candidato.json", "r") as archivo:

    datos = json.load(archivo)
print(datos)
print(datos["nombre"])
