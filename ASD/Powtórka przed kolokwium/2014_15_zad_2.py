# 2. Problem plecakowy - dwuwymiarowa wersja problemu - oprócz ciężaru jest wysokość towarów.
# {p1, ..., pn} - przedmioty v | (pi) - wartość przedmiotu pi | r(pi) - ciężar przedmiotu pi | h(pi) - wysokość przedmiotu pi
# Jaka jest największa możliwa sumaryczna wartość przedmiotów, których ciężar
# nie przekracza M a wysokość S? Oszacować złożoność i udowodnić poprawność algorytmu.


def knapsack3D(W, V, H, MaxW, MaxH):
    n = len(W) + 1
    F = [None] * n

    for i in range(n):
        F[i] = [0] * (MaxW + 1)

    for w in range(W[0], MaxW + 1):
        F[0][w] = (V[0], H[0])

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = (F[i - 1][w][0], F[i - 1][w][1])
            if w >= W[i]:
                if F[i][w][1] <= MaxH and F[i - 1][w - W[i]][1] + H[i] <= MaxH:
                    if F[i][w][0] > F[i - 1][w - W[i]][0] + V[i]:
                        pass
                    else:
                        F[i][w] = (F[i - 1][w - W[i]][0] + V[i], F[i - 1][w - W[i]][1] + H[i])

                F[i][w] = max(F[i][w][0], F[i - 1][w - W[i]][0] + V[i])
