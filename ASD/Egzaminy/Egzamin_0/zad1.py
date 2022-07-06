from zad1testy import runtests


def tanagram(x, y, t):
    n, minus = 26, 97

    word_x = [[] for _ in range(n)]
    word_y = [[] for _ in range(n)]

    for i in range(len(x)):
        word_x[ord(x[i]) - minus].append(i)
        word_y[ord(y[i]) - minus].append(i)

    for j in range(n):
        if len(word_x[j]) == len(word_y[j]):
            for z in range(len(word_x[j])):
                if abs(word_x[j][z] - word_y[j][z]) > t:
                    return False
        else:
            return False

    return True


runtests(tanagram)
