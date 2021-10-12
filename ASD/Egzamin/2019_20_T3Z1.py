from queue import PriorityQueue


def best_root(L):
    n = len(L)
    b_root = 0
    max_t = 100000
    for i in range(n):
        t = dijkstry(L,i)
        if max_t > t:
            max_t = t
            b_root = i

    return b_root


def dijkstry(G, s):
    n = len(G)
    Q = PriorityQueue()

    dp = [100000] * n
    v = [-1]*n

    dp[s] = 0
    Q.put((s))

    while not Q.empty():
        u = Q.get()
        v[u] = 1

        for i in range(len(G[u])):
            if dp[G[u][i]] > dp[u] + 1 and v[G[u][i]] == -1:
                Q.put((G[u][i]))
                dp[G[u][i]] = dp[u] + 1



    return max(dp)



L = [[2],
     [2],
     [0, 1, 3],
     [2, 4],
     [3, 5, 6],
     [4],
     [4]]


print(best_root(L))