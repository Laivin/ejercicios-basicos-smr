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

def descuento():
    precio = float(input("Introduce el precio del producto: "))
    descuento = float(input("Introduce el porcentaje de descuento: "))
    precio_final = precio - (precio * (descuento / 100))
    return precio_final

def contraseña_correcta():
    contraseña = input("Introduce la contraseña: ")
    if contraseña == "1234":
        return "Contraseña correcta"
    else:
        return "Contraseña incorrecta"

def calculadora():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operacion = input("Introduce la operación (+, -, *, /): ")
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

def semaforo():
    color = input("Introduce el color del semáforo (rojo, amarillo, verde): ").lower()
    if color == "rojo":
        return "Detente"
    elif color == "amarillo":
        return "Precaución"
    elif color == "verde":
        return "Avanza"
    else:
        return "Color no válido"    

def dias_mes():
    mes = input("Introduce el mes (1-12): ")
    if mes in ["1", "3", "5", "7", "8", "10", "12"]:
        return "El mes tiene 31 días"
    elif mes in ["4", "6", "9", "11"]:
        return "El mes tiene 30 días"
    elif mes == "2":
        return "El mes tiene 28 días"
    else:
        return "Mes no válido"

def cajero_automatico():
    saldo = 1000
    print("Que quieres hacer?")
    print("1.Consultar saldo")
    print("2.Ingresar dinero")
    print("3.Retirar dinero")
    print("4.Salir")
    opcion = int(input("Introduce una opción: "))
    if opcion == 1:
        print(f"Saldo actual: {saldo}")
    elif opcion == 2:
        ingresar = float(input("Introduce la cantidad a ingresar: "))
        saldo += ingresar
    elif opcion == 3:
        retirar = float(input("Introduce la cantidad a retirar: "))
        if retirar <= saldo:
            saldo -= retirar
            return f"Dinero retirado. Saldo restante: {saldo}"
        else:
            return "Saldo insuficiente"
    elif opcion == 4:
        return "Gracias por usar el cajero automático"


def gastos_envio():
    importe = float(input("Introduce el importe del envío: "))
    if importe <= 50:
        resultado = (
            f"Importe de la compra: {importe}€\n\n"
            f"Gastos de envío: 5€\n"
            f"Total a pagar: {importe + 5}€" 
        )
        return resultado
    elif importe <= 100:
        resultado = (
            f"Importe de la compra: {importe}€\n\n"
            f"Gastos de envío: 2€\n"
            f"Total a pagar: {importe + 2}€"
        )
        return resultado
    else:
        resultado = (
            f"Importe de la compra: {importe}€\n\n"
            f"Gastos de envío: 0€\n"
            f"Total a pagar: {importe}€"
        )
        return resultado

def precio_entrada():
    edad = int(input("Introduce tu edad: "))
    if edad < 5:
        return "Entrada gratuita"
    elif edad < 18:
        return "Entrada: 5€"
    elif edad < 65:
        return "Entrada: 10€"
    else:
        return "Entrada: 6€"
    
def tiempo_corredores():
    tiempo1 = float(input("Introduce el tiempo del primer corredor (en segundos): "))
    tiempo2 = float(input("Introduce el tiempo del segundo corredor (en segundos): "))
    tiempo3 = float(input("Introduce el tiempo del tercer corredor (en segundos): "))
    if tiempo1 < tiempo2 and tiempo1 < tiempo3:
        return "Ganador: Corredor 1"
    elif tiempo2 < tiempo1 and tiempo2 < tiempo3:
        return "Ganador: Corredor 2"
    elif tiempo3 < tiempo1 and tiempo3 < tiempo2:
        return "Ganador: Corredor 3"
    else:
        return "Empate"
    
def tipo_triangulo():
    lado1 = float(input("Introduce el primer lado del triángulo: "))
    lado2 = float(input("Introduce el segundo lado del triángulo: "))
    lado3 = float(input("Introduce el tercer lado del triángulo: "))
    if lado1 == lado2 == lado3:
        return "El triángulo es equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "El triángulo es isósceles"
    else:
        return "El triángulo es escaleno"

def calcular_impuesto():
    ingresos = float(input("Introduce tus ingresos anuales: "))
    if ingresos <= 1000:
        impuesto = 0
    elif ingresos <= 2000:
        impuesto = 0.1
    else:
        impuesto = 0.2
    return (f"Sueldo bruto: {ingresos}€\n\n"
            f"Impuesto: {impuesto}%\n"
            f"Descuento: {ingresos * impuesto}€\n"
            f"Sueldo neto: {ingresos - (ingresos * impuesto)}€"
            )

def ordenar_numeros():
    numeros = []
    for i in range(3):
        numero = float(input(f"Introduce el número {i + 1}: "))
        numeros.append(numero)
    numeros.sort()
    return numeros

def convertir_segundos():
    horas = int(input("Introduce las horas: "))
    minutos = int(input("Introduce los minutos: "))
    segundos = int(input("Introduce los segundos: "))
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

