class MinPQ:
    def __init__(self):
        self.pq = [None]
        self.n = 0

    def isEmpty(self):
        return self.n == 0

    def insert(self, v):
        self.pq.append(v)
        self.n += 1
        self.swim(self.n)

    def delMin(self):
        if self.n < 1:
            raise Exception("Empty heap")
        min = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        return min

    def sink(self, k: int):
        while 2 * k <= self.n:
            # Left child
            c = 2 * k
            if c < self.n and self.isMore(c, c + 1):
                c += 1
            if not self.isMore(c, k):
                self.exch(c, k)
            k = c

    def swim(self, k: int):
        while k > 1 and self.isMore(k // 2, k):
            self.exch(k // 2, k)
            k = k // 2

    def exch(self, i: int, j: int):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def isMore(self, i: int, j: int):
        return self.pq[i] > self.pq[j]


import random

if __name__ == "__main__":
    pq: MinPQ = MinPQ()
    for _ in range(10):
        pq.insert(random.randint(0, 100))
    print(pq.pq)
    for _ in range(pq.n):
        print(pq.delMin())
