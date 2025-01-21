from math import factorial


def uniquePaths(m, n):
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


if __name__ == "__main__":
    print(uniquePaths(2, 2))
