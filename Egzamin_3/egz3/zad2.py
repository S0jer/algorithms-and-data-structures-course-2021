from zad2testy import runtests


def double_prefix(L):
    n, m = len(L), 0
    for j in range(n):
        if len(L[j]) > m:
            m = len(L[j])

    zero = [0 for _ in range(m + 1)]
    ones = [0 for _ in range(m + 1)]
    for a in range(n):
        b = 0
        for znak in L[a]:
            if znak == '1':
                ones[b] += 1
            if znak == '0':
                zero[b] += 1

            b += 1
    print(zero)
    print(ones)

    return []


runtests(double_prefix)
