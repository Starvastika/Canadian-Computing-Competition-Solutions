def generate_fractal(levels, width, check_x):
    fractal_segments = {(0, width, 1, 1, 1)}
    for i in range(levels):
        new_segments = set()
        for start_x, end_x, start_y, end_y, direction in fractal_segments:
            segment_width = abs(start_x - end_x) // 3 if start_y == end_y else abs(start_y - end_y) // 3
            if start_y == end_y:
                new_segments.add((start_x, start_x + segment_width, start_y, end_y, direction))
                new_segments.add((end_x - segment_width, end_x, start_y, end_y, direction))
                new_segments.add((
                    start_x + segment_width, end_x - segment_width,
                    start_y + direction * segment_width, start_y + direction * segment_width, direction))
                new_segments.add((
                    start_x + segment_width, start_x + segment_width,
                    min(start_y + direction * segment_width, end_y),
                    max(start_y + direction * segment_width, end_y), -1))
                new_segments.add((
                    end_x - segment_width, end_x - segment_width,
                    min(start_y + direction * segment_width, end_y),
                    max(start_y + direction * segment_width, end_y), 1))
            else:
                new_segments.add((start_x, end_x, start_y, start_y + segment_width, direction))
                new_segments.add((start_x, end_x, end_y - segment_width, end_y, direction))
                new_segments.add((
                    start_x + direction * segment_width, start_x + direction * segment_width,
                    start_y + segment_width, end_y - segment_width, direction))
                new_segments.add((
                    min(start_x + direction * segment_width, end_x), max(start_x + direction * segment_width, end_x),
                    start_y + segment_width, start_y + segment_width, -1))
                new_segments.add((
                    min(start_x + direction * segment_width, end_x), max(start_x + direction * segment_width, end_x),
                    end_y - segment_width, end_y - segment_width, 1))
        fractal_segments = new_segments
    result_y_values = []
    for start_x, end_x, start_y, end_y, _ in fractal_segments:
        if start_x <= check_x <= end_x:
            result_y_values.append((start_y, end_y))
    result_y_values = {y for start, end in result_y_values for y in range(start, end + 1)}
    print(*sorted(result_y_values))
levels, width, check_x = map(int, input().split())
generate_fractal(levels, width, check_x)
