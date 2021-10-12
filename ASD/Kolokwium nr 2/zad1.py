from zad1testy import runtests


def select_buildings(T, p):
    T.sort(key=lambda T: T[2])
    n = len(T)

    road = []
    dp = [[0] * p for _ in range(n)]

    for a in range(T[0][3], p):
        dp[0][a] = students(T[0])

    for i in range(n):
        for z in range(p):
            for j in range(i):
                if z - T[i][3] > 0 and T[i][1] > T[j][2]:
                    dp[i][z] = max(students(T[i]) + dp[j][z - T[i][3]], dp[i - 1][z])


    road = recover(dp)

    return road


def recover(dp):
    n = len(dp)
    i = len(dp) - 1
    j = len(dp[i]) - 1
    max_w = 0
    for a in range(n):
        if dp[i][a] > max_w:
            max_w = dp[i][a]
            j = a

    solution = []
    while i >= 0 and j >= 0:
        if j - 1 >= 0 and dp[i][j - 1] == max_w:
            j -= 1

        elif i - 1 >= 0 and dp[i - 1][j] == max_w:
            i -= 1
        else:
            solution.append(i)
            i -= 1
            max_w = dp[i][j]


    return solution[::-1]




def students(u):
    result = abs(u[0] * (u[2] - u[1]))

    return result


T = [(2,1,5,3),(3,7,9,2),(2,8,11,1)]
R1 = [0,2]
p = 6

# print(select_buildings(T, p))

runtests(select_buildings)
