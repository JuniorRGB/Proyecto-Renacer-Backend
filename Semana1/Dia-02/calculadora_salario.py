nombre = input("¿Cómo te llamas?")
salario_actual = int(input("¿Cuál es tu salario actual?"))
salario_deseado = int(input("¿Cuál es tu salario deseado?"))


if salario_actual == 0:
    print("Tu salario actual es 0, no es posible calcular un aumento.")

elif salario_deseado > salario_actual:
    diferencia = salario_deseado - salario_actual
    porcentaje = (diferencia / salario_actual) * 100
    años = int(input("En cuantos años deseas alcanzar ese salario deseado?"))

    if años <= 0:
        print('Los años deben ser mayores a 0 para poder calcular el aumento anual.')

    else:

        salario_anual = diferencia / años
        print("\n ----Resultado----")
        print(f"Hola {nombre}.")
        print(f"Tu salario actual es de RD$: {salario_actual:,}")
        print(f"Tu salario deseado es de RD$: {salario_deseado:,}")
        print(f"La diferencia entre tu salario actual y el deseado es de RD$: {diferencia:,}")
        print(f"Eso representa un aumento del: {porcentaje:.2f}%")
        print(f"Por lo tanto, debes de aumentar tu salario en RD$: {salario_anual:.2f} cada año durante {años} años para alcanzar tu salario deseado.")

elif salario_actual == salario_deseado:
    print("Ya tienes el salario deseado, no es necesario un aumento.")

else:
    print("Tu salario actual es mayor que el salario deseado, no es necesario un aumento.")

