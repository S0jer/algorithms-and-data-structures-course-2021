# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x
# , gdzie a to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
# Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
# zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej.
# Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność
# obliczeniową. Nagłówek funkcji fast sort powinien mieć postać:
from math import log


def fast_sort(tab, a):
    n = len(tab)
    for i in range(n):
        tab[i] = log(tab[i], a)

    tab = bucket_sort(tab)

    for j in range(n):
        tab[j] = a ** tab[j]
    return tab


def bucket_sort(T):
    n, idx, v_max, length = len(T), 0, 0, 0

    A = [[] for _ in range(11)]

    for i in range(n):
        A[int((T[i] * 10))].append(T[i])

    for j in range(len(A)):
        A[j] = selection_sort(A[j])
        for i in A[j]:
            T[idx] = i
            idx += 1

    return T


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


n = 8
T = [1.321928094887362, 1.321928094887362, 1.0, 1.5145731728297583, 1.7369655941662063, 1.3219280948873622,
     1.3219280948873623, 1.7369655941662062, 2]

print(fast_sort(T, 2))

flaga = False
for i in range(n - 1):
    if T[i] > T[i + 1]:
        print("Błąd!")
        flaga = True
        break

if flaga == False:
    print("OK!")
