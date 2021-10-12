from queue import PriorityQueue


def payment(G, s, t):
    n = len(G)
    Q = PriorityQueue()
    road, cost = [], 0

    v = [-1] * n
    dp = [-100000] * n
    p = [-1] * n

    dp[s] = 0
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()
        v[u[1]] = 1

        for i in range(len(G[u[1]])):

            if v[G[u[1]][i][0]] == -1 and (dp[G[u[1]][i][0]] > max(G[u[1]][i][1], u[0]) or dp[G[u[1]][i][0]] < 0):
                dp[G[u[1]][i][0]] = max(G[u[1]][i][1], u[0])
                Q.put((dp[G[u[1]][i][0]], G[u[1]][i][0]))
                p[G[u[1]][i][0]] = u[1]


        if u[1] == t:
            road = get_road(p, t)
            cost = u[0]
            break

    return road[::-1], cost


def get_road(p, s):
    road = [s]
    while p[s] != -1:
        road.append(p[s])
        s = p[s]

    return road


G = [[(1, 60), (3, 120)],
     [(0, 60), (2, 80)],
     [(1, 80), (4, 70)],
     [(0, 120), (5, 30), (4, 150)],
     [(2, 70), (3, 150)],
     [(3, 30)]]

print(payment(G, 0, 5))
