from EdgeWeightedDigraph import EdgeWeightedDigraph, loadEWD
from DirectedEdge import DirectedEdge


class BellmanFordSP:
    def __init__(self, g: EdgeWeightedDigraph, s: int):
        self.edgeTo = [None for _ in range(g.getV())]
        self.distTo = [float("inf") for _ in range(g.getV())]
        self.distTo[s] = 0
        for _ in range(g.getV() - 1):
            for v in range(g.getV()):
                for e in g.getAdj(v):
                    self.relax(e)

    def relax(self, e: DirectedEdge):
        s: int = e.getSource()
        d: int = e.getDestination()
        new_distance: float = self.distTo[s] + e.getWeight()
        if self.distTo[d] > new_distance:
            self.distTo[d] = new_distance
            self.edgeTo[d] = e

    def hasPathTo(self, v: int):
        return self.distTo[v] < float("inf")

    def pathTo(self, v: int):
        if not self.hasPathTo(v):
            return None
        path = []
        e: DirectedEdge = self.edgeTo[v]
        path.append(v)
        while e is not None:
            path.append(e.getSource())
            e = self.edgeTo[e.getSource()]
        path.reverse()
        return path

    def getDistTo(self, v: int):
        return self.distTo[v]


if __name__ == "__main__":
    g: EdgeWeightedDigraph = loadEWD("NegativeEWG.txt")
    s = 0
    sp = BellmanFordSP(g, s)
    for v in range(g.getV()):
        print(f"Distance to {v}: {sp.getDistTo(v)}")
        if sp.hasPathTo(v):
            print(f"Path: {sp.pathTo(v)}")
        print()
