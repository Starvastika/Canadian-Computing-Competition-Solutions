def process_arrays(array_length, array_A, array_B):
    unique_values, value_ranges, left_swipes, right_swipes = [array_B[0]], [], [], []
    left_index, right_index, current_value = 0, 0, array_B[0]
    for i in range(1, array_length):
        if array_B[i] == current_value:
            right_index += 1
        else:
            value_ranges.append((left_index, right_index))
            left_index, right_index, current_value = i, i, array_B[i]
            unique_values.append(current_value)
    value_ranges.append((left_index, right_index))
    current_unique_index = 0
    for i in range(array_length):
        if current_unique_index == len(unique_values):
            break
        if array_A[i] == unique_values[current_unique_index]:
            if value_ranges[current_unique_index][0] < i:
                left_swipes.append((value_ranges[current_unique_index][0], i))
            if value_ranges[current_unique_index][1] > i:
                right_swipes.append((i, value_ranges[current_unique_index][1]))
            current_unique_index += 1
    if current_unique_index == len(unique_values):
        print("YES")
        print(len(left_swipes) + len(right_swipes))
        for swipe in left_swipes:
            print("L", swipe[0], swipe[1])
        for swipe in reversed(right_swipes):
            print("R", swipe[0], swipe[1])
    else:
        print("NO")
array_length = int(input())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))
process_arrays(array_length, array_A, array_B)