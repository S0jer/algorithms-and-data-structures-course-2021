from queue import PriorityQueue


def which_edge(G, E, s, t):
    dp_s = dijkstry(G, s)
    dp_t = dijkstry(G, t)

    r, r_max, edge = 0, 0, E[0]

    for i in range(len(E)):
        r_1 = dp_s[t] - (dp_s[E[i][0]] + E[i][2] + dp_t[E[i][1]])
        r_2 = dp_s[t] - (dp_s[E[i][1]] + E[i][2] + dp_t[E[i][0]])
        if r_1 > r_max or r_2 > r_max:
            r_max = r
            edge = E[i]

    return edge


def dijkstry(G, s):
    n = len(G)
    Q = PriorityQueue()

    dp = [100000] * n
    p = [-1] * n

    dp[s] = 0
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()

        for i in range(n):
            if dp[i] > dp[u[1]] + G[u[1]][i] and G[u[1]][i] != -1:
                Q.put((G[u[1]][i], i))
                dp[i] = dp[u[1]] + G[u[1]][i]
                p[i] = u[1]

    return dp


G = [[-1, 3, 5, -1, -1, -1, -1],
    [3, -1, -1, 7, -1, -1, -1],
    [5, -1, -1, 3, -1, -1, -1],
    [-1, 7, 3, -1, 10, 9, -1],
    [-1, -1, -1, 10, -1, -1, 4],
    [-1, -1, -1, 9, -1, -1, 2],
    [-1, -1, -1, -1, 4, 2, -1]]

E = [(0, 3, 13), (1, 4, 2), (4, 5, 37), (0, 6, 1), (2, 5, -2)]

print(which_edge(G, E, 0, 6))
