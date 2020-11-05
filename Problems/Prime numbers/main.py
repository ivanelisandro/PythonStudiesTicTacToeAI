prime_numbers = []
for n in range(2, 1000):
    if not any(n != d and n % d == 0 for d in range(2, n - 1)):
        prime_numbers.append(n)
