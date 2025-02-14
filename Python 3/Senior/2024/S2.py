from collections import Counter
def check_alternating_pattern(s, N):
    freq = Counter(s)
    def is_light(c):
        return freq[c] == 1
    for i in range(1, N):
        if is_light(s[i]) == is_light(s[i - 1]):
            return False
    return True
T, N = map(int, input().split())
for _ in range(T):
    s = input().strip()
    if check_alternating_pattern(s, N):
        print("T")
    else:
        print("F")