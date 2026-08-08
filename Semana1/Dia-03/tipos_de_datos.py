#nombre = "Junior"
#edad = 27
#salario = 55000
#promedio = 9.5
#backend = True

#print(type(nombre))
#print(type(edad))
#print(type(salario))
#print(type(promedio))
#print(type(backend))


edad = "27"

print(type(edad))

edad = int(edad)

print(type(edad))

salario_actual = 55000
salario_deseado = 90000

print(salario_deseado > salario_actual)
print(salario_actual > salario_deseado)
print(salario_actual == salario_deseado)
print(salario_actual != salario_deseado)
print(salario_actual >= 55000)
print(salario_actual <= 55000)


tiene_python = True
tiene_git = True
tiene_sql = False

print(tiene_python and tiene_git)

print(tiene_python and tiene_sql)

print(tiene_python or tiene_sql)

print(not tiene_sql)


nombre = input("¿Cómo te llamas?")
python = input("¿Sabes programar en Python? (si/no)")
git = input("¿Sabes usar Git? (si/no)")
sql = input("¿Sabes usar SQL? (si/no)")

if python == 'si' and git == 'si' and sql == 'si':
    python = True
    git = True
    sql = True

    print("\n ----Perfil----")
    print(f"Nombre: {nombre}")
    print(f"Python: {python}")
    print(f"Git: {git}")
    print(f"SQL: {sql}")
    print("¿Está listo para Backend?")
    print(python and git and sql)

elif python == 'si' and git == 'si' and sql == 'no':
    python = True
    git = True
    sql = False

    print("\n ----Perfil----")
    print(f"Nombre: {nombre}")
    print(f"Python: {python}")
    print(f"Git: {git}")
    print(f"SQL: {sql}")
    print("¿Está listo para Backend?")
    print(python and git and sql)
    
elif python == 'si' and git == 'no' and sql == 'si':
    python = True
    git = False
    sql = True

    print("\n ----Perfil----")
    print(f"Nombre: {nombre}")
    print(f"Python: {python}")
    print(f"Git: {git}")
    print(f"SQL: {sql}")
    print("¿Está listo para Backend?")
    print(python and git and sql)

elif python == 'no' and git == 'si' and sql == 'si':
    python = False
    git = True
    sql = True

    print("\n ----Perfil----")
    print(f"Nombre: {nombre}")
    print(f"Python: {python}")
    print(f"Git: {git}")
    print(f"SQL: {sql}")
    print("¿Está listo para Backend?")
    print(python and git and sql)

elif python == 'si' and git == 'no' and sql == 'no':
    python = True
    git = False
    sql = False

    print("\n ----Perfil----")
    print(f"Nombre: {nombre}")
    print(f"Python: {python}")
    print(f"Git: {git}")
    print(f"SQL: {sql}")
    print("¿Está listo para Backend?")
    print(python and git and sql)

elif python == 'no' and git == 'si' and sql == 'no':
    python = False
    git = True
    sql = False

    print("\n ----Perfil----")
    print(f"Nombre: {nombre}")
    print(f"Python: {python}")
    print(f"Git: {git}")
    print(f"SQL: {sql}")
    print("¿Está listo para Backend?")
    print(python and git and sql)

elif python == 'no' and git == 'no' and sql == 'si':
    python = False
    git = False
    sql = True

    print("\n ----Perfil----")
    print(f"Nombre: {nombre}")
    print(f"Python: {python}")
    print(f"Git: {git}")
    print(f"SQL: {sql}")
    print("¿Está listo para Backend?")
    print(python and git and sql)
    
elif python == 'no' and git == 'no' and sql == 'no':
    python = False
    git = False
    sql = False

    print("\n ----Perfil----")
    print(f"Nombre: {nombre}")
    print(f"Python: {python}")
    print(f"Git: {git}")
    print(f"SQL: {sql}")
    print("¿Está listo para Backend?")
    print(python and git and sql)

else:
    print("Por favor, responde con 'si' o 'no' para cada pregunta sobre tus habilidades.")


ingles = input("¿Sabes inglés? (si/no)")

if ingles == 'si':
    ingles = True
    backend_junior = python and git and ingles
    print(backend_junior)

elif ingles == 'no':
    ingles = False
    backend_junior = python and git and ingles
    print(backend_junior)

else:
    print("Por favor, responde con 'si' o 'no' para indicar si sabes inglés.")

experiencia = 3

puede_aplicar = int(input("¿Cuántos años de experiencia tienes en desarrollo backend?"))

if puede_aplicar >= experiencia and ingles == True:
    print("¡Felicidades! Cumples con los requisitos para aplicar al puesto de Backend Junior.") 

elif puede_aplicar < experiencia and ingles == True:
    print("Lo siento, no cumples con los requisitos de experiencia para aplicar al puesto de Backend Junior.")

elif puede_aplicar >= experiencia and ingles == False:
    print("Lo siento, no cumples con el requisito de inglés para aplicar al puesto de Backend Junior.")

elif puede_aplicar < experiencia and ingles == False:
    print("Lo siento, no cumples con los requisitos de experiencia y de inglés para aplicar al puesto de Backend Junior.")

else:
    print("Por favor, responde con 'si' o 'no' para cada pregunta sobre tus habilidades.")