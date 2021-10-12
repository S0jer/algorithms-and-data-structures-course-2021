# Zadanie 7. Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. Proszę
# podać możliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów
# A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna (innymi słowy,
# szukamy najkrótszego przedziału z wszystkimi kolorami)


def zad(A, k):
    B = [0] * k
    x, i, j, kol = 0, 0, -1, 0
    y = len(A)
    while j < len(A) - 1:
        if kol == k:
            if j - i < y - x:
                x = i
                y = j
            B[A[i]] -= 1
            if B[A[i]] == 0:
                kol -= 1
            i += 1
        else:
            j += 1
            B[A[j]] += 1
            if B[A[j]] == 1:
                kol += 1
    while B[A[i]] > 1:
        B[A[i]] -= 1
        i += 1
    while B[A[j]] > 1:
        B[A[j]] -= 1
        j -= 1
    if j - i < y - x:
        return i, j
    return x, y


k = 3
A = [0, 0, 1, 1, 2, 2, 0, 0, 2, 2, 2, 2, 1, 0]
# A = [0, 0, 0, 1, 0, 1, 2, 3, 1, ]
print(zad(A, k))
