def count_valid_rotations(start, end):
    valid_map = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
    def is_valid(n):
        num_str = str(n)
        return all(digit in valid_map for digit in num_str) and "".join(valid_map[d] for d in reversed(num_str)) == num_str
    return sum(is_valid(num) for num in range(start, end + 1))
start, end = int(input()), int(input())
print(count_valid_rotations(start, end))
