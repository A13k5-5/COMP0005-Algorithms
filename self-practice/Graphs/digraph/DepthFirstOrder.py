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
