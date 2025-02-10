from PancakeSorting import flipTuple, sortTuple

from collections import deque
import random


def advancedFlip(a, start, end):
    if start >= end:
        return
    m, n = start, end
    while m < n:
        a[m], a[n] = a[n], a[m]
        m += 1
        n -= 1


def advancedFlipTuple(a, start, end):
    l = list(a)
    advancedFlip(l, start, end)
    return tuple(l)


def advancedPancakeSort(a):
    q = deque()
    visited = set()
    startState = tuple(a)
    goalState = sortTuple(startState)
    visited.add(startState)
    q.append((startState, []))
    while q:
        curState, curFlips = q.popleft()
        for i in range(len(curState)):
            for j in range(0, i):
                newState = advancedFlipTuple(curState, j, i)
                newPath = curFlips + [(j, i)]
                if newState == goalState:
                    return list(newState), newPath
                if newState in visited:
                    continue
                visited.add(newState)
                q.append((newState, newPath))


if __name__ == "__main__":
    a = [1, 3, 2, 67, 8, 23, 5, 234]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # a = [3, 2, 4, 1]
    a = [i for i in range(10)]
    random.shuffle(a)
    # a = [1, 8, 9, 3, 2, 7, 6, 5, 4, 10]
    print(advancedPancakeSort(a))
