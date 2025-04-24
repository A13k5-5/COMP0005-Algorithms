import heapq
from collections import defaultdict


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for source, target, value in times:
        graph[source].append((target, value))

    timeTo = {}

    pq = [(0, k)]

    while pq:
        time_to_k, node = heapq.heappop(pq)
        if node in timeTo:
            continue
        timeTo[node] = time_to_k

        for target_node, edge_weight in graph[node]:
            if target_node in timeTo:
                continue
            heapq.heappush(pq, (time_to_k + edge_weight, target_node))

    print(timeTo)

    if len(timeTo) == n:
        return max(timeTo.values())
    return -1


if __name__ == "__main__":
    print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
