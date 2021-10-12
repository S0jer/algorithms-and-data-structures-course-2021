# Zadanie 2. (wybór zadań z terminami) Mamy dany zbiór zadań T = {t1, . . . , tn}. Każde zadanie ti
# dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w
# terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie ti zostanie
# wykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrodę g(ti) (pierwsze wybrane
# zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi
# do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.


def tasks(T):
    n = len(T)
    T.sort(key=lambda T: T[1], reverse=True)

    idx = 0
    for i in range(n):
        if T[i][0] > idx:
            idx = T[i][0]
    idx += 1

    dp = [(0, 0) for _ in range(idx)]

    for j in range(n):
        if T[j][1] < dp[T[j][0]][1]:
            for i in range(T[j][0] - 1, -1, -1):
                if T[j][1] > dp[i][1]:
                    dp[i] = T[j]
        else:
            dp[T[j][0]] = T[j]

    result = 0
    for a in range(idx):
        result += dp[a][1]

    return result, dp


T = [(1, 2), (1, 8), (2, 6), (0, 5), (1, 2), (4, 4), (3, 5)]
print(tasks(T))
