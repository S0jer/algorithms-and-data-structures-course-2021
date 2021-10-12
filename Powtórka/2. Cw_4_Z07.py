# Zadanie 7. Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. Proszę podać
# możliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów
# A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna (innymi słowy,
# szukamy najkrótszego przedziału z wszystkimi kolorami).


def colors(A, k):
    n, i, j, cnt = len(A), 0, -1, 0
    col = [0 for _ in range(k + 1)]

    while cnt < k:
        j += 1
        if col[A[j]] == 0:
            col[A[j]] += 1
            cnt += 1
        else:
            col[A[j]] += 1

    distance = j - i
    i_w, j_w = i, j

    while j < n and i < n:
        if col[A[i]] - 1 > 0:
            col[A[i]] -= 1
            i += 1
        else:
            j += 1
            if j < n:
                col[A[j]] += 1

        if j - i < distance:
            distance = j - i
            i_w, j_w = i, j

    return i_w, j_w


A_1 = [1, 2, 1, 2, 2, 2, 1, 1]
print(colors(A_1, 2))

T = [1, 2, 3, 1, 2, 4, 3, 2, 5, 3, 3, 1]
print(colors(T, 5))
