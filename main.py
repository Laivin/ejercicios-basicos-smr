def pedir_nombre():
    nombre = input("Introduce tu nombre: ")
    return nombre

def suma():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 + num2
    return resultado

def area_rectangulo():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    area = base * altura
    return area

def conversor_celsius_fahrenheit():
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def datos_personales():
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    ciudad = input("Introduce tu ciudad: ")
    return f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}"

def mayor_edad():
    edad = int(input("Introduce tu edad: "))
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"

def valor():
    numero = float(input("Introduce un número: "))
    if numero < 0:
        return "El número es negativo"
    elif numero == 0:
        return "El número es cero"
    else:
        return "El número es positivo"

def par_impar():
    numero = int(input("Introduce un número entero: "))
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

def mayor_menor():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if num1 > num2:
        return f"{num1} es mayor que {num2}"
    elif num1 < num2:
        return f"{num1} es menor que {num2}"
    else:
        return "Los números son iguales"

def nota_alumno():
    nota = float(input("Introduce la nota: "))
    if ( nota < 0 ) and ( nota > 10 ) :
        return f"Valor no válido"
    elif nota < 5:
        return f"Suspenso"
    elif nota < 7:
        return f"Aprobado"
    elif nota < 9:
        return f"Notable"
    else:
        return f"Sobresaliente"

print(pedir_nombre())
print(suma())
print(area_rectangulo())
print(conversor_celsius_fahrenheit())
print(datos_personales())
print(mayor_edad())
print(valor())
print(par_impar())
print(mayor_menor())
print(nota_alumno())
