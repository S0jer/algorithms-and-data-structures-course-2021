from math import inf


def tank_1(F, B, d):
    cnt, a, d_f, n = 0, 0, d, len(B)
    road = 0
    while a < n:

        if road + d >= F:
            return cnt
        elif road + d_f >= F:
            return cnt + 1

        if road + d < F and a == n - 1:
            return False

        if B[a + 1] - B[a] > d_f:
            return False

        if d - (B[a + 1] - B[a]) >= 0:
            d -= (B[a + 1] - B[a])
            a += 1
            road = B[a]
        elif d - (B[a + 1] - B[a]) < 0:
            d = d_f
            cnt += 1


def tank_1b(F, B, C, d):
    n = len(B)
    d_f = d
    a_1, a_2 = 1, 1
    prize, road, a = 0, B[0], 0
    d -= B[0]

    while a < n - 1 and B[a] < F:

        if road + d >= F:
            return prize

        if B[a + 1] - B[a] > d_f:
            return False

        x = a + 1
        a_1 = a + 1
        c_min_1 = C[a]
        c_min_2 = C[a_1]
        while x < n and B[x] - B[a] < d_f:
            if C[x] < c_min_2:
                c_min_2 = C[x]
                a_1 = x
            x += 1

        if c_min_1 < c_min_2:
            prize += (d_f - d) * C[a]
            d = d_f
            d -= (B[a_1] - B[a])
        else:
            if d - (B[a_1] - B[a]) >= 0:
                d -= (B[a_1] - B[a])
                prize += (d_f - d) * C[a_1]
                d = d_f
            else:
                need = abs(d - (B[a_1] - B[a]))
                prize += need * C[a]
                d = 0
                if a_1 != n - 1:
                    prize += d_f * C[a_1]
                    d = d_f
        a = a_1
        road = B[a_1]
    if road + d >= F:
        return prize
    elif road + d_f >= F:
        prize += (F - road - d) * C[a]
        return prize
    else:
        return False


def tank_2b(d, S, P, L):
    wynik = inf
    n = len(S)
    dp = [inf for _ in range(n + 1)]
    dp[0] = 0
    S = [0] + S
    P = [0] + P

    for i in range(1, n + 1):
        j = i - 1
        while j >= 0 and S[i] - S[j] <= L:
            dp[i] = min(dp[i], dp[j] + (S[i] - S[j]) * P[i])
            j -= 1

    j = n
    while d - S[j] <= L:
        wynik = min(wynik, dp[j])
        j -= 1

    print(dp, wynik)


L = 10
S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 33, 36, 42]
P = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 6.9, 2.5, 2.021]
t = 45

# L = 10
# S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# P = [2, 1, 2, 3, 3, 1, 1, 3, 2, 2, 1, 2, 2, 3, 2, 3, 3, 1, 1, 2]
# t = 21

print(tank_1(t, S, L))
