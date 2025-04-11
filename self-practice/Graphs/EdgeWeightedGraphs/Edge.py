class Edge:
    def __init__(self, v: int, w: int, weight: float):
        self.v: int = v
        self.w: int = w
        self.weight = weight

    def either(self) -> int:
        return self.v

    def other(self, vertex: int) -> int:
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        raise Exception("Illegal argument")

    def __lt__(self, other) -> bool:
        return self.weight < other.weight

    def __eq__(self, other) -> bool:
        return self.weight == other.weight

    def __repr__(self):
        return f"{self.v, self.w, self.weight}"


if __name__ == "__main__":
    e1: Edge = Edge(1, 2, 7)
    e2: Edge = Edge(1, 2, 7)
    print(e1 == e2)
