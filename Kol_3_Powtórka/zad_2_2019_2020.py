from queue import PriorityQueue


def letters(E, L, W):
    n = len(E)
    w_len = len(W)
    min_len = 100000000

    for x in range(len(L)):
        if L[x] == W[0]:
            Q = PriorityQueue()

            dp = [100000] * n

            dp[x] = 0
            Q.put((0, x, 1))
            while not Q.empty():
                u = Q.get()
                if u[2] == w_len:
                    min_len = min(u[0], min_len)
                    break

                for i in range(n):

                    if E[i][0] == u[1] and L[E[i][1]] == W[u[2]]:
                        dp[E[i][1]] = dp[u[1]] + E[i][2]
                        Q.put((dp[E[i][1]], E[i][1], u[2] + 1))

                    elif E[i][1] == u[1] and L[E[i][0]] == W[u[2]]:
                        dp[E[i][0]] = dp[u[1]] + E[i][2]
                        Q.put((dp[E[i][0]], E[i][0], u[2] + 1))

    return min_len


L = ["k", "k", "o", "o", "t", "t"]
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
G = (L, E)
W = 'ktot'

print(letters(E, L, W))
