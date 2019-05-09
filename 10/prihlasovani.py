user_db = {'evajs':'muf', 'gimli':'muf2'}

def authentication(db, user_str, password_str):
    '''
    Tahle funkce vrací True, když je jméno a heslo nalezeno v databázi.
    :param db: databáze uživatelů
    :param user_str: uživatelské jméno
    :param password_str: heslo
    :return: zda je heslo daného uživatele správné
    '''
    vysledek = False
    if user_str in db.keys() and db[user_str]==password_str:
            vysledek = True
    return vysledek

while True:
    jmeno = input('Zadej uživatelské jméno: ')
    heslo = input('Zadej heslo: ')

    if authentication(user_db, jmeno, heslo):
        print('Vítej zpět {}!'.format(jmeno))
        break
    else:
        print('Eee špatné heslo.')

print('Tady bude možné vybrat si dovolenou.')