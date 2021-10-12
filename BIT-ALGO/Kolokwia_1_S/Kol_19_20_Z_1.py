# Zadania
# [2pkt.] Zadanie 1. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.


def count(x):
    A = [0] * 10
    while x != 0:
        A[x % 10] += 1
        x //= 10
    j = 0
    w = 0
    for i in A:
        if i == 1:
            j += 1
        elif i != 0:
            w += 1
    w = 9 - w
    result = 10 * j + w
    return result


def pretty_sort(T):
    X = [[] for _ in range(100)]
    for i in range(len(T)):
        X[count(T[i])].append(T[i])
    indeks = 0
    for i in range(len(X) - 1, 0, -1):
        j = 0
        while j < len(X[i]) and len(X[i]) != 0:
            T[indeks] = X[i][j]
            j += 1
            indeks += 1
    return T


T = [2344, 67333, 123, 114577, 1266, 455]
print(T)
T = pretty_sort(T)
print(T)