def numero_secreto():
    import random
    numero = random.randint(1, 10)
    adivinanza = input("Adivina el número secreto (entre 1 y 10): ")
    if adivinanza < numero:
            print("El numero secreto es mayor")
    elif adivinanza > numero:
            print("El numero secreto es menor")
    else:
            return f"¡Felicidades! Adivinaste el número."

def factura():
    producto = input("Introduce nombre del producto: ")
    precio = input("Introduce el precio: ")
    cantidad = input("Introduce la cantidad: ")
    return (
            f"Producto: {producto}\n"
            f"Precio: {precio}\n"
            f"Cantidad: {cantidad}\n"
            f"Subtotal: {precio * cantidad}€\n"
            f"IVA: {cantidad * 0.21}€\n"
            f"Total: {precio * cantidad + cantidad * 0.21}€"
            )
def bisiesto():
    ano = int(input("Introduce un año: "))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return f"El año {ano} es bisiesto"
    else:
        return f"El año {ano} no es bisiesto"
def tarjeta_credito():
    importe = float(input("Introduce el importe de la compra: "))
    if importe > 500:
        cliente = input("Tiene tarjeta cliente? (s/n): ")
        if cliente == "s":
            descuento = importe * 0.15
            importe -= descuento
            return (
                f"Precio original: {importe}€"
                f"\nDescuento: {descuento}€"
                f"\nPrecio final: {importe - descuento}€"
            )
        else:
            descuento = importe * 0.05
            importe -= descuento
            return (
                f"Precio original: {importe}€"
                f"\nDescuento: {descuento}€"
                f"\nPrecio final: {importe - descuento}€"
            )
    else:
        return "No aplica descuento"

def cajero_billetes():
    cantidad = int(input("Introduce la cantidad a retirar: "))
    billetes_50 = cantidad // 50
    cantidad %= 50
    billetes_20 = cantidad // 20
    cantidad %= 20
    billetes_10 = cantidad // 10
    cantidad %= 10
    billetes_5 = cantidad // 5
    cantidad %= 5
    return (
        f"Billetes de 50€: {billetes_50}\n"
        f"Billetes de 20€: {billetes_20}\n"
        f"Billetes de 10€: {billetes_10}\n"
        f"Billetes de 5€: {billetes_5}\n"
        f"Monedas restantes: {cantidad}€"
    )

def dos_cifras():
    numero = int(input("Introduce un número de dos cifras: "))
    decenas = numero // 10
    unidades = numero % 10
    suma = decenas + unidades
    return (
        f"Numero: {numero}\n"
        f"Decenas: {decenas}\n"
        f"Unidades: {unidades}\n"
        f"Suma: {suma}"
    )

def test():
    pregunta1 = input("¿Cuál es la capital de España? ")
    if pregunta1 == "madrid":
        print("Correcto")
    else:
        print("Incorrecto")

def main():
    while True:
        print("Escoge un ejercicio, 0 para salir del programa")
        ejercicio = int(input("Introduce el número del ejercicio (1-30): "))
        if ejercicio == 0:
            print("Saliendo del programa...")
            break
        elif ejercicio == 1:
            print(pedir_nombre())
        elif ejercicio == 2:
            print(suma())
        elif ejercicio == 3:
            print(area_rectangulo())
        elif ejercicio == 4:
            print(conversor_celsius_fahrenheit())
        elif ejercicio == 5:
            print(datos_personales())
        elif ejercicio == 6:
            print(mayor_edad())
        elif ejercicio == 7:
            print(valor())
        elif ejercicio == 8:
            print(par_impar())
        elif ejercicio == 9:
            print(mayor_menor())
        elif ejercicio == 10:
            print(nota_alumno())
        elif ejercicio == 11:
            print(descuento())
        elif ejercicio == 12:
            print(contraseña_correcta())
        elif ejercicio == 13:
            print(calculadora())
        elif ejercicio == 14:
            print(semaforo())
        elif ejercicio == 15:
            print(dias_mes())
        elif ejercicio == 16:
            print(cajero_automatico())
        elif ejercicio == 17:
            print(gastos_envio())
        elif ejercicio == 18:
            print(precio_entrada())
        elif ejercicio == 19:
            print(tiempo_corredores())
        elif ejercicio == 20:
            print(tipo_triangulo())
        elif ejercicio == 21:
            print(calcular_impuesto())
        elif ejercicio == 22:
            print(ordenar_numeros())
        elif ejercicio == 23:
            print(convertir_segundos())
        elif ejercicio == 24:
            print(numero_secreto())
        elif ejercicio == 25:
            print(factura())
        elif ejercicio == 26:
            print(bisiesto())
        elif ejercicio == 27:
            print(tarjeta_credito())
        elif ejercicio == 28:
            print(cajero_billetes())
        elif ejercicio == 29:
            print(dos_cifras())
        elif ejercicio == 30:
            print(test())
        else:
            print("Ejercicio no encontrado.")

main()