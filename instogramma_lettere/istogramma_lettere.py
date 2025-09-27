

import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import string

mio_array =  [0] * 26

parser = argparse.ArgumentParser(description="Leggi un path da linea di comando")  # Crea il parser per gli argomenti della linea di comando
parser.add_argument("file", type=Path, help="Percorso del file di testo")#legge il file di testo tipo path
args = parser.parse_args() # Parsing degli argomenti della linea di comando, legge e memorizza in args

with args.file.open("r", encoding="utf-8") as f:  # apre il file in modalita' lettura
    while True:
        lettera = f.read(1)   # legge un carattere
        if not lettera:       # fine file
            break
        if lettera.isalpha():
            lettera = lettera.lower() 
            mio_array[ord(lettera) - 97] += 1  # Incrementa il contatore per la lettera letta
lettere = list(string.ascii_lowercase)  # ['a', 'b', ..., 'z']
plt.bar(lettere, mio_array, color='skyblue', edgecolor='black')
plt.xlabel('Lettere (a-z)')
plt.ylabel('Frequenza')
plt.show()