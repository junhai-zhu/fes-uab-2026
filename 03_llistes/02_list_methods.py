###
# 04 - Mètodes de les llistes
# Els mètodes més importants per treballar amb llistes
###

llista1 = ['a', 'b', 'c', 'd']
print(llista1)
# Afegir o inserir elements a la llista
# llista1[4]='e'
llista1.append('e') # Afegeix un element al final.
print(llista1)

llista1.insert(1, '@') # Insereix un element a la posició indicada pel primer argument.
print(llista1)

llista1.extend(['😃', '😍']) # Afegeix elements al final de la llista.
print(llista1)

# Eliminar elements de la llista
llista1.remove('@') # Elimina la primera aparició del caràcter @.
print(llista1)

ultim = llista1.pop() # Elimina l'últim element de la llista i també el retorna.
# llista1.pop(-1) # També es pot fer així.
print(ultim)
print(llista1)

lletra_b = llista1.pop(1) # Elimina el segon element de la llista (índex 1).
print(lletra_b)
print(llista1)

# Eliminar directament amb del
del llista1[-1]
print(llista1)

llista1.clear() # Elimina tots els elements de la llista.
print(llista1)

# Eliminar un interval d'elements
llista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del llista1[1:3]
print(llista1)

# Més mètodes útils
print("Ordenar llistes modificant l'original")
nombres = [3, 10, 2, 8, 99, 101]
nombres.sort()
print(nombres)

print('Ordenar llistes creant-ne una de nova')
nombres = [3, 10, 2, 8, 99, 101]
nombres_ordenats = sorted(nombres)
print(nombres)
print(nombres_ordenats)

print("Ordenar una llista de cadenes de text (tot en minúscula)")
fruites = ['poma', 'pera', 'llimona', 'poma', 'pera', 'llimona']
fruites_ordenades = sorted(fruites)
print(fruites_ordenades)

print("Ordenar una llista de cadenes de text (majúscules i minúscules barrejades)")
fruites = ['poma', 'Pera', 'Llimona', 'poma', 'pera', 'llimona']
fruites.sort(key=str.lower)
# No distingeix entre majúscules i minúscules.
print(fruites)

# Més coses útils
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Mida de la llista -> 4
print(animals.count('🐶')) # Quantes vegades apareix '🐶' -> 2
print('🐼' in animals) # Comprova si hi ha un '🐼' a la llista -> True
print('🐹' in animals) # -> False
