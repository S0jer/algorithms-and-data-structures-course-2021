# Paweł Jaśkowiec, 406165

# Program przyjmuje do funkcji 'printAllLIS' tablice 'A' i następnie wyszukuje i spisuje za pomocą rekurencji
# najdłuższe ciągi liczbowe z tablicy 'A' do tablicy 'R' oraz następnie wypisuje kolejno ciągi z tablicy 'R'
# oraz zwraca ich ilość


# Funkcja 'printAllLIS' znajduje długości ciągów malejących przechodząc po tablicy A od końca i zapisuje je w tablicy 'F'
# oraz odwołania do indeksów dla każdego możliwego ciągu i zapisuje je w tablicy 'P'



def printAllLIS(A):
    n = len(A)
    P = [[-1] + [] * n for _ in range(n)]
    F = [1] * n
    R = [[] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if A[j] > A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if F[j] + 1 == F[i] and A[j] > A[i]:
                if P[i] == [-1]:
                    P[i] = [j]
                else:
                    P[i].append(j)

    # 'P' zawiera odwołania do indeksów kolejnych ciągów
    # 'F' zawiera długości ciągów
    maks = max(F)
    for x in range(len(F)):
        if F[x] == maks:  # Funkcję rekurencyjna wywołuję dla indeksów najdłuższych ciągów i po nich je sortuję
            R = get_solution(A, P, x, [], R, maks, x)

    count = print_solution(R)

    return count


# Funkcja 'get_solution' rekurencyjnie znajduje wszystkie możliwe kombinacje ciągów maksymalnych
# idąc po różnych rozgałęzieniach z tablicy 'P' oraz gdy znaleziony ciąg jest długości 'maks' dodaje go
# do tablicy R pod indeks 'idx'


def get_solution(A, P, i, result, R, maks, idx):
    if P[i][0] != -1:
        if len(P[i]) > 1:
            for a in range(
                    len(P[i])):  # wywołujemy rekurencję dla każdego indeksu z tablicy 'P' po którym idą nasze ciągi
                get_solution(A, P, P[i][a], result + [A[i]], R, maks, idx)
        else:  # jeśli w tablicy P jest tylko jedna droga wybieramy ją
            get_solution(A, P, P[i][0], result + [A[i]], R, maks, idx)

    result.append(A[i])
    if len(result) == maks:
        R[idx].append(result)

    return R


# Funkcja wypisuje kolejne najdłuższe ciągi rosnące zawarte w tablicy 'R'


def print_solution(R):
    count = 0
    for i in range(len(R)):
        for j in range(len(R[i])):
            print(*R[i][j], sep=' ')
            count += 1
    return count


# A = [2, 1, 4, 3]
# B = [10 * k + i for k in range(8) for i in range(6, 0, -1)]
# C = [13, 7, 21, 42, 8, 2, 44, 53, 47]
D = [3, 2, 1, 13, 12, 11, 23, 22, 21]

count = printAllLIS(D)
print(count)
