from random import randint


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def sort(T):
    p = len(T)
    T_p = [[] for _ in range(p)]
    for i in range(len(T)):
        b = T[i] % p
        T_p[b].append(T[i])
    indeks = 0
    for j in T_p:
        for z in j:
            T[indeks] = z
            indeks += 1
    T_p = [[] for _ in range(p)]
    for i in range(len(T)):
        a = T[i] // p
        T_p[a].append(T[i])
    indeks = 0
    for j in T_p:
        for z in j:
            T[indeks] = z
            indeks += 1
    return T


# def search_and_count(T, U):
#     if len(T) != 1:
#         half = len(T) // 2
#         search_and_count(T[half:], U)
#         search_and_count(T[:half], U)
#     else:
#         for i in range(len(U) - 1):
#             if T[0] == U[i][0]:
#                 U[i][1] += 1
#                 break
#             elif U[i][0] < T[0] and T[0] < U[i+1][0]:
#                 for j in range(len(U), i + 1, -1):
#                     U[j][0] = U[j - 1][0]
#                     U[j][1] = U[j - 1][1]
#                 U[i][0] = T[0]
#                 U[i][1] = 1
#                 break
#             elif T[0] < U[i+1][0]:
#                 for j in range(len(U), i + 1, -1):
#                     U[j][0] = U[j - 1][0]
#                     U[j][1] = U[j - 1][1]
#                 U[i][0] = T[0]
#                 U[i][1] = 1
#                 break
#     return U

def search_uni(T, U):
    if len(T) != 1:
        half = len(T) // 2
        search_uni(T[half:], U)
        search_uni(T[:half], U)
    elif T[0] not in U:
        U.append(T[0])
    return U


def count_uni(T, U, I):
    if len(T) != 1:
        half = len(T) // 2
        count_uni(T[half:], U, I)
        count_uni(T[:half], U, I)
    else:
        for i in range(len(U)):
            if T[0] == U[i]:
                I[i] += 1
                break
    return I


def sort_2(T):
    indeks = 0
    U = search_uni(T, [])  # [3, 5, 6, 7]
    U = insertion_sort(U)
    I_U = [0 for _ in range(len(U))]  # [0, 0, 0, 0]
    I_U = count_uni(T, U, I_U)
    for i in range(len(U)):
        while I_U[i] != 0:
            T[indeks] = U[i]  # n*log(logn)
            indeks += 1
            I_U[i] -= 1
    return T


if __name__ == '__main__':
    T = [randint(1, 4) for i in range(10)]
    # T = sort(T)
    print(T)
    T = sort(T)
    print(T)
