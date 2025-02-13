height = int(input())
width = height * 2
bow_tie = [[' ' for _ in range(width)] for _ in range(height)]
for i in range(height):
    star_count = (i * 2 + 1) if i <= height // 2 else ((height - i - 1) * 2 + 1)
    for j in range(star_count):
        bow_tie[i][j] = '*'
        bow_tie[i][width - j - 1] = '*'
for row in bow_tie:
    print(''.join(row))