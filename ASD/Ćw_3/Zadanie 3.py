# Zadanie 3. Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad
# alfabetem długości k, sprawdza czy A i B są swoimi anagramami.
# 1. Proszę zaproponować rozwiązanie działające w czasie O(n + k).
# 2. Proszę zaproponować rozwiązanie działające w czasie O(n) (proszę zwrócić uwagę, że k może być dużo
# większe od n—np. dla alfabetu unicode; złożoność pamięciowa może być rzędu O(n + k)).
# Proszę zaimplementować oba algorytmy.


def check_anagrams(word1, word2):
    K = [0] * 94
    if len(word1) != len(word2):
        return False
    i, j = 0, 0
    while i < len(word1):
        x = ord(word1[i]) - 32
        y = ord(word2[i]) - 32
        K[x] -= 1
        K[y] += 1
        i += 1
    for i in range(len(K)):
        if K[i] != 0:
            return False
    return True


# word1 = 'abcde*/^'
# word2 = '*/^dceba'
word1 = 'absd*/^f4c9dd*de0gf'
word2 = 'fegf/ds^dc09b*add*4'
print(check_anagrams(word1, word2))
