# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
# [a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości w tam, który spadł tuż przed nim.


def blocks(A):
    n = len(A)
    dp = [0]*n
    dp[0] = 1



    for i in range(1, n):
        for j in range(i - 1, -1, -1):
           if A[j][1] > A[i][0]:
               dp[i] -= 1


    print(dp)




A = [(1, 4), (2, 3), (1, 99), (2, 4), (1, 4), (2, 9), (3, 8), (4, 11), (4, 7), (9, 12)]
blocks(A)
