def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

# iterables
suma(1, 5, 7)
suma(2, 5)
suma(2, 8, 9, 13)