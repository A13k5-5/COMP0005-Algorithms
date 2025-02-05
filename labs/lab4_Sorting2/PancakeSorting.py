from collections import deque


def flip(a, i, flips):
    if i <= 0:
        return
    flips = flips.append(i)
    m, n = 0, i
    while m < n:
        a[m], a[n] = a[n], a[m]
        m += 1
        n -= 1
    # print(a)


def flipTuple(a, i):
    flips = list(a)
    flip(flips, i, [])
    return tuple(flips)


def findMaxIndex(a, hi):
    maxIndex = 0
    for i in range(hi, -1, -1):
        if a[i] > a[maxIndex]:
            maxIndex = i
    return maxIndex


def pancakeSort(a):
    flips = []
    sorted = 0
    while sorted < len(a):
        maxIndex = findMaxIndex(a, len(a) - 1 - sorted)
        while maxIndex == len(a) - 1 - sorted and sorted != len(a) - 1:
            sorted += 1
            maxIndex = findMaxIndex(a, len(a) - 1 - sorted)
        flip(a, maxIndex, flips)
        flip(a, len(a) - 1 - sorted, flips)
        sorted += 1
    return flips


def sortTuple(a):
    srt = list(a)
    srt.sort()
    return tuple(srt)


def pancakeSort2(a):
    q = deque()
    visited = set()
    startState = tuple(a)
    goalState = sortTuple(startState)
    visited.add(startState)
    q.append((startState, []))
    while q:
        currentState, currentFlips = q.popleft()
        for i in range(len(a)):
            newState = flipTuple(currentState, i)
            if newState == goalState:
                return list(newState), currentFlips + [i]
            if newState in visited:
                continue
            visited.add(newState)
            q.append((newState, currentFlips + [i]))


if __name__ == "__main__":
    a = [1, 3, 2, 67, 8, 23, 5, 234]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # a = [3, 2, 4, 1]
    # print(len(pancakeSort(a)))
    print(pancakeSort2(a))
