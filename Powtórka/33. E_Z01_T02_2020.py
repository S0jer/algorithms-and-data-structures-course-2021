# Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
# większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
# energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
# szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
# (wartość przekąki dodaje się do aktualnej energii Zbigniewa).
# Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
# len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie. Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
# n-1 lub −1 jeśli nie jest to możliwe.


from math import inf


def frog(A):
    n = len(A)
    dp = [[[0, inf] for _ in range(1)] for _ in range(n)]
    dp[0].append([A[0], 0])

    d = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for z in range(len(dp[i])):
            for j in range(i + 1, min(i + dp[i][z][0] + 1, n)):
                k = j - i
                if dp[j][0][1] > dp[i][z][1] + 1:
                    dp[j][0][1] = dp[i][z][1] + 1
                    dp[j][0][0] = dp[i][z][0] - k + A[j]
                elif dp[i][z][0] - k + A[j] > dp[j][0][0] and j != n - 1:
                    dp[j].append([dp[i][z][0] - k + A[j], dp[i][z][1] + 1])

    if dp[n - 1][0][1] == inf:
        return -1

    return dp[n - 1][0][1]


A = [3, 4, 0, 3, 0, 0, 0, 0, 0]
B = [2, 2, 1, 0, 0, 0]  # 3
C = [4, 5, 2, 4, 1, 2, 1, 0]  # 2

result = frog(A)
print(result)
