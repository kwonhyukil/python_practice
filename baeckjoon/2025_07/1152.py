word = list(map(str, input()))

count = 0

if word and word[0] != ' ':
    count = 1

for i in range(1, len(word)):
    if word[i - 1] == ' ' and word[i] != ' ':
        count += 1

print(count)
