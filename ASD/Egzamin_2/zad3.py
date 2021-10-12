# Paweł Jaśkowiec

# Pomysł na rozwiazanie zadania polega na przejsciu po tablicy zawierającej 'wciśnięcia' guzików o raz na bieżąco
# zliczaniem ilości światełek świecących się na niebiesko po każdej operacji naciśnięć, na koniec program zwraca maksymalną
# zarejestrowaną ilość świecących się lampek w danej chwili

# Złozonosc pamieciowa to n

# Złozonosc programu: T  - jesli T rozumiemy przez łączną ilośc wciśnięć guzików z każdej m operacji


from zad3testy import runtests


def lamps(n, T):
    t, cnt, n_max = len(T), 0, 0

    colors = [0 for _ in range(n)]

    for i in range(t):  # rozwazamy operacje wcisniec po kolei i po kazdej
        for j in range(T[i][0], T[i][1] + 1):  # operacji sprawdzamy ilosc lampek swiecacych na niebiesko
            if colors[j] == 2:
                cnt -= 1
            colors[j] = (colors[j] + 1) % 3

            if colors[j] == 2:
                cnt += 1

        if cnt > n_max:
            n_max = cnt

    return n_max


runtests(lamps)
