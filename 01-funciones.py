#funcion
def hola():
    print ("Hola Mundo")
    print("Ultimate Python")

#llamado de la funcion
hola()
# parametros (xxx,xxx)
def hola2(nombre, apellido):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")

# argumentos ("xxx","xxx")
hola2("Ricardo", "Flores")
hola2("chanchito", "feliz")

def hola3(nombre, apellido="Feliz"):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")

hola3("Ricardo", "Flores")
hola3("Chanchito")

#cuando no sabes el orden de los parametros
hola3(apellido="Flores", nombre="Ricardo")

