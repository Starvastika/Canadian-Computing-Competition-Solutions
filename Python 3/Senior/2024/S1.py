def count_same_hat_numbers(n, hat_numbers):
    count = 0
    for i in range(n):
        if hat_numbers[i] == hat_numbers[(i + n // 2) % n]:
            count += 1
    return count
n = int(input())
hat_numbers = []
for i in range(n):
    hat_numbers.append(int(input()))
result = count_same_hat_numbers(n, hat_numbers)
print(result)