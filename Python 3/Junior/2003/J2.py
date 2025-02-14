import math
area = int(input())
while area != 0:
    min_perimeter = float('inf')
    best_dimensions = [0, 0]

    for l in range(1, int(math.sqrt(area)) + 1):
        if area % l == 0:
            w = area // l
            perimeter = 2 * (l + w)
            if perimeter < min_perimeter:
                min_perimeter = perimeter
                best_dimensions = [l, w]
    dimensions = " x ".join(map(str, best_dimensions))
    print(f"Minimum perimeter is {min_perimeter} with dimensions {dimensions}")
    area = int(input())