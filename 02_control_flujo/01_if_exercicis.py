###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
senyal = float(input("Nivell de senyal Wi-Fi (dBm): "))
if senyal >= -50:
    print("Cobertura excel·lent.")
elif senyal >= -67:
    print("Cobertura bona.")
elif senyal >= -75:
    print("Cobertura feble.")
else:
    print("Cobertura molt feble.")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia = float(input("Potència òptica rebuda (dBm): "))
if potencia < -27:
    print("Nivell massa baix.")
elif potencia <= -8:
    print("Nivell acceptable.")
else:
    print("Nivell massa alt.")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Consum de dades (GB): "))
if consum <= 20:
    print("Consum dins del límit.")
else:
    addicionals = consum - 20
    print(f"Consum superat. GB addicionals: {addicionals}")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los = input("L'indicador LOS està encès? (si/no): ") == "si"
internet = input("L'indicador d'Internet esta ences? (si/no): ") == "si"
if los and internet:
    print("La connexio sembla funcionar correctament.")
elif los and not internet:
    print("Cal revisar el cable de fibra.")
else:
    print("Cal comprovar el servei del proveïdor.")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria = float(input("Percentatge de bateria del SAI: "))
if bateria < 0 or bateria > 100:
    print("Valor fora del rang valid (0-100%).")
elif bateria < 20:
    print("Nivell de bateria critic.")
elif bateria < 50:
    print("Nivell de bateria baix.")
else:
    print("Nivell de bateria suficient.")