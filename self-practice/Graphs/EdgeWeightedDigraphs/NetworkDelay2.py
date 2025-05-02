import heapq


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = [[] for _ in range(n + 1)]
    for source, target, weight in times:
        graph[source].append((target, weight))

    distTo = {}
    # distTo = [float("inf") for _ in range(n + 1)]
    pq = [(0, k)]
    while pq:
        time_node_to_k, node = heapq.heappop(pq)

        if node in distTo:
            continue

        distTo[node] = time_node_to_k

        for neighbour, weight in graph[node]:
            heapq.heappush(pq, (time_node_to_k + weight, neighbour))
    if len(distTo) == n:
        return max(distTo.values())
    return -1


if __name__ == "__main__":
    networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
