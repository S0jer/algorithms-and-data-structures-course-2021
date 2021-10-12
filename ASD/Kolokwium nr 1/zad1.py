# Paweł Jaśkowiec, 406165

# Tworzę tablice długości n^2 i przepisuję do niej wartości z tablicy T, następnie funkcją select znajduję
# wartości leżące w przedziale z którego zbuduję przekątną, następnie w funkcji for a dalej while przepisuję
# wartości mniejsze od początku przekątnej oraz większe od jej końca.

# Złożoność czasowa funkcji wynosi n^2 ze względu na przepisywanie wartości.

from zad1testy import runtests


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def select(A, p, r, k):
    if p == r:
        return
    q = partition(A, p, r)
    if q == k:
        return
    elif k < q:
        return select(A, p, q - 1, k)
    else:
        return select(A, q + 1, r, k)


def Median(T):
    A = []
    for z in range(len(T)):
        A += T[z]

    start = (len(T) ** 2 - len(T)) // 2
    end = len(T) ** 2 - len(T)
    select(A, 0, len(A) - 1, start)
    select(A, 0, len(A) - 1, end)
    median = -1
    before = 0
    minus = start + len(T) - end
    after = end + minus  # wyznaczam na której wartości kończy się "przekątna"
    check = start
    for j in range(len(T)):
        median += 1
        T[j][median] = A[check]
        check += 1
        i = 0
        while i < median and before < start:
            T[j][i] = A[before]
            before += 1
            i += 1
        a = median + 1
        while a < len(T) and after < len(A):
            T[j][a] = A[after]
            after += 1
            a += 1
    return


runtests(Median)
