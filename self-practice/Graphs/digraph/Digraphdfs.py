from Digraph import Digraph
from Digraph import sample_digraph


class DigraphDfs:
    def __init__(self, g: Digraph, s: int):
        self.marked = [False for _ in range(g.getV())]
        self.edgeTo = [-1 for _ in range(g.getV())]
        self._dfs(g, s)
        self.s = s

    def _dfs(self, g: Digraph, v: int):
        self.marked[v] = True
        for w in g.getAdj(v):
            if self.marked[w]:
                continue
            self.edgeTo[w] = v
            self._dfs(g, w)

    def pathTo(self, v: int):
        path = []
        if not self.marked[v]:
            return path
        path.append(v)
        x: int = self.edgeTo[v]
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.s)
        return path


if __name__ == "__main__":
    d: Digraph = sample_digraph()
    print(d)
    dfs: DigraphDfs = DigraphDfs(d, 0)
    print(dfs.marked)
    print(dfs.pathTo(3))
