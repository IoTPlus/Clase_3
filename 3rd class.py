#TERCERA CLASE

#LAS VARIABLES QUE SON UNICAMENTE CREADAS DENTRO DE UNA FUNCION SON CONSIDERADAS VARIABLES LOCALES
#LAS VARIABLES GLOBALES SON AQUELLAS QUE SON DEFINIDAS EN EL CODIGO GENERAL, NO DENTRO DE UNA FUNCION

#1 Como se define una función, argumento, acción a ejecutar, return/print:

#Si deseamos que la función solo imprima el resultado debemos incluir print dentro:
from math import pi

def perimetro_2(r):
    per = 2 * pi * r
    print(per)

perimetro_2(3)

#Si deseamos trabajar con el resultado de la función debemos usar return:
def perimetro(r:float):  # Hace que el valor a ingresar será convertida a float
    per = 2 * pi * r
    return per

per_ingresado = perimetro(3)
print(per_ingresado)

#2 Existen dos formas de llamar una función incluida en una librería en particular:
#Forma 1:
import math
r = int(input("Ingrese radio: "))
area = math.pi * (r**2)

#Forma 2:
from math import pi
area = pi * (r**2)

print(area)

#3 Tipos de funciones:
#3.1 Con valor de retorno:
def promedio(c1,c2,c3):
    prom = (c1+c2+c3)/3
    return round(prom)

avg = promedio(10,20,30)
print(avg)

#3.2 Con multiples valores de retorno:
def conv_horas_minutos(total_minutos):
    horas = total_minutos//60
    minutos = total_minutos%60
    return horas, minutos

h, m = conv_horas_minutos(359)
print(f"La conversión es: {h}:{m} horas")

#3.3 Sin valor de retorno:
def imprimir_datos(nombre, apellido, pais, edad, rut):
    print(f"Mi nombre es {nombre}")
    print(f"Mi apellido es {apellido}")
    print(f"Vivo en {pais}")
    print(f"Tengo {edad} años")
    print(f"Mi rut es: {rut}")

imprimir_datos("George","Saavedra", "Chile", "27", "21835456-4")

#3.4 Parámetros con valores por omisión:
def coeficientes(a, b=2, c=10):
    print(a+b+c)

coeficientes(15)
coeficientes(23,5)

#IMPORTANTE
#Para usar una función propia como una libreria externa, debemos copiar solo la funcion en un archivo nuevo
#dentro del mismo proyecto (directorio) e importarla como una libreria normal, i.e. Si el archivo se
#llama Fx_clase3.py debemos llamar a la función como con una típica librería i.e.:
# import Fx_clase3 y luego llamar Fx_clase3.pcirculo       La otra forma es la siguiente:
# from Fx_clase3 import pcirculo
#(El archivo que contiene la función debe estar siempre abierto en paralelo con el codigo que lo llama y debe
# ser previamente ejecutado).

#Otra forma es guardando el codigo .py que contiene tales funciones en la carpeta que contiene las
#librerias de python, así no será necesario tener tal archivo abierto ya que será tratado como una
#librería convencional.

from Fx_clase3 import p_circulo, a_cuadrado

radio = float(input("Ingrese radio de circulo: "))
lado = float(input("Ingrese lado del cuadrado: "))

per = p_circulo(radio)
area = a_cuadrado(lado)

print(per)
print(area)

#4 Función que retorna si el numero ingresado es par o impar:
def es_par(num):
    if num%2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

numero = int(input("Ingrese un numero: "))
es_par(numero)

#5 Funcion que resuelve la ecuación de segundo grado:
#from cmath import sqrt

import cmath

a, b, c = map(int, input("Ingrese valores de a, b y c:").split())
disc_sq = b**2 - (4*a*c)
disc = cmath.sqrt(disc_sq)
x1 = (-b+disc)/(4*a*c)
x2 = (-b-disc)/(4*a*c)
print(f"La ecuación tiene dos soluciones: {x1} y {x2}")

#6 Cree archivo incluyendo funcion que invierta digitos del numero ingresado:
#Hacer un archivo en mismo directorio con nombre mimodulo.py e incluir uno de las siguientes funciones:
#from mimodulo import invertir_digitos, invertir_digitos_2

def invertir_digitos(numero):
    num_str = str(numero)
    num_inv = num_str[::-1]
    print(num_inv)

invertir_digitos(234)

def invertir_digitos_2(numero):
    num_str = str(numero)
    len_num = len(num_str)
    i=1
    num_inv = 0
    while i<=len_num:
        resto = numero%10
        num_inv = num_inv + (resto*10**(len_num-i))
        numero = numero // 10
        i=i+1
    print(num_inv)

invertir_digitos_2(234)

#7 Seno y Coseno representados como sumatorias infinitas:
from math import factorial

def factorial_reciproco(n):
    if n==0:
        return 1
    else:
        #return (1/n)*factorial_reciproco(n-1)
        return 1/factorial(n)

def signo(n):
    if n%2==0:
        return 1
    else:
        return -1

def seno_aprox(x,m):
    i=0
    seno=0
    while(i<m):
        seno=seno+signo(i)*x**(2*i+1)*(factorial_reciproco(2*i+1))
        i=i+1
    return seno

def coseno_aprox(x,m):
    i=0
    coseno=0
    while(i<m):
        coseno=coseno+signo(i)*x**(2*i)*(factorial_reciproco(2*i))
        i=i+1
    return coseno

from math import pi

