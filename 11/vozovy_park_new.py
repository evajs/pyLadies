class Vuz:
    def __init__(self, udana_spz, udana_kapacita):
        self.kapacita = udana_kapacita
        self.spz = udana_spz

    def __str__(self):
        return '<SPZ: {}>'.format(self.spz)

class ElektroVuz(Vuz):
    def __init__(self, udana_spz, udana_kapacita, udany_dojezd, udana_spotreba):
        super().__init__(udana_spz, udana_kapacita)
        self.dojezd = udany_dojezd
        self.kilowat_na_sto = udana_spotreba

    def cena(self, vzdalenost, cena_kilowaty, cena_nafty):
        cena = cena_kilowaty*self.kilowat_na_sto*vzdalenost/100
        return cena


class NaftoVuz(Vuz):
    def __init__(self, udana_spz, udana_kapacita, udany_dojezd, udana_spotreba):
        super().__init__(udana_spz, udana_kapacita)
        self.dojezd = udany_dojezd
        self.litru_na_sto = udana_spotreba

    def cena(self, vzdalenost, cena_kilowaty, cena_nafty):
        return cena_nafty*self.litru_na_sto*vzdalenost/100

class HybridVuz(Vuz):
    def __init__(self, udana_spz, udana_kapacita, udany_dojezd_elektro, udany_dojezd_nafta, udana_spotreba_elektro, udana_spotreba_nafta):
        super().__init__(udana_spz, udana_kapacita)
        self.dojezd_elektro = udany_dojezd_elektro
        self.dojezd_nafta = udany_dojezd_nafta
        self.kilowat_na_sto = udana_spotreba_elektro
        self.litru_na_sto = udana_spotreba_nafta

    def cena(self, vzdalenost, cena_kilowaty, cena_nafty):
        if vzdalenost <= self.dojezd_elektro:
            cena = cena_kilowaty*self.kilowat_na_sto*vzdalenost/100
        else:
            cena = cena_kilowaty*self.kilowat_na_sto*self.dojezd_elektro/100 + cena_nafty*self.litru_na_sto*(vzdalenost-self.dojezd_elektro)/100
        return cena

vozovy_park = [
    ElektroVuz('4Z2 42 42', 5, 500, 14),
    ElektroVuz('3A8 21 84', 20, 400, 30),
    ElektroVuz('4B2 33 21', 12, 200, 20),
    NaftoVuz('1C6 17 11', 14, 500, 10),
    NaftoVuz('6D2 51 61', 6, 600, 7),
    HybridVuz('8E5 16 71', 6, 200, 400, 15, 10),
    HybridVuz('0F2 59 12', 10, 400, 200, 20, 15),
]

def najdi_nejlevnejsi(vozovy_park, kapacita, delka, cena_kilowaty, cena_nafty):
    nejlevnejsi = None
    for vuz in vozovy_park:
        if vuz.kapacita >= kapacita and (type(vuz)!=ElektroVuz or delka<= vuz.dojezd):
            if nejlevnejsi== None or vuz.cena(delka, cena_kilowaty, cena_nafty)< cena:
                cena = vuz.cena(delka, cena_kilowaty, cena_nafty)
                nejlevnejsi = vuz
    return nejlevnejsi


kapacita = int(input('Kolik osob pojede? '))
delka = int(input('Kolik kilometrů bude dlouhý výlet? '))
cena_nafty = int(input('Zadej cenu nafty v Kč: '))
cena_kilowaty = int(input('Zadej cenu kilowatthodiny v Kč: '))


try :
    print('Nejlevnější řešení je vůz ', najdi_nejlevnejsi(vozovy_park, kapacita, delka, cena_nafty, cena_kilowaty).spz)
except AttributeError:
    print('Žádný dost velký vůz s dostatečným dojezdem nemáme :-(')

