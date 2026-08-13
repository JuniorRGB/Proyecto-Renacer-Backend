#candidato = {
#
#    "Nombre": "Junior",
#    "Edad": 27,
#    "Experiencia": 3,
#    "Ingles": True,
#    "Rol": "SEO Specialist"
#}

candidatos = [
    {
        "nombre": "Junior",
        "experiencia": 3,
        "ingles": True
    },
    {
        "nombre": "Carlos",
        "experiencia": 1,
        "ingles": False
    },
    {
        "nombre": "Ana",
        "experiencia": 4,
        "ingles": True
    }
]


#print(f"nombre: {candidatos["nombre"]}")
#print(f"experiencia: {candidatos["experiencia"]} años")

#candidatos["rol"] = "Backend Developer"

#print(candidatos["rol"])

#candidatos["sql"] = True

#print(candidatos.get("nombre"))
#print(candidatos.get("postgresql"))

#for clave, valor in candidatos.items():
#    print(f"{clave}: {valor}")

for candidato in candidatos:
    print(
        f"{candidato['nombre']} - "
        f"{candidato['experiencia']} años"
        )