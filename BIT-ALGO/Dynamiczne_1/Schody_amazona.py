# Zadanie 3: Rekurencyjne schody Amazona
# Dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. Początkowo stoimy na pozycji 0, wartość A[i]
# informuje nas jaka jest maksymalna długość skoku na następną pozycję.
# Przykład A = {1,3,2,1,0}
# Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4.
# Należy policzyć na ile sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy


def stairs(A, i):
    n = len(A)
    dp = [0 for _ in range(n)]
    dp[0] = 1

    for i in range(n):
        for j in range(i, min(A[i] + 1, n)):
            dp[i + j] += dp[i]

    print(dp)
    print(dp[i - 1])



A = [1, 3, 2, 1, 0]
stairs(A, 3)