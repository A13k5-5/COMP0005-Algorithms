from digraph import Digraph, sample_digraph


class DirectedCycle:
    def __init__(self, g: Digraph):
        self.onStack = [False for _ in range(g.getV())]
        self.marked = [False for _ in range(g.getV())]
        self.hasCycle = False
        for s in range(g.getV()):
            if not self.marked[s]:
                self._dfs(g, s)

    def _dfs(self, g: Digraph, v: int):
        self.marked[v] = True
        self.onStack[v] = True
        for w in g.getAdj(v):
            if self.hasCycle:
                return
            elif not self.marked[w]:
                self._dfs(g, w)
            elif self.onStack[w]:
                self.hasCycle = True
        self.onStack[v] = False


if __name__ == "__main__":
    g: Digraph = sample_digraph()
    d: DirectedCycle = DirectedCycle(g)
    print(d.hasCycle)
