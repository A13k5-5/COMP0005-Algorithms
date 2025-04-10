from digraph import Digraph
from digraph import sample_digraph


class DigraphDfs:
    def __init__(self, g: Digraph):
        self.marked = [False for _ in range(g.getV())]
        self.edgeTo = [-1 for _ in range(g.getV())]

    def _dfs(self, g: Digraph, v: int):
        if self.marked[v]:
            return
        self.marked[v] = True
        for w in g.getAdj(v):
            if self.marked[w]:
                continue
            self.edgeTo[w] = v
            self._dfs(g, w)


if __name__ == "__main__":
    d: Digraph = sample_digraph()
    print(d)
