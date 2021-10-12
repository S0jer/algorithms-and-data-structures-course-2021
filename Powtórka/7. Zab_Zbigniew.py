# Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
# wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
# jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
# niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
# dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
# skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
# każdej z liczb.

from math import inf


def frog(A):
    n = len(A)
    dp = [[[0, inf] for _ in range(1)] for _ in range(n)]
    dp[0].append([A[0], 0])


    for i in range(n):
        for z in range(len(dp[i])):
            for j in range(i + 1, min(i + dp[i][z][0] + 1, n)):
                k = j - i
                if dp[j][0][1] > dp[i][z][1] + 1:
                    dp[j][0][1] = dp[i][z][1] + 1
                    dp[j][0][0] = dp[i][z][0] - k + A[j]
                elif dp[i][z][0] - k + A[j] > dp[j][0][0] and j != n - 1:
                    dp[j].append([dp[i][z][0] - k + A[j], dp[i][z][1] + 1])

    for i in dp:
        print(i)

    return dp[n - 1][0][1]


A = [3, 4, 0, 3, 0, 0, 0, 0, 0]
B = [2, 2, 1, 0, 0, 0]  # 3
C = [4, 5, 2, 4, 1, 2, 1, 0]  # 2

result = frog(B)
print(result)
