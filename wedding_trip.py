from collections import deque
from itertools import permutations


def bfs(graph, start):
    distance = [-1] * len(graph)
    parent = [-1] * len(graph)
    distance[start] = 0
    queue = deque([start])

    while queue:
        city = queue.popleft()

        for neighbor in graph[city]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[city] + 1
                parent[neighbor] = city
                queue.append(neighbor)

    return distance, parent


def wedding_trip(c, flights, home, cities):
    graph = [[] for _ in range(c + 1)]

    for a, b in flights:
        graph[a].append(b)

    distances = {}
    parents = {}

    for start in [home] + cities:
        distances[start], parents[start] = bfs(graph, start)

    best_count = float("inf")
    best_order = None

    for order in permutations(cities):
        stops = [home] + list(order) + [home]
        count = 0

        for i in range(4):
            part = distances[stops[i]][stops[i + 1]]

            if part == -1:
                count = float("inf")
                break

            count += part

        if count < best_count:
            best_count = count
            best_order = stops

    if best_order is None:
        return -1, []

    route = [home]

    for i in range(4):
        start = best_order[i]
        city = best_order[i + 1]
        path = []

        while city != start:
            path.append(city)
            city = parents[start][city]

        route.extend(reversed(path))

    return best_count, route


if __name__ == "__main__":
    c, f = map(int, input().split())
    home, a, b, d = map(int, input().split())
    flights = []

    for _ in range(f):
        start, finish = map(int, input().split())
        flights.append((start, finish))

    count, route = wedding_trip(c, flights, home, [a, b, d])
    print(count)

    if route:
        print(*route)
