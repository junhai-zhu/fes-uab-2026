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

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
latencia = float(input("Latència de la connexió (ms): "))
perdues = float(input("Percentatge de paquets perduts (%): "))
if latencia < 0:
    print("Latència no vàlida.")
elif perdues < 0 or perdues > 100:
    print("Percentatge de pèrdues fora del rang valid (0-100%).")
elif latencia <= 30 and perdues <= 1:
    print("Connexió excel·lent.")
elif latencia <= 80 and perdues <= 3:
    print("Connexió bona.")
elif latencia <= 150 and perdues <= 5:
    print("Connexió acceptable.")
else:
    print("Connexió deficient.")

# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
tipus_pla = input("Tipus de pla (bàsic o plus): ").lower()
consum = float(input("Consum mensual (GB): "))
if consum < 0:
    print("Consum no vàlid.")
elif tipus_pla == "bàsic":
    cost = 10 + max(0, consum - 10) * 1.5
    print(f"Cost total del pla bàsic: {cost:.2f} €")
elif tipus_pla == "plus":
    cost = 20 + max(0, consum - 30) * 0.75
    print(f"Cost total del pla plus: {cost:.2f} €")
else:
    print("Tipus de pla desconegut.")

# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
compte_actiu = input("El compte està actiu? (s/n): ").lower() == "s"
contrasenya_correcta = input("La contrasenya és correcta? (s/n): ").lower() == "s"
if not compte_actiu:
    print("Accés denegat: compte desactivat.")
elif not contrasenya_correcta:
    print("Accés denegat: contrasenya incorrecta.")
else:
    codi_correcte = input("El codi de doble verificació és correcte? (s/n): ").lower() == "s"
    if codi_correcte:
        print("Accés permès.")
    else:
        print("Accés denegat: codi incorrecte.")

# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router_ences = input("El router està encès? (s/n): ").lower() == "s"
los_actiu = input("L'indicador LOS del terminal òptic està encès? (s/n): ").lower() == "s"
internet_actiu = input("L'indicador d'Internet del router està encès? (s/n): ").lower() == "s"
if not router_ences:
    print("Cal encendre el router.")
elif los_actiu:
    print("Cal revisar el cable de fibra.")
elif not internet_actiu:
    print("Cal contactar amb el proveïdor.")
else:
    print("La connexió funciona correctament.")

# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
servei_critic = input("La incidència afecta un servei crític? (s/n): ").lower() == "s"
usuaris_afectats = int(input("Nombre d'usuaris afectats: "))
if usuaris_afectats < 0:
    print("Nombre d'usuaris no vàlid.")
else:
    alternativa = input("Hi ha una alternativa de connexió disponible? (s/n): ").lower() == "s"
    if (servei_critic and not alternativa) or (usuaris_afectats >= 50 and not alternativa):
        print("Prioritat crítica.")
    elif usuaris_afectats >= 10 or servei_critic:
        print("Prioritat alta.")
    else:
        print("Prioritat baixa.")
