from math import pi

def p_circulo(radio:float):  # Hace que el valor a ingresar será convertida a float
    perimetro = 2 * pi * radio
    return perimetro

def a_circulo(radio:float):
    area_circulo = pi * (radio**2)
    return area_circulo

def a_cuadrado(lado:float):  # Hace que el valor a ingresar será convertida a float
    area_cuadrado = lado**2
    return area_cuadrado
