import math

# Alpha-Beta Pruning algorithm
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Terminal node (leaf node)
    if depth == 3:
        return values[node_index]
    
    if maximizing_player:
        max_eval = -math.inf
        # Explore the children of this node
        for i in range(2):  # Assuming each node has 2 children
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        # Explore the children of this node
        for i in range(2):  # Assuming each node has 2 children
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Example usage:
# Values at leaf nodes of the game tree
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Initialize alpha to negative infinity and beta to positive infinity
alpha = -math.inf
beta = math.inf

# Start the algorithm: depth = 0, node_index = 0, maximizing_player = True
optimal_value = alpha_beta_pruning(0, 0, True, values, alpha, beta)

# Output the result
print("Optimal value:", optimal_value)
