from json.encoder import INFINITY


def shortest_distance(graph, start):

    # Create a dictionary to store visited graph points
    visited = {}

    # Create an empty array that will store the unvisited points
    unvisited = []

    # Initialize dictionary values for each point
    for let in graph.keys():
        unvisited.append(let)

        # If the current letter matches the start letter then initialize to 0
        if let == start:
            visited[let] = 0
        else:
            visited[let] = float(INFINITY)

    # Iterate through each point in unvisited
    for point in unvisited:

        # Iterate through each adjacent point to that point
        for adj_point, val in graph[point].items():

            # If that point and its path is less than that previously stored in visited then replace it
            if visited[adj_point] > val + visited[point]:
                visited[adj_point] = val + visited[point]

    print(f"The shortests paths are {visited}")


graph1 = {
    "A": {"B": 6, "D": 1},
    "B": {"A": 6, "C": 5, "D": 2, "E": 2},
    "C": {"B": 5, "E": 2},
    "D": {"A": 1, "B": 2, "E": 1},
    "E": {"B": 2, "C": 5, "D": 1},
}

graph2 = {
    "U": {"V": 6, "W": 7},
    "V": {"U": 6, "X": 10},
    "W": {"U": 7, "X": 1},
    "X": {"W": 1, "V": 10},
}

shortest_distance(graph1, "A")  # Answer = {'A': 0, 'B': 3, 'C': 7, 'D': 1, 'E': 2}
shortest_distance(graph2, "U")  # Answer = {'U': 0, 'V': 6, 'W': 7, 'X': 8}
