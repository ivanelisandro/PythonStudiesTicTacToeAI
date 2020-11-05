def fib(n):

    if n == 0:  # base case for month 0
        return 0
    elif n == 1:  # base case for month 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
