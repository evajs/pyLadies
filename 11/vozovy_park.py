class Vuz:
    def __init__(self, udana_spz, udana_kapacita, udana_cena_za_kilometr, udane_palivo, udany_dojezd):
        self.kapacita = udana_kapacita
        self.spz = udana_spz
        self.cena_za_kilometr = udana_cena_za_kilometr
        self.palivo = udane_palivo
        self.dojezd = udany_dojezd

    def __str__(self):
        return '<SPZ: {}>'.format(self.spz)


vozovy_park = [
    Vuz('3A8 21 84', 20, 8, 'elektrický', 400),
    Vuz('4B2 33 21', 12, 12, 'naftový', 200),
    Vuz('1C6 17 11', 14, 7, 'elektrický', 330),
    Vuz('6D2 51 61', 6, 10, 'naftový', 600),
]

def secti_celkovou_kapacitu(seznam_vozu):
    kapacita = 0
    for vuz in seznam_vozu:
        kapacita += vuz.kapacita
    return kapacita

def najdi_dost_velky(seznam_vozu, pozadovana_kapacita):
    vyhovujici_vozy=[]
    for vuz in seznam_vozu:
        if vuz.kapacita >= pozadovana_kapacita:
            vyhovujici_vozy.append(vuz)
    return vyhovujici_vozy

# def najdi_dost_velky_levny(seznam_vozu, pozadovana_kapacita):
#     nejvyhodnejsi = None
#     for vuz in seznam_vozu:
#         if vuz.kapacita >= pozadovana_kapacita:
#             if nejvyhodnejsi == None or vuz.spotreba < nejvyhodnejsi.spotreba:
#                 nejvyhodnejsi =  vuz
#     return nejvyhodnejsi

def najdi_dost_velky_levny(seznam_vozu, pozadovana_kapacita, delka_vyletu):
    nejvyhodnejsi = None
    for vuz in seznam_vozu:
        if vuz.kapacita >= pozadovana_kapacita and (vuz.dojezd >= delka_vyletu or vuz.palivo == 'naftový'):
            if nejvyhodnejsi == None or vuz.cena_za_kilometr < nejvyhodnejsi.cena_za_kilometr:
                nejvyhodnejsi =  vuz
    return nejvyhodnejsi


try :
    print(najdi_dost_velky_levny(vozovy_park, 12, 650).spz)
except AttributeError:
    print('Žádný dost velký vůz s dostatečným dojezdem nemáme :-(')


