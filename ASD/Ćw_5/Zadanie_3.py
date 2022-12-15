# Zadanie 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
# długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n^2).


def longest(A, B):
    n = max(len(A), len(B))
    dp = [[0] * (n) for _ in range(n)]
    R = A[:]
    l = 0

    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                A[i] = -1
                B[j] = 1
                dp[i][j] = 1


    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] == 1:
                l += 1
                print(R[i], end='')
                break
    print("\n", l)


A = ['D', 'D', 'A', 'M', 'Res', 'A', 'N', 'D']
B = ['X', 'D', 'Res', 'N', 'D']
longest(A, B)
