class Vuz:
    def __init__(self, udana_spz, udana_kapacita):
        self.kapacita = udana_kapacita
        self.spz = udana_spz

    def __str__(self):
        return '<SPZ: {}>'.format(self.spz)


vozovy_park = [
    Vuz('3A8 21 84', 8),
    Vuz('4B2 33 21',12),
    Vuz('1C6 17 11',14),
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

for vuz in najdi_dost_velky(vozovy_park, 10):
    print(vuz.spz)

