# Paweł Jaśkowiec, 406165


# Z przedzialow tworzymy punkty oznaczajace poczatek: (A[i][0], 0, A[i][1]) oraz koniec: (A[i][0], 1, inf)
# Dane punkty sortujemy oraz iterujemy po nich, zwiekszajac cnt o 1 jesli mamy poczatek zmniejszajac dla konca
# Jesli rozwazamy k przedzialow (cnt == k) to sprawdzamy czy dany przedzial jest wiekszy od poprzednio znalezionego
# Dla najwiekszego znalezionego przedizalu znajdujemy k przedzialow z tablicy A ktorego go zawieraja i zwracamy wynik


from math import inf
from queue import PriorityQueue

from zad3testy import runtests


def kintersect(A, k):
    n = len(A)
    points = []

    for i in range(n):
        points.append((A[i][0], 0, A[i][1]))
        points.append((A[i][1], 1, inf))

    points.sort(key=lambda X: (X[0], X[1], -1 * X[2]))
    Q = PriorityQueue()
    m, cnt = len(points), 0
    rStart, rEnd, lastStart = 0, 0, points[0][0]
    for i in range(m):
        if points[i][1] == 0:
            lastStart = points[i][0]
            Q.put(points[i][2])
            cnt += 1
        else:
            cnt -= 1
            if not Q.empty():
                Q.get()

        if cnt == k:
            end = Q.get()
            if end - lastStart > rEnd - rStart:
                rEnd = end
                rStart = lastStart
            Q.put(end)
        elif cnt > k:
            # Jesli otworzylismy wiecej niz k przedzialow to wyrzucamy te ktorych koniec jest najmniejszy i sprawdzamy
            # dla end najwikeszego mozliwego
            end = inf
            while not Q.empty() and cnt >= k:
                end = Q.get()
                cnt -= 1

            if end - lastStart > rEnd - rStart:
                rEnd = end
                rStart = lastStart

    result, cnt = [], 0
    for j in range(n):
        if A[j][0] <= rStart and rEnd <= A[j][1] and cnt < k:
            result.append(j)
            cnt += 1

    return result


runtests(kintersect)
