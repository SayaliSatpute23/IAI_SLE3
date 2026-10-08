from collections import deque
from time import perf_counter

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["H"],
    "F": ["I"],
    "G": ["J"],
    "H": ["J"],
    "I": ["J"],
    "J": [],
}

START = "A"
GOAL = "J"


def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    expanded = []

    while queue:
        node = queue.popleft()
        expanded.append(node)

        if node == goal:
            return expanded

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return expanded


def dfs(graph, start, goal):
    stack = [start]
    visited = {start}
    expanded = []

    while stack:
        node = stack.pop()
        expanded.append(node)

        if node == goal:
            return expanded

        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return expanded


def average_time(search_function, runs=1000):
    total = 0.0
    for _ in range(runs):
        begin = perf_counter()
        search_function(GRAPH, START, GOAL)
        total += perf_counter() - begin
    return total / runs


def main():
    bfs_result = bfs(GRAPH, START, GOAL)
    dfs_result = dfs(GRAPH, START, GOAL)

    print("BFS expanded:", bfs_result)
    print("BFS node count:", len(bfs_result))
    print("BFS average time:", average_time(bfs))

    print("DFS expanded:", dfs_result)
    print("DFS node count:", len(dfs_result))
    print("DFS average time:", average_time(dfs))


if __name__ == "__main__":
    main()
