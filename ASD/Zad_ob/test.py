def lis(A):
    n = len(A)
    F = [1] * n
    P = [[-1] for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1

    for i in range(1, n):
        for j in range(i):
            if F[j] + 1 == F[i] and A[j] < A[i]:
                if P[i] == [-1]:
                    P[i] = [j]
                else:
                    P[i].append(j)

    return (max(F), F, P)


count = 0


def print_all_solution(A, F, P, max_value):
    global count

    def print_solution(A, P, i, result, idx):
        global count
        if P[i] == [-1]:
            result[idx].append(A[i])
            result[idx].reverse()
            count += 1
            print(count)

        elif len(P[i]) == 1 and P[i] != [-1]:
            result[idx].append(A[i])
            print_solution(A, P, P[i][0], result, idx)

        else:
            result[idx].append(A[i])
            tmp = result[idx].copy()
            print_solution(A, P, P[i][0], result, idx)
            new_idx = idx + 1
            for j in range(1, len(P[i])):
                result.append(tmp)
                print_solution(A, P, P[i][j], result, new_idx)
                new_idx += 1

    for i in range(len(F)):
        if F[i] == max_value:
            print_solution(A, P, i, [[]], 0)

    print(count)

A = [10 * k + i for k in range(8) for i in range(6, 0, -1)]
max_value, F, P = lis(A)
print_all_solution(A, F, P, max_value)