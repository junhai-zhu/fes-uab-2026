###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
name = "Junhai"
city = "Barcelona"
print(name)
print(city)
print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"Tipus de dades de 'a': {type(a)}")
print(f"Tipus de dades de 'b': {type(b)}")
print(f"Tipus de dades de 'c': {type(c)}")
print(f"Tipus de dades de 'd': {type(d)}")
print(f"Tipus de dades de 'e': {type(e)}")

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
cadena = "12345"
enter = int(cadena)
float_valor = float(enter)
print(f"Enter: {enter}, Float: {float_valor}")

enter_from_float = int(3.99)
print(f"Enter a partir de 3.99: {enter_from_float}")

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí
name = "Junhai"
age = 21
height = 1.75

print(f"Hola! Em dic {name}, tinc {age} anys i faig {height} metres.")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

### Completa aquí
pi = 3.14159
pi_arrodonit = round(pi)
divisio_entera = pi_arrodonit // 2

print(f"PI arrodonit: {pi_arrodonit}")
print(f"Divisió entera: {divisio_entera}")

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí
celsius = float(input("Temperatura en graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperatura en graus Fahrenheit: {fahrenheit}")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
total_compte = float(input("Total del compte: "))
percentatge_propina = float(input("Percentatge de propina (en %): "))
propina = total_compte * (percentatge_propina / 100)
total_final = total_compte + propina

print(f"Propina: {propina:.2f}")
print(f"Total final: {total_final:.2f}")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí
contrasenya = input("Introdueix una contrasenya: ")
if len(contrasenya) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")