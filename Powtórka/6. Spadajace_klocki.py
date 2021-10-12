# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
# [a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości w tam, który spadł tuż przed nim.


def block(A):
    n = len(A)
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if A[j][0] <= A[i][0] and A[j][1] >= A[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    result = n - max(dp)

    return result


A = [(1, 4), (2, 3), (1, 99), (1, 2), (2, 9), (3, 5), (2, 6), (2, 4)]
print(block(A))

# dp[i] = max(dp[i], dp[j] + 1)
# najdluzszy ciag klockow, z ktorych kazdy
# jest zawarty w poprzednich, konczacy sie na i
