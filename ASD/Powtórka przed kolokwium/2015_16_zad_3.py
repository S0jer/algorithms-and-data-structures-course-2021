# 3. Zbiór przedziałów {[a1, b1], ..., [an, bn]}, każdy przedział należy do [0, 1]. Opisać algorytm który
# sprawdzi czy jest możliwy taki wybór przedziałów, aby cały przedział [0, 1] zawierał się w
# wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.

def sections(A):
    n = len(A)
    A.sort(key=lambda A: A[1])

    if A[n - 1][1] < 1:
        return False

    i = 0
    for j in range(n):
        if A[j][0] == 0:
            i = j

    road = [A[i]]
    p = A[i]
    cnt = 1
    i_check = i

    while p[1] < 1:
        x = p
        for j in range(i, n):
            if A[j][0] > p[0] and A[j][0] < p[1] and A[j][1] > x[1]:
                x = A[j]
                i_check = j
        if p == x:
            return False

        p = x
        road.append(p)
        cnt += 1
        i = i_check

    print(road)

    return cnt


A = [(0, 0.15), (0.1, 0.25), (0.05, 0.4), (0.35, 0.6), (0.75, 0.85), (0.15, 0.3), (0.35, 0.7), (0, 0.25), (0.65, 0.95),
     (0.85, 1), (0.55, 0.8), (0.95, 1)]

B = [(0, 0.2), (0.25, 0.45), (0.4, 0.9), (0.8, 1)]

C = [(0, 0.15), (0.1, 0.25), (0.05, 0.4), (0.35, 0.6), (0.75, 0.85), (0.15, 0.3), (0.35, 0.7), (0, 0.25), (0.65, 0.95),
     (0.55, 0.8)]

print(sections(A))
print(sections(B))
print(sections(C))
