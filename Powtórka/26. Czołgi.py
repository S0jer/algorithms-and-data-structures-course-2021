# Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
# jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
# (1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.
# (2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo
# cenę za litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.
# (3) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna

from math import inf


def tank_1(L, S, t):
    cnt, position, fuel, idx = 0, 0, L, -1
    tank = []

    while position < t:

        if position + fuel >= t:
            return cnt, tank
        elif position + L >= t:
            tank.append(idx)
            return cnt + 1, tank

        if S[idx + 1] <= position + fuel:
            idx += 1
            fuel -= S[idx] - position
            position = S[idx]

        elif S[idx + 1] <= position + L:
            tank.append(idx)
            idx += 1
            cnt += 1
            fuel = L
            fuel -= (S[idx] - position)
            position = S[idx]

        elif S[idx + 1] > position + L:
            return False

    return cnt, tank


def tank_2(L, S, P, t):
    cnt, position, fuel, idx, idx_min = 0, 0, L, -1, 0
    tank, cost = [], 0
    n = len(S)

    while position < t:

        if idx + 1 < n:
            c_min = P[idx + 1]
            idx_min = idx + 1
            a = idx
            while a + 1 < n and position + L >= S[a + 1]:
                a += 1
                if P[a] < c_min:
                    idx_min = a
                    c_min = P[a]

        if P[idx_min] >= P[idx]:
            cost += P[idx] * (L - fuel)
            fuel = L
            tank.append(idx)
            idx = idx_min
            fuel -= S[idx] - position
            position = S[idx]


        elif P[idx] > P[idx_min]:

            if position + fuel >= S[idx_min]:
                idx = idx_min
                fuel -= S[idx] - position
                position = S[idx]

            else:
                to_tank = S[idx_min] - position - fuel
                cost += P[idx] * to_tank
                fuel = 0
                tank.append(idx)
                idx = idx_min
                position = S[idx]

        if position + fuel >= t:
            return cost, tank
        elif position + L >= t:
            if idx == n - 1:
                tank.append(idx)
                cost += P[idx] * (t - (position + fuel))
                return cost, tank

    return cost, tank


def tank_3(L, S, P, t):
    result, n = inf, len(S)
    dp = [inf for _ in range(n + 1)]
    S, P = [0] + S, [0] + P
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if S[i] - S[j] <= L:
                dp[i] = min(dp[i], dp[j] + (S[i] - S[j]) * P[i])

    a = n
    while t - S[a] <= L:
        result = min(result, dp[a])
        a -= 1

    return result


def tank_3_road(L, S, P, t):
    result, n = inf, len(S)
    dp = [[inf, []] for _ in range(n + 1)]
    S, P = [0] + S, [0] + P
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if S[i] - S[j] <= L and dp[i][0] > dp[j][0] + (S[i] - S[j]) * P[i]:
                dp[i][0] = dp[j][0] + (S[i] - S[j]) * P[i]
                dp[i][1] = dp[j][1] + [j]

    a, result = n, n
    while t - S[a] <= L:
        if dp[result][0] > dp[a][0]:
            result = a
        a -= 1

    return dp[result]


P = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 6.9, 2.5, 2.021]
S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 33, 36, 42]
L = 10
t = 45

print(tank_1(L, S, t))

print(tank_2(L, S, P, t))
# 61,308

print(tank_3(L, S, P, t))

print(tank_3_road(L, S, P, t))
