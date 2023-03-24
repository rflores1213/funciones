def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char !=" ":
            nuevo_texto += char
    return nuevo_texto

def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    print(texto_al_reves)
    return texto.lower() == texto_al_reves.lower()

print(es_palindromo("somos o no somos"))
print(es_palindromo("Hola Mundo"))
print(es_palindromo("Reconocer"))
