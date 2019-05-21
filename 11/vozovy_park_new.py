class Vuz:
    def __init__(self, udana_spz, udana_kapacita, udany_dojezd):
        self.kapacita = udana_kapacita
        self.spz = udana_spz
        self.dojezd = udany_dojezd

    def __str__(self):
        return '<SPZ: {}>'.format(self.spz)

class ElektroVuz(Vuz):
    def __init__(self, udana_spz, udana_kapacita, udany_dojezd, udana_spotreba):
        super().__init__(udana_spotreba, udana_kapacita, udany_dojezd)
        self.kilowat_na_sto = udana_spotreba


class NaftoVuz(Vuz):
    def __init__(self, udana_spz, udana_kapacita, udany_dojezd, udana_spotreba):
        super().__init__(udana_spotreba, udana_kapacita, udany_dojezd)
        self.litru_na_sto = udana_spotreba

class HybridVuz(Vuz):
    def __init__(self, udana_spz, udana_kapacita, udany_dojezd, udana_spotreba_elektro, udana_spotreba_nafta):
        super().__init__(udana_spotreba, udana_kapacita, udany_dojezd)
        self.kilowat_na_sto = udana_spotreba_elektro
        self.litru_na_sto = udana_spotreba_nafta

vozovy_park = [
    ElektroVuz('3A8 21 84', 20, 400, 30),
    ElektroVuz('4B2 33 21', 12, 200, 20),
    NaftoVuz('1C6 17 11', 14, 500, 10),
    NaftoVuz('6D2 51 61', 6, 600, 7),
    HybridVuz('8E5 16 71', 6, 200, 15, 7),
    HybridVuz('0F2 59 12', 10, 400, 18, 10),
]