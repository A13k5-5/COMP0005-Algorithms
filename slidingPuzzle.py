from collections import deque


def getNeighbours(x, y, xs):
    top = down = left = right = None
    if y > 0:
        top = (x, y - 1)
    if y < len(xs) - 1:
        down = (x, y + 1)

    if x > 0:
        left = (x - 1, y)
    if x < len(xs[0]) - 1:
        right = (x + 1, y)

    return list(filter(lambda n: n is not None, [top, down, left, right]))


def convertPuzzToNum(puzz):
    acc = 0
    flat = [i for s in puzz for i in s][::-1]
    for i in range(len(flat)):
        acc += flat[i] * 10**i
    return acc


def printPuzz(puzz):
    for p in puzz:
        print(p)
    print()


def tupleToPuzz(tuple, dimension):
    newPuzz = [[]]
    for i, t in enumerate(tuple):
        newPuzz[-1].append(t)
        if len(newPuzz[-1]) == dimension and i != len(tuple) - 1:
            newPuzz.append([])
    return newPuzz


def bfs(puzz, x, y):
    n = len(puzz)
    start_state = tuple(i for row in puzz for i in row)
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    q = deque()
    q.append((start_state, x, y, []))

    visited = set()
    visited.add(start_state)

    while q:
        cur_state, x, y, path = q.popleft()
        if cur_state == goal_state:
            for step in path:
                printPuzz(step)
            return path

        for nx, ny in getNeighbours(x, y, puzz):
            new_state = list(cur_state)
            new_pos = ny * n + nx
            new_state[new_pos], new_state[y * n + x] = 0, new_state[new_pos]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                new_puzz = tupleToPuzz(new_state, 3)
                q.append((new_state, nx, ny, path + [new_puzz]))


if __name__ == "__main__":
    puzzle = [[1, 6, 7], [2, 8, 3], [5, 4, 0]]
    print(tupleToPuzz((1, 2, 3, 4, 5, 6, 7, 8, 0), 3))
    bfs(puzzle, 2, 2)
