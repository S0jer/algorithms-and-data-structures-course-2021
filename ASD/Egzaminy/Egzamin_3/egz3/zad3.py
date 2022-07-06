# Paweł Jaśkowiec, 406165


# Pomysł polega na odczytaniu z kazdego indeksu w tablicy X trasy dla danego indeksu poprzez sprawdzenie
# czy z danego indeksu, przykładowo 5, idę w prawą bądź lewą stronę oraz spisaniu ścieżki dotarcia do danego indeksu w tablicy
# następnie przechodząc po drzewie zgodnie z instrukcjami z tablicy docieramy do elementu o podanym indeksie i sprawdzamy czy dana wartość
# pod tym indeksem jest maksymalna


from zad3testy import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.right = None  # prawe poddrzewo
        self.parent = None  # rodzic drzewa jesli istnieje
        self.key = None  # klucz


def maxim(T, C):
    n = len(C)

    result = -1
    for i in range(n):
        if C[i] > 0:
            check = find_idK(T, C[i])  # dla kazdego naturalnej wartosci z tablicy
            if check > result:  # szukamy jaka wartosc jest pod tym indeksem
                result = check

    return result


def find_idK(T, idx):
    if idx == 1:
        return T.key

    cnt = 0
    for j in bin(idx):  # po trasie docieramy do danego indeksu
        if j == '0' and cnt > 2:
            T = T.left
        if j == '1' and cnt > 2:
            T = T.right
        cnt += 1

    return T.key


runtests(maxim)
