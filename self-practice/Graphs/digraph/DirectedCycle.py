from digraph import Digraph, sample_digraph


class DirectedCycle:
    def __init__(self, g: Digraph):
        self.onStack = [False for _ in range(g.getV())]
        self.marked = [False for _ in range(g.getV())]
        self.edgeTo = [-1 for _ in range(g.getV())]
        self.cycle = None
        for s in range(g.getV()):
            if not self.marked[s]:
                self._dfs(g, s)

    def _dfs(self, g: Digraph, v: int):
        self.marked[v] = True
        self.onStack[v] = True
        for w in g.getAdj(v):
            if self.hasCycle():
                return
            elif not self.marked[w]:
                self.edgeTo[w] = v
                self._dfs(g, w)
            elif self.onStack[w]:
                self.cycle = []
                x: int = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
                self.cycle.append(v)
                self.cycle = self.cycle[::-1]

        self.onStack[v] = False

    def hasCycle(self):
        return self.cycle is not None


if __name__ == "__main__":
    g: Digraph = sample_digraph()
    d: DirectedCycle = DirectedCycle(g)
    print(d.cycle)
