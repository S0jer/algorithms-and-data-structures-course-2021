# Zadanie 3. (szukanie sumy) Dana jest posortowana tablica A[1...n] oraz liczba x.
# Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.


def search_sum(T, x):
    i, j = 0, len(T) - 1
    while i < j:
        if T[i] + T[j] == x:
            return True
        if T[i] + T[j] > x:
            j -= 1
        if T[i] + T[j] < x:
            i += 1
    return False


if __name__ == '__main__':
    T = [1, 3, 5, 8, 13, 15, 27, 35, 47, 50]
    x = 11
    print(search_sum(T, x))
