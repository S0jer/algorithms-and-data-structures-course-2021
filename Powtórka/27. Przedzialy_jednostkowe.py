# Zadanie 1. (pokrycie przedziałami jednostkowymi) Dany jest zbiór punktów X = {x1, . . . , xn} na
# prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
# potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
# przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).


def sections(X):
    X.sort()
    n = len(X)
    cnt, border = 0, 0
    for i in range(n):
        if X[i] > border:
            cnt += 1
            border = X[i] + 1

    return cnt


X = [0.25, 0.5, 1.6, 0.3, 2.7, 3.8, 4.2]

print(sections(X))
