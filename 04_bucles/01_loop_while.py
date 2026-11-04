###
# 01 - Bucles (while)
# Permeten executar un bloc de codi repetidament mentre es compleixi una condició
###

# print("\n Bucle while:")

# Bucle amb una condició simple
# comptador = 0

# {claus} [claudàtors] (parèntesis)
# indentació "tabulació o sagnat"

# while comptador <= 5:
#     print(comptador)
#     comptador += 1 # és molt important per evitar un bucle infinit

# utilitzant la paraula break, per trencar el bucle
# print("\n Bucle while amb break:")
# comptador = 0

# while True:
#   print(comptador)
#   comptador += 1
#   if comptador == 5:
#     break # surt del bucle

# continue, el que fa és saltar aquesta iteració en concret
# i continuar amb el bucle
# print("\n Bucle amb continue")
# comptador = 0
# while comptador < 10:
#   comptador += 1

#   if comptador % 2 == 0:
#     continue

#   print(comptador)

# else, quan s'executa aquesta condició?
# print("\n Bucle while amb else:")
# comptador = 0
# while comptador < 5:
#   print(comptador)
#   comptador += 1

# else:
#   print("El bucle ha acabat, i ha recorregut tots els números")

# else, quan s'executa aquesta condició?
# print("\n Bucle while amb else:")
# comptador = 0
# while comptador < 5:
#   print(comptador)
#   comptador += 1
# else:
#   print("El bucle ha acabat")

# comptador = 0
# while comptador < 5:
#     print(f"El comptador = {comptador}")
#     comptador += 1
# else:
#     print("El bucle while ha acabat de forma natural.")
#     print(f"El valor final del comptador = {comptador}.")

# numero = 0
# while numero < 10:
#     print(f"El nombre = {numero}")
#     if numero == 3:
#         print("Hem arribat al 3! Trencant el bucle.")
#         break  # Interromp el bucle
#     numero += 1
# else:
#     print("Aquest missatge no s'imprimirà perquè el bucle ha estat interromput per 'break'.")

# print("El programa ha continuat despres del bucle.")

# Sortida esperada:
# El número és 0
# El número és 1
# El número és 2
# El número és 3
# Hem arribat al 3! Trencant el bucle.
# El programa ha continuat després del bucle.

# Sortida esperada:
# El comptador és 0
# El comptador és 1
# El comptador és 2
# El comptador és 3
# El comptador és 4
# El bucle while ha acabat de forma natural.
# El valor final del comptador és 5.

# demanar a l'usuari un número que ha
# de ser positiu, si no, no el deixem en pau
numero = -1
while numero < 0:
  numero = int(input("Escriu un número positiu: "))
  if numero < 0:
    print("El número ha de ser positiu. Torna-ho a provar.")

print(f"El número que has introduït és {numero}")

# numero = -1
# while numero < 0:
#   try:
#     numero = int(input("Escriu un número positiu: "))
#     if numero < 0:
#       print("El número ha de ser positiu. Torna-ho a provar.")
#   except:
#     print("El que introdueixes ha de ser un número, que si no peta!")

# print(f"El número que has introduït és {numero}")

