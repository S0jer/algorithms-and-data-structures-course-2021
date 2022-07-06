from queue import PriorityQueue

# To nie działa, dynamik w "ASD_2022/Egz_kol/Egz_2020/egzamin_popr_1_szablony/zad1.py"
def zaba_monika(M, L, x, y):
    G, s, e = create_g(M, L, x, y)
    Q = PriorityQueue()

    for i in G:
        print(i)


    Q.put((0, s, 2 * L))

    while not Q.empty():
        u = Q.get()


        for i in range(len(G[u[1]])):

            if G[u[1]][i][1] == 2 * L and u[2] >= G[u[1]][i][1]:
                Q.put((u[0] + 1, G[u[1]][i][0], L / 2))

            elif G[u[1]][i][1] == L and u[2] >= G[u[1]][i][1]:
                Q.put((u[0] + 1, G[u[1]][i][0], 2 * L))

            elif G[u[1]][i][1] == L / 2 and u[2] >= G[u[1]][i][1]:
                Q.put((u[0] + 1, G[u[1]][i][0], 2 * L))

        if u[1] == e:
            return u[0]

    return None


def create_g(M, L, x, y):
    s, e = 0, 0
    n = len(M)
    G = [[]] * n

    for i in range(n):
        for j in range(n):
            l = euklidesowa(M[i], M[j])

            if L / 2 >= l and i != j:
                G[i] = G[i] + [(j, L / 2)]
            elif L >= l > L / 2 and i != j:
                G[i] = G[i] + [(j, L)]
            elif 2 * L >= l > L and i != j:
                G[i] = G[i] + [(j, 2 * L)]

        if M[i] == x:
            s = i
        if M[i] == y:
            e = i

    return G, s, e


def euklidesowa(a_0, a_n):
    result = ((a_n[0] - a_0[0]) ** 2 + (a_n[1] - a_0[1]) ** 2) ** (1 / 2)
    return result


M = [(1, 3), (2, 1), (2, 4), (6, 6), (7, 4), (8, 6), (4, 1), (2, 6), (8, 8), (6, 3), (4, 7)]
L = 2

print(zaba_monika(M, L, (2, 1), (4, 7)))
