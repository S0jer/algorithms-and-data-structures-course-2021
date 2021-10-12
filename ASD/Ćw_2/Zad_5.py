# Zadanie 5. (Lider ciągu) Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
# O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.


def lider(T):
    counter, n = 1, len(T)
    lider = T[0]
    for i in range(1, n):
        if counter == 0:
            lider = T[i]
            counter = 1
        elif T[i] == lider:
            counter += 1
        else:
            counter -= 1
    counter = 0
    for j in range(n):
        if T[j] == lider:
            counter += 1
    if counter > n // 2:
        return True
    return False


if __name__ == '__main__':
    T = [5, 2, 5, 2, 5, 5, 3]
    print(lider(T))
