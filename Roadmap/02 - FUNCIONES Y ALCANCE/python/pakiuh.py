#funciones básicas de python
nombre = "Pakiuh"
a = 9
b = 2

# función con parametros
def hola_nombre(nombre):
    print("Hola", nombre)

hola_nombre(nombre)

# función con parametros y retorno
def suma(a, b):
    return a + b
    print("Esto no se va a imprimir")


# función con parametros y sin retorno
def suma2(a, b):
    print(a + b)

# función dentro de otra función
def hola_nombre2(nombre):
    def hola():
        print("Hola")
    hola()
    print(nombre)

# función ya creada por el lenguaje
print(len(nombre))

# función con variable global
def hola_nombre3():
    global nombre
    nombre = "Pakiuh2"
    print("Hola", nombre)

# función con variable LOCAL
def hola_nombre4():
    nombre = "Pakiuh2"
    print("Hola", nombre)