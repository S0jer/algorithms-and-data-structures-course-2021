# 3. Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
# ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
# mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
# ciąg składa się wyłącznie z liter a i b.
# Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
# powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
# algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.




# Idziemy po tablicy i dzielimy ją na kolejne k podciągi,
# [a b a b a b b b a] -> [a b a] [b a b] [a b a] [b a b] [a b b] [b b b]
# sortujemy radixem i zliczamy najdłuższy podciąg posortowanej listy podciągów o długości k




