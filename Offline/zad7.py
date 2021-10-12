#
# Paweł Jaśkowiec, 406165
#
# W funkcji Hoffman sortuje tablice S oraz F a następnie zapisuję wartości z F do pierwszego wiersza tablicy Huff,
# jednocześnie tworzę kopię tablicy S przed posortowaniem aby odnosić się do elementów w pierwotnej kolejności,
# następnie tworzę pierwszy element wybierając dwa najrzadsze elementy i na miejsce ich czestości wpisuje kolejno 0 oraz 1
# przechodząc po kazdym elemencie tworzę tablicę Huff w której zawierać się będą odpowiednio wartości 0 lub 1 z których
# utworzę kod oraz przekierowania na następny element tworzący kod danej litery.
#
# Złożoność: O(n^2)
#

from queue import PriorityQueue

S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]


# T_1 = ["a", "b", "c", "d", "e"]
# T_2 = [0.1, 0.1, 0.15, 0.2, 0.45]
# S_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "r", "s", "t", "u", "w", "y", "z",
#        "q"]
# F_1 = [865, 395, 777, 912, 431, 42, 266, 989, 524, 498, 415, 941, 803, 850, 311, 992, 489, 367, 598, 914, 930, 224, 517]


def partition(A, B, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    B[r], B[i + 1] = B[i + 1], B[r]

    return i + 1


def quicksort(T, L, p, l):
    while p < l:
        q = partition(T, L, p, l)
        quicksort(T, L, p, q - 1)
        p = q + 1


def search(S, el):
    idx = 0
    while S[idx] != el:
        idx += 1
    return idx


def huffman(S, F):
    n = len(F)
    S_S = S[:]  # kopia tablicy aby odnosić się do pierwotnej kolejności liter
    Huff = [[-1] * (2 * n - 1) for _ in range(2)]
    quicksort(F, S, 0, len(F) - 1)  # sortuję aby biorąc elementy po kolei mieć najmniejszy element
    L = 0

    for i in range(n):
        Huff[0][i] = F[i]  # uzupełniam tablicę Huff wartością częstości dla każdej litery

    # tworzę słowo z dwóch o najmniejszych wartościach
    w = n
    p_last = Huff[0][0] + Huff[0][1]
    Huff[1][0], Huff[1][1], Huff[0][0], Huff[0][1] = w, w, 0, 1
    Huff[0][w] = p_last
    j, w, w_prev, = 2, n + 1, n

    # powtarzam dla każdych dwóch elementów o najmniejszych wartościach do momentu aż wykorzystam wszystkie i przypisuję
    # im odpowiednio 0 lub 1
    while j < n or w < 2 * n:

        if Huff[1][j] == -1 and Huff[0][j] != -1:
            mini_1 = Huff[0][j]
        else:
            while Huff[1][j] != -1 or Huff[0][j] == -1:
                j += 1
            mini_1 = Huff[0][j]

        mini_2 = p_last
        idx = w_prev
        for i in range(j + 1, 2 * n - 1):
            if Huff[0][i] < mini_2 and Huff[1][i] == -1 and Huff[0][i] != -1:
                mini_2 = Huff[0][i]
                idx = i

        p_last = mini_1 + mini_2
        Huff[1][idx], Huff[1][j] = w, w

        if w < 2 * n - 1:
            Huff[0][w] = p_last

        if mini_1 <= mini_2:
            Huff[0][idx] = 1
            Huff[0][j] = 0
        else:
            Huff[0][idx] = 0
            Huff[0][j] = 1

        w_prev = w
        w += 1
        j += 1

    for i in range(n):
        a = search(S, S_S[i])  # znajduję miejsce kolejnych elementów z tablicy nieposortowanej w tablicy posortowanej
        a_0 = a  # i względem nich wypisuje odpowiadający im kod oraz zliczam długość napisu
        l = 0
        word = ''
        while a < 2 * n - 2:
            l += 1
            word += str(Huff[0][a])
            a = Huff[1][a]
        L += F[a_0] * l
        print(S_S[i], ':', word[::-1])
    # wypisuję utworzony kod

    print("dlugosc napisu:", L)


huffman(S, F)
