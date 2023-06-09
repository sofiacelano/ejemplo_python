from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Inicio contadores de respuestas
correctas = 0
incorrectas = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = int(input("resultado: "))
    #Calculamos la cuenta
    if (operator == "+"):
        resultado = number_1 + number_2
    elif(operator == "-"):
        resultado = number_1 - number_2
    elif(operator == "*"):
        resultado = number_1 * number_2
    else:
        resultado = number_1 / number_2
    #Vemos si respondió bien
    if (result == resultado):
        correctas += 1
        print("Respuesta correcta")
    else:
        incorrectas += 1
        print("Respuesta incorrecta")
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
# Mostramos cantidad de respuestas correctas e incorrectas
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Tuviste {correctas} respuestas correctas.")
print(f"\n Tuviste {incorrectas} respuestas incorrectas.")
