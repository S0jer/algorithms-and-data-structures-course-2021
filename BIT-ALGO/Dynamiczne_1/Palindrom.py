# Najdłuższy palindrom


def palindrom(A):
    n = len(A)
    P = []
    p_max = ''

    for i in range(2, n - 1):

        if A[i - 2] == A[i]:
            search = find_palindrom(A, i - 2, i)

            if len(search) > len(p_max):
                p_max = search
            P.append(search)

        elif A[i - 1] == A[i]:
            search = find_palindrom(A, i - 1, i)

            if len(search) > len(p_max):
                p_max = search
            P.append(search)



    print(P)
    print(p_max)


def find_palindrom(A, s, k):
    while s > -1 and k < len(A) and A[s] == A[k]:
        k += 1
        s -= 1

    search = A[s + 1:k]

    return search


A = "sebastitsantaaaabbaa"
B = "aaaaaaaaaaaaaaaaaaa"

palindrom(A)
palindrom(B)
