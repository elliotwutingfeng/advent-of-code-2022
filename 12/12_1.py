with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

grid = [[x for x in line] for line in lines]

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "S":
            source = (x, y)
            grid[x][y] = "a"
        if grid[x][y] == "E":
            destination = (x, y)
            grid[x][y] = "z"


def is_at_most_one_higher(start, end):
    return ord(end) - 1 <= ord(start)


assert is_at_most_one_higher("x", "v") is True
assert is_at_most_one_higher("x", "w") is True
assert is_at_most_one_higher("x", "x") is True
assert is_at_most_one_higher("x", "y") is True
assert is_at_most_one_higher("x", "z") is False


graph: dict = {}
for x in range(len(grid)):
    for y in range(len(grid[0])):
        val = grid[x][y]
        neighbors = {
            k: 1
            for k in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if 0 <= k[0] < len(grid)
            and 0 <= k[1] < len(grid[0])
            and is_at_most_one_higher(val, grid[k[0]][k[1]])
        }
        graph[(x, y)] = neighbors


def find_shortest_path(graph, source, destination) -> float:
    """
    Dijkstra's algorithm
    """

    def get_keys(dictionary) -> set[str]:
        """
        Get all keys in nested dict
        """
        result = set()
        for key, value in dictionary.items():
            if type(value) is dict:
                new_keys = get_keys(value)
                result.add(key)
                result.update(new_keys)
            else:
                result.add(key)
        return result

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in (node for node in costs if node not in processed):
            cost = costs[node]
            if cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    all_nodes = get_keys(graph)
    if source not in all_nodes or destination not in all_nodes:
        return -1
    costs = {**{node: float("inf") for node in all_nodes}, **graph[source]}
    parents = {
        **{destination: None for _ in all_nodes},
        **{k: source for k in graph[source]},
    }

    processed = set()
    while (node := find_lowest_cost_node(costs)) is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)

    return costs[destination]


cost = find_shortest_path(graph, source, destination)
print(cost)
