def last_indexof_max(numbers):
    if not numbers:
        return -1

    last_max_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[last_max_index]:
            last_max_index = i

    return last_max_index
