# Zadanie 5. (suma odległości) Dana jest posortowana tablica A zawierająca n liczb i celem jest wyznaczenie
# liczby x takiej, że wartość ∑ n−1 i=0 ∣A[i] − x∣ jest minimalna. Proszę zaproponować algorytm, uzasadnić
# jego poprawność oraz ocenić złożoność obliczeniową.


def sums(A):
    n, a = len(A), 0

    for i in range(n):
        a += A[i]
    s = a / n

    r_min, x = abs(s - A[0]), A[0]
    for j in range(n):
        if r_min > abs(s - A[j]):
            r_min = abs(s - A[j])
            x = A[j]

    result = 0
    for z in range(n):
        result += abs(A[z] - x)

    return result


A = [5, 6, 15, 21, 13, 16, 25, 30, 34]

print(sums(A))
