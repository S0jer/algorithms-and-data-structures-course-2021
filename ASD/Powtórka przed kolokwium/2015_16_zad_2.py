# . struct field { int value; int long j; int short j; };
# Z każdego pola można skakać tylko o ilość pól zapisaną w long j lub short j. Napisać program
# który zwróci maksymalną wartość jaką możemy osiągnąć poprzez przejście z pola 0 do n-1.
# Można założyć że z każdego pola da się dojść do pola n-1.


def field(A):
    n = len(A[0])
    dp = [-1] * n

    dp[0] = A[0][0]

    for i in range(n):
        x = i + A[1][i]
        y = i + A[2][i]
        if x < n:
            dp[x] = max(dp[x], dp[i] + A[0][x])
        if y < n:
            dp[y] = max(dp[y], dp[i] + A[0][y])


    print(dp[n - 1])

    return dp[n - 1]


A = [[5, 1, 3, 6, 1, 4, 3, 1, 5, 1, 0],
     [2, 1, 2, 2, 2, 4, 1, 2, 4, 1, 0],
     [3, 2, 4, 6, 2, 4, 3, 4, 6, 2, 0]]

field(A)
