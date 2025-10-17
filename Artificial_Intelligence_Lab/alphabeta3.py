import math

# Define the alpha-beta pruning function
def alpha_beta(node, depth, alpha, beta, maximizingPlayer, values, tree):
    if depth == 0 or node not in tree:
        return values[node]

    if maximizingPlayer:
        value = -math.inf
        for child in tree[node]:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False, values, tree))
            alpha = max(alpha, value)
            if beta <= alpha:
                break   # β cut-off
        return value
    else:
        value = math.inf
        for child in tree[node]:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True, values, tree))
            beta = min(beta, value)
            if beta <= alpha:
                break   # α cut-off
        return value

# Tree structure
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
}

# Heuristic values of the leaf nodes
values = {
    'H': 3,
    'I': 5,
    'J': 6,
    'K': 9,
    'L': 1,
    'M': 2,
    'N': 0,
    'O': -1
}

# Run Alpha-Beta pruning
optimal_value = alpha_beta('A', 3, -math.inf, math.inf, True, values, tree)

print("Optimal value (with Alpha-Beta Pruning):", optimal_value)
