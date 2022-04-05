# Paweł Jaśkowiec, 406165
#
# Pomysł polega na przekształceniu tablicy T w celu zapamiętania na jakich indeksach znajduję się pierwotnie liczby
# następnie sortuję po wartościach używając mergesorta ze względu na to że jest to stabilne sortowanie
# mając liczby na odpowiednich miejscach porównuję liniowo indeksy na których są aktualnie a na których znajdowały się
# przed posortowaniem aby odnaleźć k maksymalne.

# Złożoność: n*log(n)


from zad1testy import runtests


def chaos_index(T):
    n = len(T)

    for i in range(n):
        T[i] = (T[i], i)

    T = mergesort(T)

    k_max = 0
    for i in range(n):
        if abs(T[i][1] - i) > k_max:
            k_max = abs(T[i][1] - i)

    return k_max


def merge(L, R):
    i, j, z, result = 0, 0, 0, []
    while i < len(L) and j < len(R):
        if L[i][0] <= R[j][0]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
        z += 1

    if j < len(R):
        result += R[j:]
    elif i < len(L):
        result += L[i:]

    return result


def mergesort(T):
    if len(T) <= 1:
        return T
    half = len(T) // 2
    L = mergesort(T[:half])
    R = mergesort(T[half:])

    return merge(L, R)


runtests(chaos_index)
