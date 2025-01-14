# 1 - Union-find


def init(n):
    return [i for i in range(n)]


def find(u, v, network):
    return network[u] == network[v]


def union(u, v, network):
    old = network[u]
    new = network[v]
    for i, x in enumerate(network):
        if x == old:
            network[i] = new


if __name__ == "__main__":
    network = init(10)
    union(5, 0, network)
    union(6, 5, network)
    union(2, 1, network)
    union(7, 2, network)
    union(3, 8, network)
    union(4, 3, network)
    union(9, 4, network)
    union(6, 1, network)
    print(network)
