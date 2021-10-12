# Zadanie 6. Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
# znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
# że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
# których A[i + 1] − A[i] jest największe).


def pair(A):
    n = len(A)
    mini, maxi = A[0], A[0]
    B = [[] for _ in range(n)]
    for i in range(n):
        mini = min(mini, A[i])
        maxi = max(maxi, A[i])

    x = (mini + maxi) / n
    for i in range(n):
        ind = int(A[i] / x)
        B[ind].append(A[i])

    result = 0
    p_max = max(B[0])
    for i in range(1, n):
        if len(B[i]) != 0:
            p_min = min(B[i])
            if result < p_min - p_max:
                result = p_min - p_max
                p_1, p_2 = p_max, p_min
            p_max = max(B[i])

    return result, p_1, p_2


if __name__ == '__main__':
    A = [0.5, 0.3, 0.01, 0.7, 0.2, 0.92, 0.11, 0.91]
    print(pair(A))
