# 3. Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę
# jeśli z liter słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter)
# oraz fałsz w przeciwnym wypadku. Można założyć, że w i v składają się wyłącznie z małych liter
# alfabetu łacińskiego. Proszę krótko uzasadnić wybór zaimplementowanego algorytmu.

def possible(u, v, w):
    suma = len(w)
    A = [0] * 57
    for a in range(len(w)):
        A[ord(w[a]) - 65] += 1
    i, j = 0, 0
    while i < len(u) or j < len(v):
        if i < len(u):
            if A[ord(u[i]) - 65] != 0:
                A[ord(u[i]) - 65] -= 1
                suma -= 1
        if j < len(v):
            if A[ord(v[i]) - 65] != 0:
                A[ord(v[i]) - 65] -= 1
                suma -= 1
        if suma == 0:
            return True
        i += 1
        j += 1

    return False



# def possible(u, v, w):
#     i = 0
#     j = 0
#     witer = 0
#     while i < len(u) or j < len(v):
#
#         x = w[witer]
#
#         if witer == len(w) - 1:
#             return True
#
#         if i < len(u):
#             if x == u[i]:
#                 witer += 1
#                 i = 0
#             else:
#                 i += 1
#
#         elif j < len(v):
#             if v[j] == x:
#                 j = 0
#                 witer += 1
#             else:
#                 j += 1
#
#     return False


u = 'Abcd'
v = 'abcde'
w = 'abcdeabcd'
print(possible(u, v, w))