print(seno_aprox(2*pi,10))
print(coseno_aprox(2*pi,10))

#8 Strings son inmutables, i.e. no pueden ser modificados una vez fueron definidos
cadena = "Hola mundo"
print(cadena[:7])
print(cadena[2:7])
print(cadena[-5:])
print(cadena[::2])

#9 Recorrer cada caracter de un string:
#9.1
i=0
while i<len(cadena):
    print(f"s: {cadena[i]}")
    i+=1

#9.2
for i in cadena:
    print(f"s: {i}")

#10 Reemplazar secciones de un string:
a = "jajajaja"
a.replace("a","s") #Reemplaza todas las apariciones del string a por s.

#Reemplaza una palabra completa:
mensaje="Estoy muy cansado"
print(mensaje.replace("cansado", "animado"))

#Reemplaza la primera letra a del mensaje por una s:
print(mensaje.replace("a", "e", 1))

#Convertir a mayusculas:
print(mensaje.upper())

#Convertir a minusculas:
print(mensaje.lower())

#Encontrar indice de caracter o seccion especifica:
print(mensaje.index("muy"))

#11 Interpolación de strings:
# s.format(): Permite generar un string dinamico a partir de un string "plantilla"

s = "Soy {0} y vivo en {1}"  # Plantilla
print(s.format("Juan", "Santiago"))

print('{0}{0}{0}{1}{1}{1} Viva Chile!'.format("CHI ", "LE "))

#12 Cadena al azar que retorne secuencia con n bases:
from random import choice

def cadena_al_azar(n):
    i=0
    base=""
    while i<n:
        base=base+choice("acgt")
        i=i+1
    print(base)

cadena_al_azar(10)

#13 Cadena complementaria:
cadena = str(input("Ingrese cadena: "))

def complementaria(c):
    complemento =c.replace("a","x").replace("t","a").replace("x","t").replace("c","y").replace("g","c").replace("y","g")
    print(c)
    print(complemento)

complementaria(cadena)

#14 Palabra a descifrar, del final al inicio en impares:
palabra = input("Ingrese palabra a descifrar: ")

def codigo_palabra(word):
    codigo = word[::-2]
    print(codigo)

codigo_palabra(palabra)

#15 Función para descifrar hora y minutos ingresados en código:
def codigo_hora(tiempo):
    a, b = tiempo.split(":")
    i=0
    j=0
    a=str(a)
    b=str(b)
    suma_a = 0
    suma_b = 0
    while i<len(a):
        suma_a = suma_a + int(a[i])
        i+=1

    while j<len(b):
        suma_b = suma_b + int(b[j])
        j+=1

    print(f"{suma_a%24}: {suma_b%60}")

codigo_hora('776199:68556')

# Ejercicio extra 1:
def contador(st):
    unique = 0
    while len(st) > 0:
        unique += 1
        st = st.replace(st[0], "")

    return unique

cant = int(input("Cantidad de palabras que ingresará: "))
k=1
word = input("Ingrese palabra: ")
menor = contador(word)
mayor = menor
palabra_mas_corta = word
palabra_mas_larga = word
while k < cant:
    word = input("Ingrese palabra: ")
    if contador(word) > mayor:
        mayor = contador(word)
        palabra_mas_larga = word
    if contador(word) < menor:
        menor = contador(word)
        palabra_mas_corta = word
    k+=1

print(f"La palabra con menos caracteres unicos es: {palabra_mas_corta} con {menor} letras unicas")
print(f"La palabra con mas caracteres unicos es: {palabra_mas_larga} con {mayor} letras unicas")

#Ejercicio extra 2:
def valida(cadena):
    cadena = cadena.replace('A','').replace('T','').replace('C','').replace('G','').replace(' ','')
    if len(cadena) == 0:
        return True
    else:
        return False

print(valida('CTGA AATT GGGC'))

#Ejercicio extra 3:
def cantidad(cadena, base):
    bases = "ATCG "
    i=0
    while i < 5:
        if base != bases[i]:
            cadena = cadena.replace(bases[i],'')
        i+=1
    return len(cadena)

print(cantidad("CTGA AATT","A"))

#Ejercicio extra 4:
def cantidad_bases(cadena):
    bases = "ATCG "
    i=0
    cadena_A = cadena.replace('T','').replace('C','').replace('G','').replace(' ','')
    cadena_T = cadena.replace('A', '').replace('C', '').replace('G', '').replace(' ', '')
    cadena_C = cadena.replace('T', '').replace('A', '').replace('G', '').replace(' ', '')
    cadena_G = cadena.replace('T', '').replace('C', '').replace('A', '').replace(' ', '')
    cadena_X = cadena.replace('T', '').replace('C', '').replace('A', '').replace('G','').replace(' ', '')
    return len(cadena_A), len(cadena_T), len(cadena_C), len(cadena_G), len(cadena_X)


cantidad = int(input("Cantidad de cadenas a ingresar: "))
k=1
animal = 0
vegetal = 0
ET = 0
while k <= cantidad:
    cadena = input(f"Ingrese cadena {k}: ")
    A, T, C, G, X = cantidad_bases(cadena)
    A_T = A + T
    C_G = C + G
    if X > 0:
        ET+=1
    elif C_G > A_T:
        vegetal+=1
    elif C_G < A_T:
        animal+=1
    k+=1

print(f"Cantidad de animales: {animal}")
print(f"Cantidad de vegetales: {vegetal}")
print(f"Cantidad no validas: {ET}")