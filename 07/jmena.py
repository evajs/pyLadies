# def vyber_chybne(zaznamy):
#     chybne = []
#     for jmeno in zaznamy:
#         rozdel = jmeno.split()
#         if (rozdel[0].islower() or rozdel[1].islower()):
#             chybne.append(jmeno)
#     return chybne
#
# def vyber_spravne(zaznamy):
#     spravne = []
#     for jmeno in zaznamy:
#         rozdel = jmeno.split()
#         if not (rozdel[0].islower() or rozdel[1].islower()):
#             spravne.append(jmeno)
#     return spravne
#
# #
# # def oprav_zaznamy(zaznamy):
# #     opravene =[]
# #     for i in range(len(zaznamy)):
# #         rozdel = zaznamy[i].split()
# #         opraveny_zaznam = (rozdel[0].capitalize()) + ' ' + (rozdel[1].capitalize())
# #         opravene.append(opraveny_zaznam)
# #     return opravene


def vyber_chybne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if jmeno[0].islower() or prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

def vyber_spravne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if not jmeno[0].islower() and not prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

def oprav_zaznamy(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        vysledek.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())
    return vysledek

zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
chybne_zaznamy = vyber_chybne(zaznamy)
print(chybne_zaznamy) # → ['pepa novák', 'Ivo navrátil', 'jan Poledník']

spravne_zaznamy = vyber_spravne(zaznamy)
print(spravne_zaznamy) # → ['Jiří Sládek']

opravene_zaznamy = oprav_zaznamy(zaznamy)
print(opravene_zaznamy) # → ['Pepa Novák', 'Jiří Sládek', 'Ivo Navrátil', 'Jan Poledník']