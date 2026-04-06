# FUNCIONES

def calcular_puntaje_ronda(diccionario_jueces):
    """Esta función recibe un diccionario con los puntos de los jueces y devuelve la suma total.
    """
    # .values() nos da solo los números: [8, 7, 9]
    # sum() los suma automáticamente: 24
    total = sum(diccionario_jueces.values())
    return total

def obtener_ganador_ronda(puntajes_ronda):
    """Esta funcion recibe un diccionario de la forma {'Nombre': total_puntos} y devuelve el nombre del que tiene más puntos.
    """
    ganador = ""
    max_puntos = -1
    
    for nombre, puntos in puntajes_ronda.items():
        if puntos > max_puntos:
            max_puntos = puntos
            ganador = nombre
            
    return ganador

def calcular_promedio(puntos_totales, cantidad_rondas):
    """Esta funcion la cantidad total de puntos y la cantidad de rondas y calcula el promedio. Uso una estructura condicional para evitar dividir por cero.
    """
    if cantidad_rondas == 0:
        return 0
    return puntos_totales / cantidad_rondas