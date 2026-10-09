###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "Router"
ubicacio_encaminador = "Servidor"
nombre_ports = 24
ences = "esta ences"

print(f"El {nom_encaminador} està ubicat a {ubicacio_encaminador} i té {nombre_ports} ports y {ences}.")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_inclosos = 10
gb_consumits = 3
gb_restants = gb_inclosos - gb_consumits
print(f"Queden {gb_restants} GB de dades disponibles.")
gb_consumits = 5
gb_restants = gb_inclosos - gb_consumits
print(f"Queden {gb_restants} GB de dades disponibles.")