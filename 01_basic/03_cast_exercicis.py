###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets_rebuts = input("Introdueix el nombre de paquets rebuts: ")
paquets_rebuts_int = int(paquets_rebuts)
total_paquets = paquets_rebuts_int + 1200
print("El total de paquets és:", total_paquets)

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat_mbps = input("Introdueix la velocitat de connexió en Mbps: ")
velocitat_mbps_float = float(velocitat_mbps)