# Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z
# tej tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne ). Napisz algorytm, który
# posortuje tablicę w czasie O(n).


def resort(A, k):
    U = []
    W = []
    i, id_w, id_u = 0, -1, -1
    while i <= len(A):
        if i < len(A) and A[i] > k:
            W.append(A[i])
            id_w += 1
            id_ws = id_w
            while id_ws > 0 and W[id_ws - 1] > W[id_ws]:
                W[id_ws - 1], W[id_ws] = W[id_ws], W[id_ws - 1]
                id_ws -= 1
            A.pop(i)
            if i != 0:
                i -= 1
        if i < len(A) and A[i] < 0:
            U.append(A[i])
            id_u += 1
            id_us = id_u
            while id_us > 0 and U[id_us - 1] > U[id_us]:
                U[id_us - 1], U[id_us] = U[id_us], U[id_us - 1]
                id_us -= 1
            A.pop(i)
            if i != 0:
                i -= 1
        else:
            i += 1
    A = U + A + W
    return A


if __name__ == '__main__':
    n = 11
    k = 15
    # A = [randint(0, k) for i in range(n)]
    A = [17, -5, 23, -10, -1, -6, 1, -2, 30, 64, 22]
    print(A)
    A = resort(A, k)
    print(A)
