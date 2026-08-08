nombre = input("¿Cómo te llamas? ")

python = input("¿Sabes programar en Python? (si/no) ").lower()
git = input("¿Sabes usar Git? (si/no) ").lower()
sql = input("¿Sabes usar SQL? (si/no) ").lower()

if python == "si":
    python = True
elif python == "no":
    python = False
else:
    print("Respuesta inválida para Python.")

if git == "si":
    git = True
elif git == "no":
    git = False
else:
    print("Respuesta inválida para Git.")

if sql == "si":
    sql = True
elif sql == "no":
    sql = False
else:
    print("Respuesta inválida para SQL.")

print("\n----- PERFIL -----")
print(f"Nombre: {nombre}")
print(f"Python: {python}")
print(f"Git: {git}")
print(f"SQL: {sql}")

listo_backend = python and git and sql

print(f"¿Está listo para Backend? {listo_backend}")

ingles = input("¿Sabes inglés? (si/no) ").lower()

if ingles == "si":
    ingles = True
elif ingles == "no":
    ingles = False
else:
    print("Respuesta inválida para inglés.")

experiencia_requerida = 3

años_de_experiencia = int(
    input("¿Cuántos años de experiencia tienes en desarrollo backend? ")
)

if años_de_experiencia >= experiencia_requerida and ingles:
    print("¡Felicidades! Cumples con los requisitos para aplicar al puesto de Backend Junior.")

elif años_de_experiencia < experiencia_requerida and ingles:
    print("No cumples con el requisito de experiencia.")

elif años_de_experiencia >= experiencia_requerida and not ingles:
    print("No cumples con el requisito de inglés.")

else:
    print("No cumples con los requisitos de experiencia ni de inglés.")