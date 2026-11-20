def network_delay(r, wires, entries):
    graph = [[] for _ in range(r + 1)]
    total_length = 0

    for a, b, weight in wires:
        graph[a].append((b, weight))
        graph[b].append((a, weight))
        total_length += weight

    distance = [total_length + 1] * (r + 1)
    buckets = [[] for _ in range(total_length + 1)]

    for router in entries:
        if distance[router] != 0:
            distance[router] = 0
            buckets[0].append(router)

    for current in range(total_length + 1):
        while buckets[current]:
            router = buckets[current].pop()

            if distance[router] != current:
                continue

            for neighbor, weight in graph[router]:
                new_distance = current + weight

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    buckets[new_distance].append(neighbor)

    if total_length + 1 in distance[1:]:
        return -1

    return sum(distance[1:])


if __name__ == "__main__":
    r, m, k = map(int, input().split())
    entries = list(map(int, input().split()))
    wires = []

    for _ in range(m):
        a, b, weight = map(int, input().split())
        wires.append((a, b, weight))

    print(network_delay(r, wires, entries))
