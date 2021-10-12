from queue import PriorityQueue


def easy_way(G):
    n = len(G)
    max_len = 0
    road = []

    for s in range(n):
        if len(G[s]) <= 2:
            Q = PriorityQueue()
            v = [-1] * n
            dp = [-100000] * n
            p = [-1] * n

            dp[s] = 0
            Q.put((0, s))

            while not Q.empty():
                u = Q.get()
                v[u[1]] = 1
                for i in range(len(G[u[1]])):

                    if dp[G[u[1]][i][0]] < dp[u[1]] + G[u[1]][i][1] and len(G[G[u[1]][i][0]]) <= 2 and \
                            v[G[u[1]][i][0]] == -1:
                        dp[G[u[1]][i][0]] = dp[u[1]] + G[u[1]][i][1]
                        Q.put((dp[i] * (-1), G[u[1]][i][0]))
                        p[G[u[1]][i][0]] = u[1]

            max_p, idx_max = 0, 0
            for j in range(n):
                if dp[j] > max_p:
                    idx_max = j
                    max_p = dp[j]

            if max_p > max_len:
                max_len = max_p
                road = get_road(p, idx_max)


    return road[::-1], max_len


def get_road(p, s):
    road = [s]

    while p[s] != -1:
        road.append(p[s])
        s = p[s]

    return road


G = [[(1, 1), (6, 1)],
     [(0, 1), (2, 1), (6, 1)],
     [(1, 1), (3, 1)],
     [(2, 1), (4, 1)],
     [(3, 1), (5, 1)],
     [(4, 1), (6, 1)],
     [(0, 1), (5, 1), (1, 1)]]

G1 = [[(1, 1), (6, 1)],
      [(0, 1), (2, 1)],
      [(1, 1), (3, 1)],
      [(2, 1), (4, 1)],
      [(3, 1), (5, 1)],
      [(4, 1), (6, 1)],
      [(0, 1), (5, 1)]]

G2 = [[(1, 1), (6, 1)],
      [(0, 1), (2, 1), (6, 1)],
      [(1, 1), (3, 1)],
      [(2, 1), (4, 7)],
      [(3, 7), (5, 1)],
      [(4, 1), (6, 1)],
      [(0, 1), (5, 1), (1, 1)]]


print(easy_way(G))
print(easy_way(G1))
print(easy_way(G2))
