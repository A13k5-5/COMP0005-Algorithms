class MinPQ:
    def __init__(self):
        self.pq = [None]
        self.n = 0

    def isEmpty(self):
        return self.n == 0

    def insert(self, v):
        pass

    def sink(self, k: int):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.isMore(j, j + 1):
                j += 1
            if not self.isMore(j, k):
                self.exch(j, k)
            k = j

    def swim(self, k: int):
        pass

    def exch(self, i: int, j: int):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def isMore(self, i: int, j: int):
        return self.pq[i] > self.pq[j]
