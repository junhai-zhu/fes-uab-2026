###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}!")

saludar_a("Alice")
saludar_a("Bob", "Benvolgut")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    return numero % 2 == 0
es_parell(4)
es_parell(5)

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)
mitjana([10, 20, 30, 40, 50])

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
    return sum(args)

sumar_tot(1, 2)
sumar_tot(1, 2, 3, 4, 5)

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
    for i in range(1, limit + 1):
        print(f"{numero} x {i} = {numero * i}")
taula_multiplicar(5)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(nom="Junhai", edat=22, grau="teleco")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
  resultat = 1
  comptador = 1
  while comptador <= n:
    resultat *= comptador
    comptador += 1
  return resultat

def maxim(numeros):
  valor_maxim = numeros[0]
  for numero in numeros:
    if numero > valor_maxim:
      valor_maxim = numero
  return valor_maxim

print(f"El factorial de 3 és {factorial(3)}")
print(f"El màxim és {maxim([1, 5, 2, 11, 23])}")
# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    vocals = "aeiouáàèéíòóúù"
    comptador = 0
    for lletra in text.lower():
        if lletra in vocals:
            comptador += 1
    return comptador

print(f"La cadena 'Hola' té {comptar_vocals('Hola')} vocals")

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
    min_val = numeros[0]
    max_val = numeros[0]
    for numero in numeros:
        if numero < min_val:
            min_val = numero
        if numero > max_val:
            max_val = numero
    return min_val, max_val

minim, maxim = minim_i_maxim([1, 2, 4, 95, 23])
print(f"El mínim és {minim} i el màxim és {maxim}")

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text):
    text = text.lower()
    return text == text[::-1]
print(f"'radar' és palíndrom? {es_palindrom('radar')}")
