import heapq

from DirectedEdge import DirectedEdge
from EdgeWeightedDigraph import EdgeWeightedDigraph, loadEWD


class DijkstraSP:
    def __init__(self, g: EdgeWeightedDigraph, s: int):
        self.distTo: list[float] = [float("inf") for _ in range(g.getV())]
        self.distTo[s] = 0.0
        self.edgeTo = [None for _ in range(g.getV())]
        self.pq = []
        heapq.heappush(self.pq, (self.distTo[s], s))

        while len(self.pq) > 0:
            dist, v = heapq.heappop(self.pq)
            if dist > self.distTo[v]:
                continue
            for e in g.getAdj(v):
                self.relax(e)

    def relax(self, e: DirectedEdge):
        v: int = e.getSource()
        w: int = e.getDestination()
        if self.distTo[w] > self.distTo[v] + e.getWeight():
            self.distTo[w] = self.distTo[v] + e.getWeight()
            self.edgeTo[w] = e
            heapq.heappush(self.pq, (self.distTo[w], w))

    def hasPathTo(self, v: int):
        return self.distTo[v] < float("inf")

    def getDistTo(self, v: int):
        return self.distTo[v]

    def pathTo(self, v: int):
        if not self.hasPathTo(v):
            return None
        path = []
        e = self.edgeTo[v]
        while e is not None:
            path.append(e)
            e = self.edgeTo[e.getSource()]
        path.reverse()
        return path


if __name__ == "__main__":
    # g: EdgeWeightedDigraph = loadEWD("tinyEWD.txt")
    g: EdgeWeightedDigraph = EdgeWeightedDigraph(4)
    g.addEdge(0, 1, 8)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 2, 10)
    g.addEdge(2, 3, - 17)
    s = 0
    sp = DijkstraSP(g, s)
    for v in range(g.getV()):
        print(f"Distance to {v}: {sp.getDistTo(v)}")
        if sp.hasPathTo(v):
            print(f"Path: {sp.pathTo(v)}")
        print()
