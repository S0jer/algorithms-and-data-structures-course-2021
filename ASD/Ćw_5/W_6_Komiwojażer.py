def bitonicTSP(C):
    n = len(C)
    City = []
    D = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            D[i][j] = distance(C[i][1], C[i][2], C[j][1], C[j][2])

    F = [[10000] * n for _ in range(n)]
    F[0][1] = D[0][1]

    for i in range(0, n - 2):
        tspf(i, n - 1, F, D)

    i = 0
    a = 0
    best_prev = 10000
    while i < n - 1:
        best = F[i][n - 1] + D[i][n - 1]
        if best < best_prev:
            best_prev = best
            a = i
        i += 1
    result = F[a][n - 1] + D[a][n - 1]

    City = read(C, F, D, a, result)

    print(C)
    print(City)
    print(result)


def read(C, F, D, a, result):
    n = len(C)
    idi = [[] for _ in range(11)]
    idx = []
    sums = [10000] * 11
    City = []
    u = [0] * n
    z = 0

    while F[a][z] == 10000:
        z += 1

    for x in range(n - 1, z - 1, -1):
        if x != z:
            result -= D[x - 1][x]
        City.append(C[x][0])
        if x != n - 1 and x != z:
            u[x] = 1

    idi, sums = get_sum(D, z, F[z][z + 1], sums, idx, idi)
    idi, u = match(D, idi, u)
    u[n - 1] = 1
    u[z] = 1
    u[0] = 0

    s = len(u) - 1

    while u[s] != 0:
        s -= 1

    check_1 = D[idi[0]][z] + D[s][n - 1]
    check_2 = D[idi[0]][n - 1] + D[s][z]

    if check_2 > check_1:
        for a in idi:
            City.append(C[a][0])
        City = City[::-1]

        for b in range(len(u) - 1, -1, -1):
            if u[b] == 0:
                City.append(C[b][0])
    else:
        for b in range(len(u) - 1, -1, -1):
            if u[b] == 0:
                City.append(C[b][0])
        City = City[::-1]
        for a in idi:
            City.append(C[a][0])

    return City


def get_sum(D, a, sum, sums, idx, idi):
    if a != 0:
        for x in range(a - 1, -1, -1):
            get_sum(D, x, sum - D[x][a], sums, idx + [x], idi)
    if sum > 0 and a == 0 and sum < sums[int(sum % 10)] and len(idx) > 1:
        sums[int(sum % 10)] = sum
        idi[int(sum % 10)] = idx
    return idi, sums


def match(D, idi, u):
    i_min, u_min = 0, []
    suma_min = 10000
    for i in range(len(idi)):
        suma = 0
        c = u[:]
        for j in range(len(idi[i])):
            if j != 0:
                suma += D[j - 1][j]
            c[idi[i][j]] = 1
        prev = -1
        x = c[:]
        for k in range(len(c)):
            if c[k] == 0:
                if prev != -1:
                    suma += D[prev][k]
                    prev = k
                    c[k] = 1
                else:
                    prev = k
                    c[k] = 1
        if suma < suma_min and suma != 0:
            suma_min = suma
            i_min = i
            u_min = x

    return idi[i_min], u_min


#
# def read(C, F, D, a):
#     n = len(C)
#     City = []
#     u = [0] * n
#     z = 0
#
#     while F[a][z] == 10000:
#         z += 1
#
#     for x in range(n - 1, z - 1, -1):
#         City.append(C[x][0])
#         u[x] = 1
#
#     if C[a][2] > C[0][2]:
#         c = 1
#     elif C[a][2] < C[0][2]:
#         c = 0
#
#     print(City)
#
#     while a != 1:
#         nxt = a - 1
#         print(get_sum(D, nxt, z, 0, [], []))
#         best = min(get_sum(D, nxt, z, 0, [], []))
#
#         for y in range(a - 1, 0, -1):
#             check = min(get_sum(D, y, z, 0, [], []))
#             print(get_sum(D, y, z, 0, [], []), y, c)
#             print(check, best)
#             if check < best and C[nxt][2] < C[y][2] and c == 1:
#                 best = check
#                 nxt = y
#             elif check < best and C[nxt][2] > C[y][2] and c == 0:
#                 best = check
#                 nxt = y
#             elif check == best and C[nxt][2] >= C[y][2] and c == 1:
#                 best = check
#                 nxt = y
#             elif check == best and C[nxt][2] <= C[y][2] and c == 0:
#                 best = check
#                 nxt = y
#
#         a = nxt
#         z = nxt + 1
#         u[nxt] = 1
#         City.append(C[nxt][0])
#         print(City)
#
#     City.append(C[0][0])
#     City.reverse()
#
#     for i in range(n - 1, -1, -1):
#         if u[i] != 1:
#             City.append(C[i][0])
#
#     return City
#
#
#
#
#
#
# def get_sum(D, a, z, sum, sums, idx):
#     if a != 0:
#         for x in range(a - 1, -1, -1):
#             get_sum(D, x, a, sum + D[x][a], sums, idx + [x])
#     if sum != 0 and a == 0:
#         sum += D[0][z]
#         sums.append(sum)
#         idx.append(0)
#     print(idx)
#     return sums, idx


def tspf(i, j, F, D):
    if F[i][j] != 10000:
        return F[i][j]
    if i == j - 1:
        best = 10000
        for k in range(j - 1):
            best = min(best, tspf(k, j - 1, F, D) + D[k][j])
        F[j - 1][j] = best
    else:
        F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]
    return F[i][j]


def distance(x_1, y_1, x_2, y_2):
    a = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** (1 / 2)
    return a


def printT(A):
    for i in A:
        print(i)


if __name__ == '__main__':
    # C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], ["Paprykarz Szczeciński", 1, 3], ["Rzeszów", 1.5, 1.5], ["Przeworsk", 0.1, 1.8]]
    # C = [['A', 0, 0], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],
    #   ['Res', 0.5, 2.5], ['J', 1.5, 3.5]]
    # C = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3], ["F", 0.5, -2]]
    # C = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
    #     ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
    #    ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]
    C.sort(key=lambda C: C[1])
    print(C)
    bitonicTSP(C)
    # Wrocław, Rzeszów, Kraków, Warszawa, Gdańsk, paprykarz, Wrocław
    # A Res J H D E G F C B A
    # A F D B C E A
    # *, W, s, e, i, b, j, U, s, a, W, h, c, i, k, t, e, s, y, z, *
