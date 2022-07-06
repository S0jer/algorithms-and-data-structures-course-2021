# Paweł Jaśkowiec, 406165

# Funkcja cutthetree wywołuje rekurencyjna funkcje cut dla prawego i lewego poddrzewa o ile one istnieją i zlicza dla nich najmniejsza
# mozliwa wartość aby były spełnione warunki zadania po czym sumuje wartosc dla prawego i lewego poddrzewa i zwraca sume jako wynik

from zad2testy import runtests


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(T):
    result_l, result_p = 0, 0

    # jesli istnieja poddrzewa wywołujemy funkcje rekurencyjna 'cut'
    if T.left is not None:
        result_l = cut(T.left, 0)
    if T.right is not None:
        result_p = cut(T.right, 0)

    result = result_l + result_p

    return result


def cut(T, result):
    a_l, a_p = 0, 0
    if T.left is not None:  # badamy rekurencyjnie poddrzewa w lewa strone szukajac najlepszej wartosci
        a_l = cut(T.left, result)
    if T.right is not None:  # badamy rekurencyjnie poddrzewa w prawa strone szukajac najlepszej wartosci
        a_p = cut(T.right, result)

    if T.left is None and T.right is None:
        return T.parent.value  # jesli dojdziemy do liscia zwracamy wartosc parenta

    if a_l != a_p and T.value != a_l and T.value != a_p:  # jesli T nie jest parentem prawej lub/i lewej strony wybiermy czy
        # lepiej usunac T czy jego dzieci
        result = min(a_l + a_p, T.value)
    elif T.value == a_l or T.value == a_p:  # jesli dziecko T jest lisciem musimy usunac T
        result = T.value
    else:  # dla przypadku gdzie parentem z lewej oraz prawej strony jest T
        result = min(a_l, T.value)

    return result


runtests(cutthetree)
