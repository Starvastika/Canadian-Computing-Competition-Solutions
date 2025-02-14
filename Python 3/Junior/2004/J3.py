n, m = int(input()), int(input())
adjectives = [input() for x in range(n)]
nouns = [input() for y in range(m)]
for a in range(n):
    for b in range(m):
        print(f"{adjectives[a]} as {nouns[b]}")