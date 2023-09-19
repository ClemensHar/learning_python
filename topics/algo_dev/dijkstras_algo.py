import numpy as np

INF = float("infinity")


def dijkstras(graph):
    min_distances = {}
    for key in graph.keys():
        min_distances[key] = INF

    visited = []
    unvisited = list(graph.keys())
    current_vert = unvisited[0]
    min_distances[current_vert] = 0
    while len(visited) < len(graph):
        visited.append(current_vert)
        print(f"visited: {visited}")
        distance2current_vert = min_distances[current_vert]
        for key, value in graph[current_vert].items():
            if (
                distance2current_vert + value < min_distances[key]
                and key not in visited
            ):
                min_distances[key] = distance2current_vert + value
        distance2beat = INF
        for key, value in min_distances.items():
            if key not in visited and value < distance2beat:
                distance2beat = value
                current_vert = key
                print(f"current vert at end: {current_vert}")
        print(f"min distances: {min_distances}")

    return min_distances


graph = {
    "A": {"B": 6, "D": 1},
    "B": {"A": 6, "C": 5, "D": 2, "E": 2},
    "C": {"B": 5, "E": 5},
    "D": {"A": 1, "B": 2, "E": 1},
    "E": {"B": 2, "C": 5, "D": 1},
}
dijkstras(graph=graph)
