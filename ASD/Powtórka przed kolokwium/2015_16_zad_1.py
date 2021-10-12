# 1. Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest
# możliwa sekwencja ruchów spełniająca:
# - każdy ruch kończy się zbiciem skoczka
# - sekwencja kończy się gdy zostanie jeden skoczek.


def horse(T):
    n = len(T)
    h = 0

    for i in range(n):
        for j in range(n):
            if T[i][j] == 1:
                T[i][j] = h
                h += 1
            else:
                T[i][j] = -1

    G = [[0] * h for _ in range(h)]
    moves = [(1, -2), (2, -1), (2, 1), (1, 2)]

    for i in range(n):
        for j in range(n):
            if T[i][j] != -1:
                x = T[i][j]
                for m in moves:
                    if if_possible(i + m[0], j + m[1], n) == True:
                        y = T[i + m[0]][j + m[1]]
                        if y != -1:
                            G[x][y] = 1
                            G[y][x] = 1

    road = DFS(G)
    print(road)

    if len(road) == h:
        return True
    return False


def if_possible(x, y, n):
    if x < n and y < n: return True
    return False


def DFS(G):
    n = len(G)
    v = [-1] * n
    delete = []

    delete = DFSVisit(G, 0, v, delete)

    return delete


def DFSVisit(G, u, v, delete):
    v[u] = 1
    n = len(G)
    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            DFSVisit(G, i, v, delete)

    delete.append(u)

    return delete


A = [[0, 0, 0, 1, 0, 0, 1, 0],
     [0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 1, 0]]

print(horse(A))
