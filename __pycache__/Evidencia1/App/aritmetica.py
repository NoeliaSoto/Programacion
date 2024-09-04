
def sumar(a: float, b: float) -> float:
    return round(a + b, 2) #todas las funciones deberán retornar un número flotante con dos números decimales

def restar(a: float, b: float) -> float:
    return round(a - b, 2)

def dividir(a: float, b: float) -> float:
    try:
        return round(a / b, 2) #considerar en la división el caso de división porcero y hacer un manejo de excepción.
    except:
        print("Error: No se puede dividir por cero")

def multiplicar(a: float, b: float) -> float:
    return round(a * b, 2)

def sumar_n(*numeros: float) -> float: #importante * para que pueda aceptar un num variable de numeros se ARROJAN EN UN TUPLA!!!
    return round(sum(numeros), 2) #tendria que arrojar un valor flotante con dos decimales

def promedio_n(*numeros: float) -> float:
    if len(numeros) == 0:
        return 0.0
    return round(sum(numeros) / len(numeros), 2) #VISTO:veeeeeer que pasa si no le ingreso numeros a la tupla, me deeria arrojar un numero flotando o error???
