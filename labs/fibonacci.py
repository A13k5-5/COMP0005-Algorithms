# Space complexity O(n)
def fib_recur(n):
    if n == 1 or n == 2:
        return [0, 1][n - 1]
    return fib_recur(n - 1) + fib_recur(n - 2)


# Space complexity O(1)
def fib_iter(n):
    second_last = 0
    last = 1
    counter = 2
    while counter < n:
        counter += 1
        second_last, last = last, second_last + last
    return last


if __name__ == "__main__":
    print(fib_recur(10))
    print(fib_iter(10))
