def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    pole = pole[:cislo_policka] + symbol + pole[cislo_policka+ 1:]
    return pole
