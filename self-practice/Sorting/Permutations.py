def permutations1(a, b):
    a.sort()
    b.sort()
    return a == b


if __name__ == "__main__":
    print(permutations1([1, 2, 3, 4], [4, 0, 2, 1]))
