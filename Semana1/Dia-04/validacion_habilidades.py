nombre = input("ingresa tu nombre: ").lower()

while not nombre.replace(" ", "").isalpha():
    print("Nombre inválido. Por favor, ingresa un nombre válido.")
    nombre = input("ingresa tu nombre: ").lower()

respuesta = input("¿Sabes Programar? (si/no) ").lower()

while respuesta != "si" and respuesta != "no":
    print("Respuesta inválida.")
    respuesta = input("¿Sabes Programar? (si/no) ").lower()

print("Respuesta válida:", respuesta)

python = input("¿Sabes programar en Python? (si/no) ").lower()

while python != "si" and python != "no":
    print("Respuesta inválida.")
    python = input("¿Sabes programar en Python? (si/no) ").lower()

print("Respuesta válida:", python)

git = input("¿Sabes usar Git? (si/no) ").lower()

while git != "si" and git != "no":
    print("Respuesta inválida.")
    git = input("¿Sabes usar Git? (si/no) ").lower()

print("Respuesta válida:", git)

sql = input("¿Sabes usar SQL? (si/no) ").lower()

while sql != "si" and sql != "no":
    print("Respuesta inválida.")
    sql = input("¿Sabes usar SQL? (si/no) ").lower()

print("Respuesta válida:", sql)

python = python == "si"
git = git == "si"
sql = sql == "si"

años = int(input("¿Cuántos años de experiencia tienes en desarrollo backend? "))

while años <= 0:
    print("Debes de tener al menos 1 año de experiencia.")
    años = int(input("¿Cuántos años de experiencia tienes en desarrollo backend? "))

print("Respuesta válida:", años)

listo_backend = python and git and sql

while True:

    print("\n1. Mostrar perfil")
    print("2. Validar Backend Junior")
    print("3. Salir")

    opciones = input("Selecciona una opción (1, 2 o 3): ")

    if opciones == "1":
        print("\n----- PERFIL -----")
        print(f"Nombre: {nombre}")
        print(f"Python: {python}")
        print(f"Git: {git}")
        print(f"SQL: {sql}")
        print(f"Años de experiencia: {años}")

    elif opciones == "2":
        if listo_backend and años >= 3:
            print(f"Listo para backend: {listo_backend}")
            print("¡Felicidades! Cumples con los requisitos para aplicar al puesto de Backend Junior.")
        elif not listo_backend:
            print("No cumples con los requisitos de habilidades para Backend Junior.")
        elif años < 3:
            print("No cumples con el requisito de experiencia para Backend Junior, debe ser minimo 3 años.")

    elif opciones == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")


