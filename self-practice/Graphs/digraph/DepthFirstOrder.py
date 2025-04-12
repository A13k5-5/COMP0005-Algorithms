from Digraph import Digraph


class DepthFirstOrder:
    def __init__(self, g: Digraph):
        self.marked = [False for _ in range(g.getV())]
        self.post = []
        for s in range(g.getV()):
            if self.marked[s]:
                continue
            self._dfs(g, s)

    def _dfs(self, g: Digraph, v: int):
        self.marked[v] = True
        for w in g.getAdj(v):
            if self.marked[w]:
                continue
            self._dfs(g, w)
        self.post.append(v)

    def getReversePost(self):
        return self.post[::-1]

    def getPost(self):
        return self.post


if __name__ == "__main__":
    g: Digraph = Digraph(5)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(0, 2)
    g.addEdge(3, 4)
    dfs: DepthFirstOrder = DepthFirstOrder(g)
    print(dfs.getReversePost())
