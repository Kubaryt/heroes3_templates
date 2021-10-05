import math
DZIALANIA = 6

while DZIALANIA >= 6:

    DZIALANIA = int(input('Wybierz dzialanie: 0 - Dodawanie | 1 - Odejmowanie | 2 - Mnozenie | 3 - Dzielenie | 4 - Potegowanie | 5 - Logarytm naturalny '))

if DZIALANIA == 0:

    a = float(input('Wpisz pierwsza liczbe '))
    b = float(input('Wpisz druga liczbe '))
    c = a + b
    print('Wynik dodawania to: %f' %  c )

if DZIALANIA == 1:

    a = float(input('Wpisz pierwsza liczbe '))
    b = float(input('Wpisz druga liczbe '))
    c = a - b
    print('Wynik odejmowania to: %f' %  c )

if DZIALANIA == 2:

    a = float(input('Wpisz pierwsza liczbe '))
    b = float(input('Wpisz druga liczbe '))
    c = a * b
    print('Wynik mnozenia to: %f' %  c )
if DZIALANIA == 3:

    a = float(input('Wpisz pierwsza liczbe '))
    b = 0
    while b == 0:
    
        b = float(input('Wpisz druga liczbe '))
    
    c = a / b
    print('Wynik dzielenia to: %f' % c )

if DZIALANIA == 4:

    a = float(input('Wpisz pierwsza liczbe '))
    b = float(input('Wpisz druga liczbe '))
    c = a ** b
    print('Wynik potegowania to: %f' % c)

if DZIALANIA == 5:

    a = float(input('Wpisz pierwsza liczbe '))
    c = math.log( a )
    print('Wynik to: %f' % c)
