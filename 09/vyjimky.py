def f1():
    print('f1 A')
    try:
        # return 10
        f2()
    except ZeroDivisionError:
        print('Dělit nulou neumím.')
    except Exception:
        print('Stala se nějaká chyba.')
    else:
        print('Ok.')
    finally:
        print('Tohle se vypíše vždy.')
    print('f1 B')


def f2():
    print('f2 A')
    # print(1/0)
    raise Exception('Chyba')
    print('f2 B')

f1()