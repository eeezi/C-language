word = []

for _ in range(int(input())):
    word.append(input())

set_word = list(set(word))
sort_word = []

for i in set_word:
    sort_word.append((len(i), i))

sort_word.sort()

for lenth, word in sort_word:
    print(word)