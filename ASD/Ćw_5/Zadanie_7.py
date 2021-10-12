# Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
# oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# znajdujący trasę o minimalnym koszcie.


def road(A):
    n = len(A)
    dp = [[0] * n for _ in range(n)]

    dp[0][0] = A[0][0]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + A[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + A[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j] + A[i][j], dp[i][j - 1] + A[i][j])

    return dp[n - 1][n - 1], dp


A = [[1, 100, 0, 0],
     [99, 2, 1, 0],
     [1, 2, 1, 0],
     [1, 2, 99, 2]]

B = [[4, 0, 2, 1],
     [0, 0, 2, 1],
     [1, 1, 0, 4],
     [0, 3, 0, 1]]

result, dp = road(A)

print(result)
for i in dp:
    print(i)
