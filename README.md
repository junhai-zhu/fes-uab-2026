# Fonaments d'Enginyeria de Software amb Python

Materials docents de l'assignatura **Fonaments d'Enginyeria de Software (FES)** de la Universitat Autònoma de Barcelona (**UAB**), curs acadèmic **2026–2027** (Graus d'Enginyeria d'Electrònica de Telecomunicacions i de Sistemes de Telecomunicacions).

---

## Estructura i convenció de fitxers

Els continguts s'organitzen en carpetes temàtiques numerades seguint una progressió lògica d'aprenentatge. Per a cada tema es troba:

- `NN_tema.py`: Explicacions i exemples de codi executables.
- `NN_tema.ipynb`: Versió interactiva en format Jupyter Notebook.
- `NN_tema_exercicis.py`: Enunciats d'exercicis pràctics.
- `NN_tema_solucions.py`: Propostes de resolució dels exercicis.

---

## Ruta d'aprenentatge

| Bloc | Carpeta / Fitxers | Continguts principals |
|---|---|---|
| **00. Introducció** | [`00_exemple.py`](00_exemple.py)<br>[`00_explicacio_exemple.ipynb`](00_explicacio_exemple.ipynb) | Primer programa en Python i sortida per consola. |
| **01. Conceptes bàsics** | [`01_basic/`](01_basic/) | Sortida (`print`), tipus de dades (`types`), conversions (`cast`), variables i entrada d'usuari (`input`). Inclou recopilatori d'exercicis bàsics. |
| **02. Condicionals** | [`02_condicional_if/`](02_condicional_if/) | Estructures de control `if`, `elif`, `else` i operadors booleans (`and`, `or`, `not`). |
| **03. Llistes** | [`03_llistes/`](03_llistes/) | Creació, indexació, slicing i mètodes de llista (`append`, `insert`, `remove`, `pop`, `sort`, etc.). |
| **04. Bucles** | [`04_bucles/`](04_bucles/) | Bucles `while`, `for`, `break`, `continue` i generació de seqüències amb `range()`. |
| **05. Funcions** | [`05_funcions/`](05_funcions/) | Definició de funcions (`def`), paràmetres, arguments i retorn de valors (`return`). |
| **06. Diccionaris** | [`06_diccionaris/`](06_diccionaris/) | Estructures clau-valor (`dict`), accés, mètodes i iteració. |
| **07. Tuples** | [`07_tuples/`](07_tuples/) | Seqüències immutables (`tuple`), accés, propietats i comparativa amb llistes. |

---

## Execució del codi

### Scripts de Python (`.py`)

Executa qualsevol fitxer des de l'arrel del repositori:

```bash
# Windows
py ./01_basic/01_print.py

# Linux / macOS
python3 ./01_basic/01_print.py
```

### Notebooks interactius (`.ipynb`)

Els fitxers `.ipynb` es poden obrir directament a **VS Code** (recomanat, amb l'extensió oficial de Jupyter) o bé executant Jupyter Notebook al terminal:

```bash
jupyter notebook
```

---

## Metodologia de treball recomanada

1. **Explorar**: Llegeix i executa el fitxer d'exemples (`.py` o `.ipynb`).
2. **Experimentar**: Modifica valors i prediu el comportament abans d'executar.
3. **Practicar**: Resol el fitxer `_exercicis.py` de manera autònoma.
4. **Validar**: Compara el teu resultat amb `_solucions.py` i analitza possibles alternatives.

