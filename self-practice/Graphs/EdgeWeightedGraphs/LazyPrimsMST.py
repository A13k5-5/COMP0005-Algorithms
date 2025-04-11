from EdgeWeightedGraph import EdgeWeightedGraph, loadEWG
from Edge import Edge
import heapq


class LazyPrimsMST:
    def __init__(self, g: EdgeWeightedGraph):
        self.marked: list[bool] = [False for _ in range(g.getV())]
        self.mst = []
        self.weight: int = 0
        self.pq: list[Edge] = []
        self.visit(g, 0)
        while len(self.pq) > 0:
            e: Edge = heapq.heappop(self.pq)
            v = e.either()
            w = e.other(v)
            # The laziness
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.append(e)
            if not self.marked[v]:
                self.visit(g, v)
            if not self.marked[w]:
                self.visit(g, w)

    def getEdges(self):
        return self.mst

    def getWeight(self):
        self.weight = 0
        for e in self.mst:
            self.weight += e.weight
        return self.weight

    def visit(self, g: EdgeWeightedGraph, v: int):
        self.marked[v] = True
        for e in g.getAdj(v):
            # If the edge is a crossing edge of a cut
            if not self.marked[e.other(v)]:
                # pq uses __lt__ and __eq__ to compare edges
                heapq.heappush(self.pq, e)


if __name__ == "__main__":
    g: EdgeWeightedGraph = loadEWG("tinyEWG.txt")
    lazyPrimMST: LazyPrimsMST = LazyPrimsMST(g)
    print(lazyPrimMST.getEdges())
