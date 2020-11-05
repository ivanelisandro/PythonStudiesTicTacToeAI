values = [int(n) for n in input()]

average = [(values[index] + values[index + 1]) / 2
           for index
           in range(len(values) - 1)]

print(average)
