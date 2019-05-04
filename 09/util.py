def zamen(retezec, pozice, znak):
    """Zamění znak na dané pozici

    Vrátí řetězec, který má na dané pozici daný znak;
    jinak je stejný jako vstupní retezec
    """
    return retezec[:pozice] + znak + retezec[pozice + 1:]

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    pole = zamen(pole,cislo_policka, symbol)
    return pole
