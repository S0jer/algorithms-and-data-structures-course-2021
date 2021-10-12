# Traspozycja

from math import inf

def trans_M(G):
    n = len(G)
    m = len(G[0])

    dp = [[-1 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            dp[j][i] = G[i][j]

    return dp


# def g_krawedziowy(G):
#     n, cnt = len(G), 0
#
#     for i in range(n):
#         for j in range(len(G[i])):
#             G[i][j] = [G[i][j], inf]
#
#
#     for i in range(n):
#         for j in range(len(G[i])):
#             if G[i][j][1] == inf:
#                 print(G[i][j])
#
#                 G[i][j] = [G[i][j][0], cnt]
#                 c = 0
#                 while c < len(G[j]) and G[j][c][0] != i:
#                     c += 1
#                 if c < len(G[j]) and G[j][c][1] == inf and G[j][c][0] == i:
#                     print(G[j][c])
#                     G[j][c] = [G[j][c][0], cnt]
#
#                 cnt += 1
#
#     dp = [[] for _ in range(cnt + 1)]
#
#     for i in range(n):
#         for j in G[i]:
#             for z in G[j[0]]:
#                 if i != z:
#                     if z[1] not in dp[G[i][0][1]]:
#                         dp[G[i][0][1]].append(z[1])
#                     if G[i][0][1] not in dp[z[1]]:
#                         dp[z[1]].append(G[i][0][1])
#
#     for i in dp:
#         print(i)

def g_krawedziowy(G):
    n, cnt = len(G), 0

    for i in range(n):
        for j in range(len(G[i])):
            G[i][j] = [G[i][j], inf]


    for i in range(n):
        for j in range(len(G[i])):
            if G[i][j][1] == inf:
                G[i][j] = [G[i][j][0], cnt]
                cnt += 1

    dp = [[] for _ in range(cnt + 1)]

    for i in range(n):
        for j in G[i]:
            for z in G[j[0]]:
                if i != z:
                    dp[G[i][0][1]].append(z[1])
                    dp[z[1]].append(G[i][0][1])

    return dp


G = [[1, 2, 3],
     [1, 2, 3]]

graph = [[1, 2], [2, 3], [], [4, 6], [], [], [], [3], [7]]

G_1 = [[1, 2, 3],
       [0, 4],
       [0, 3, 5],
       [0, 2, 4, 5],
       [1, 3, 5],
       [2, 3, 4]]
trans_M(G)

print(g_krawedziowy(graph))
