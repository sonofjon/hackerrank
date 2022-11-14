n = int(input())

words = [input() for _ in range(n)]

for i in range(n):
    odds = words[i][1::2]
    evens = words[i][0::2]
    print(evens, odds)