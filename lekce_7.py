import os
import random
import platform
from figurka import hangman  # relative path
from words import all_words   # relative path


def obesenec():
    zivoty = 7
    hra_bezi = True
    hra(zivoty, hra_bezi)
def hra(zivoty, hra_bezi):
    """
    Popis:
    Prubeh hry obesenec
    Parametry:
    - zivoty: int
    - hra_bezi: bool
    Return:
    - None
    """
    slovo = random.choice(all_words)
    tajenka = vytvor_tajenku(slovo, "_")
    while hra_bezi and zivoty > 0:
        zobraz_stav_hry(tajenka, zivoty)
        hadani = input("Hadej pismeno/slovo:")
        if hadani == slovo:
            hra_bezi = False
        elif len(hadani) == 1 and hadani in slovo:
            indexy = je_pismeno_ve_slove(slovo, hadani)
            tajenka = prepis_pismeno(tajenka, indexy, hadani)
            hra_bezi = kompletni_tajenka(tajenka)
        else:
            zivoty -= 1
    else:
        konec_hry(zivoty, slovo)
def vytvor_tajenku(slovo, symbol):  # ["_", "_", "_", "_", ...]
    return len(slovo) * [symbol]
def zobraz_stav_hry(tajenka, zivoty):
    prepis_vystup()
    print(
        f"TAJENKA: {' '.join(tajenka)}; ZIVOTY: {zivoty}",
        hangman[7 - zivoty],
        sep="\n"
    )
def prepis_vystup():
    if platform.system() == "Linux" or platform.system() == "MacOs":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
def je_pismeno_ve_slove(slovo, hadani):  # "virus", "i"
    indexy = []
    for index, pismeno in enumerate(slovo):  # "virus"
        if hadani == pismeno:
            indexy.append(index)
    return indexy
def prepis_pismeno(tajenka, indexy, hadani): # "pollution" -> "l" -> [2, 3]
    for index in indexy: # [2, 3]
        tajenka[index] = hadani  # ["_", "_", "l", "l", ...]
    return tajenka
def kompletni_tajenka(tajenka):
    return True if "_" in tajenka else False  # ["_", "_", "l", "l", ...] -> True
def konec_hry(zivoty, slovo):
    if not zivoty:
        print(hangman[7 - zivoty], "\nProhrals, snad priste!", slovo)
    else:
        print(f"Vyhrals, gratulace!", slovo)
obesenec()