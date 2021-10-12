def maxspan(A):
    n = len(A)
    mini = A[0]
    maxi = A[0]
    for i in range(n):
        mini = min(mini, A[i])
        maxi = max(maxi, A[i])

    B = [[] for _ in range(n)]
    x = (maxi + mini) / n

    for i in range(n):
        d = int((A[i] - mini) / x)
        B[d].append(A[i])

    result = 0
    prev_max = max(B[0])
    for i in range(1, n):
        if len(B[i]) != 0:
            act_min = min(B[i])
            result = max(result, act_min - prev_max)
            prev_max = max(B[i])

    return result

if __name__ == '__main__':
    A = [0.5, 0.3, 0.01, 0.7, 0.2, 0.92, 0.11, 0.91]
    print(maxspan(A))