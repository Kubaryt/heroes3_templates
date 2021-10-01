DZIALANIA = 5

while DZIALANIA >= 5:

    DZIALANIA = int(input('Wybierz dzialanie: 0 - Dodawanie | 1 - Odejmowanie | 2 - Mnozenie | 3 - Dzielenie | 4 - Potegowanie '))

if DZIALANIA == 0:

    a = int(input('Wpisz pierwsza liczbe '))
    b = int(input('Wpisz druga liczbe '))
    c = a + b
    print('Wynik dodawania to: %g' %  c )

if DZIALANIA == 1:

    a = int(input('Wpisz pierwsza liczbe '))
    b = int(input('Wpisz druga liczbe '))
    c = a - b
    print('Wynik odejmowania to: %g' %  c )

if DZIALANIA == 2:

    a = int(input('Wpisz pierwsza liczbe '))
    b = int(input('Wpisz druga liczbe '))
    c = a * b
    print('Wynik mnozenia to: %g' %  c )
if DZIALANIA == 3:

    a = int(input('Wpisz pierwsza liczbe '))
    b = 0
    while b == 0:
    
        b = int(input('Wpisz druga liczbe '))
    
        c = a / b
        print('Wynik dzielenia to: %g' % c )
    
    if b == 0:
    
        print('Nie dziel przez zero ')

if DZIALANIA == 4:

    a = int(input('Wpisz pierwsza liczbe '))
    b = int(input('Wpisz druga liczbe '))
    c = a ** b
    print('Wynik potegowania to: %g' % c)

if DZIALANIA >= 5:

    print('Wprowadzono zla liczbe ')