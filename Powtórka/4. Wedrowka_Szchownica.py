# Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
# oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# znajdujący trasę o minimalnym koszcie


def chessBoard(A, s, k):
    n = len(A)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    dp[s[0]][s[1]] = A[s[0]][s[1]]

    for i in range(max(1, s[1]), n):
        dp[s[0]][i] = dp[s[0]][i - 1] + A[s[0]][i]

    for i in range(max(1, s[0]), n):
        dp[i][s[1]] = dp[i - 1][s[1]] + A[i][s[1]]

    for i in range(max(1, s[0] + 1), n):
        for j in range(max(1, s[1] + 1), n):
            dp[i][j] = A[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    result = dp[k[0]][k[1]]
    for i in dp:
        print(i)

    return result


A = [[1, 100, 0, 0],
     [99, 2, 1, 0],
     [1, 2, 1, 0],
     [1, 2, 99, 2]]

B = [[4, 0, 2, 1],
     [0, 0, 2, 1],
     [1, 1, 0, 4],
     [0, 3, 0, 1]]

print(chessBoard(B, (0, 0), (3, 3)))

