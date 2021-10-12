# Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi, w którym z nich należy
# wybudować dom, tak aby suma euklidesowych odległości od tego punktu do wszystkich pozostałych była minimalna.
# Należy zwrócić również tę sumę. Algorytm powininen być jak najszybszy.

from random import randint


def search_where(A, i, j, best):
    if j - i > 1:
        half = (i + j) // 2

        l, r, sum_l, sum_r = 0, len(A) - 1, 0, 0
        while l < half or r > half:
            if r > half:
                sum_r += (A[r] - A[half])
                r -= 1
            if l < half:
                sum_l += (A[half] - A[l])
                l += 1

        if best[1] > sum_r + sum_l or best[1] == 0:
            best = (half, sum_r + sum_l)

        if sum_l > sum_r:
            return search_where(A, i, half, best)
        else:
            return search_where(A, half, j, best)

    l, r, sum_l, sum_r = 0, len(A) - 1, 0, 0
    while l < i or r > i:
        if r > i:
            sum_r += (A[r] - A[i])
            r -= 1
        if l < i:
            sum_l += (A[i] - A[l])
            l += 1

    if best[1] > sum_r + sum_l:
        best = (i, sum_r + sum_l)

    return best




if __name__ == '__main__':
    A = [randint(1, 70) for _ in range(15)]
    A.sort()
    # A = [1, 4, 9, 10, 15, 30, 35, 42, 50, 51]
    print(A)
    print(search_where(A, 0, len(A), (0, 0)))
