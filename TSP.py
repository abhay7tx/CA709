# Number of vertices
n = 4

# Adjacency Matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Stores the path
path = [-1] * n

# Start from vertex 0
path[0] = 0


# Check if vertex v can be added at position pos
def isSafe(v, pos):

    # There should be an edge from previous vertex
    if graph[path[pos - 1]][v] == 0:
        return False

    # Vertex should not already be in the path
    for i in range(pos):
        if path[i] == v:
            return False

    return True


# Backtracking function
def solve(pos):

    # All vertices are included
    if pos == n:

        # Check if last vertex connects to first
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        return False

    # Try every vertex except 0
    for v in range(1, n):

        if isSafe(v, pos):

            # Add vertex
            path[pos] = v

            # Recur for next position
            if solve(pos + 1):
                return True

            # Backtrack
            path[pos] = -1

    return False


if solve(1):
    print("Hamiltonian Cycle:")
    print(*path, path[0])
else:
    print("No Hamiltonian Cycle")