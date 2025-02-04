# [1,3,2,67,8,23,5,234]
# [234,5,23,8,67,2,3,1]
# [8,23,5,234,67,2,3,1]
# [67,234,5,23,8,2,3,1]
# [5,234,67,23,8,2,3,1]
# [23,67,234,5,8,2,3,1]
# [5,234,67,23,8,2,3,1]
# [8,23,67,234,5,2,3,1]
def flip2(a, i):
    print(a[:i][::-1] + a[i:])


def flip(a, i):
    m, n = 0, i
    while m < n:
        a[m], a[n] = a[n], a[m]
        m += 1
        n -= 1


def findMaxIndex(a, lo):
    maxIndex = lo
    for i in range(lo, len(a)):
        if a[i] > a[maxIndex]:
            maxIndex = i
    return maxIndex


def pancakeSort(a):
    sorted = 0
    while sorted < len(a):
        maxIndex = findMaxIndex(a, sorted)
        flip(a, maxIndex - 1)
        flip(a, maxIndex)
        sorted += 1
        print(a)


if __name__ == "__main__":
    a = [1, 3, 2, 67, 8, 23, 5, 234]
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = [3, 2, 4, 1]
    # print(findMaxIndex(a, 0))
    pancakeSort(a)
