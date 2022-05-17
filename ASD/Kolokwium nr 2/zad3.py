from zad3testy import runtests
from queue import PriorityQueue
from math import inf

# Paweł Jaśkowiec, 406165

# Pomysł polega na przechodzeniu ppo pierwszym wierszu i sprawdzaniu wielkości plamy kiedy mozna zatankować
# (w trakcie rrealizacji :()



def plan(T):
    n = len(T)
    stains = [0] * n

    for i in range(n):
        if T[0][i] != 0:
            stains[i] = BFS_tank(T, i, 0)


    result = []
    Q = PriorityQueue()
    Q.put(((-1) * stains[0], 0, [0]))

    while not Q.empty():
        u = Q.get()

        for i in range(u[1] + 1, min(u[1] + (-1) * u[0] + 1, n)):

            if stains[i] != 0:
                Q.put(((-1) * ((-1) * u[0] - (i - u[1]) + stains[i]), i, u[2] + [i]))

            if i == n - 1:
                result.append((u[2], u[1]))

    len_min, d_max, road = inf, 0, result[0][0]

    for i in range(len(result)):
        if len(result[i][0]) < len_min:
            len_min = len(result[i][0])
            road = result[i][0]
            d_max = result[i][1]

        elif len(result[i][0]) == len_min and d_max < result[i][1]:
            d_max = result[i][1]
            road = result[i][0]

    return road


def BFS_tank(G, j, ropa):
    Q = PriorityQueue()
    n = len(G)

    ropa += G[0][j]
    G[0][j] = 0

    Q.put((0, j))
    moves = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    while not Q.empty():
        u = Q.get()

        for m in moves:

            if if_possible(u[0] + m[0], u[1] + m[1], n) and G[u[0] + m[0]][u[1] + m[1]] != 0:
                ropa += G[u[0] + m[0]][u[1] + m[1]]
                G[u[0] + m[0]][u[1] + m[1]] = 0
                Q.put((u[0] + m[0], u[1] + m[1]))

    return ropa


def if_possible(i, j, n):
    if 0 <= i and i < n and 0 <= j and j < n: return True
    return False


T2 = [
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

T = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

runtests(plan)
