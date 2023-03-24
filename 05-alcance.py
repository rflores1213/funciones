#variable global
saludo = "Hola Global"

def saludar():
    global saludo
    print (saludo)

def saludochanchito():
    saludo ="Hola chanchito"
    print (saludo)

print(saludo)
saludar()
print(saludo)
