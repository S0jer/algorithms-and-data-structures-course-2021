# Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
# chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
# ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
# int goodThief( int A[], int n );
# która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
# kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
# poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
# jak najszybszy (ale przede wszystkim poprawny).


def goodThief(A):
    n = len(A)
    dp = [0 for _ in range(n)]
    road = []

    dp[0] = A[0]
    dp[1] = A[1]

    for i in range(2, n):
        dp[i] = max(A[i] + dp[j] for j in range(i - 1))

    result = max(dp)
    check = result

    for i in range(n - 1, -1, -1):
        if dp[i] == check:
            road.append(i)
            check -= A[i]
    road = road[::-1]

    return road, result


A = [2, 4, 8, 7, 10, 20, 1, 5, 10, 4]
road, result = goodThief(A)

print(road)
print(result)

