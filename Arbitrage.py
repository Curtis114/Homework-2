liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
import math
from collections import defaultdict

def calculate_amount_out(amount_in, liquidity_in, liquidity_out, fee=0.003):
    """Calculate the amount of token received from a trade."""
    # Deduct the fee
    amount_in_with_fee = amount_in * (1 - fee)

    # Apply Uniswap V2 formula
    new_liquidity_in = liquidity_in + amount_in_with_fee
    new_liquidity_out = liquidity_in * liquidity_out / new_liquidity_in
    amount_out = liquidity_out - new_liquidity_out

    return amount_out

def execute_trade(path, initial_balance, liquidity):
    """Execute a series of trades along a path and return the final balance."""
    balance = initial_balance
    for i in range(len(path) - 1):
        token_in, token_out = path[i], path[i+1]
        if (token_in, token_out) in liquidity:
            balance = calculate_amount_out(balance, *liquidity[(token_in, token_out)])
        elif (token_out, token_in) in liquidity:
            # Reverse the pair if needed
            balance = calculate_amount_out(balance, *liquidity[(token_out, token_in)][::-1])
        else:
            return None  # Invalid path or missing liquidity data
    return balance

def create_graph(liquidity):
    graph = defaultdict(dict)
    for (token1, token2), (amount1, amount2) in liquidity.items():
        rate1 = amount2 / amount1
        rate2 = amount1 / amount2
        graph[token1][token2] = rate1
        graph[token2][token1] = rate2
    return graph

def find_all_paths(graph, start, end, path=[], max_depth=8, current_depth=0):
    path = path + [start]
    current_depth += 1

    if start == end and len(path) > 1:
        return [path]

    if current_depth > max_depth:
        return []

    paths = []
    for node in graph[start]:
        if node != end and node in path:
            continue

        newpaths = find_all_paths(graph, node, end, path, max_depth, current_depth)
        paths.extend(newpaths)

    return paths

def calculate_balance(graph, path, initial_balance):
    balance = initial_balance
    for i in range(len(path) - 1):
        balance *= graph[path[i]][path[i + 1]]
    return balance

graph = create_graph(liquidity)

def find_arbitrage_opportunity_for_tokenB(initial_balance, target_balance, liquidity):
    start_token = "tokenB"
    graph = create_graph(liquidity)

    best_balance = 0
    best_path = None

    for path in find_all_paths(graph, start_token, start_token):
        final_balance = execute_trade(path, initial_balance, liquidity)
        if final_balance is not None and final_balance > best_balance:
            best_balance = final_balance
            best_path = path

            if final_balance > target_balance:
                return path, final_balance

    return best_path, best_balance

def print_graph(graph):
    for token, neighbors in graph.items():
        print(f"{token}: {neighbors}")

# print_graph(graph)

arbitrage_path, final_balance = find_arbitrage_opportunity_for_tokenB(5, 20, liquidity)

if arbitrage_path:
    print(f"path: {'->'.join(arbitrage_path)}, {arbitrage_path[0]} balance={final_balance}")
else:
    print("No arbitrage opportunity found for tokenB that meets the target balance")

def calculate_amount_out(amount_in, liquidity_in, liquidity_out, fee=0.003):
    amount_in_with_fee = amount_in * (1 - fee)
    new_liquidity_in = liquidity_in + amount_in_with_fee
    new_liquidity_out = liquidity_in * liquidity_out / new_liquidity_in
    amount_out = liquidity_out - new_liquidity_out
    return amount_out

initial_balance = 5  # tokenB
path = arbitrage_path
amount_in = initial_balance


for i in range(len(path) - 1):
    token_in, token_out = path[i], path[i+1]
    if (token_in, token_out) in liquidity:
        amount_out = calculate_amount_out(amount_in, *liquidity[(token_in, token_out)])
    elif (token_out, token_in) in liquidity:
        amount_out = calculate_amount_out(amount_in, *liquidity[(token_out, token_in)][::-1])
    
    print(f"Swap {token_in} to {token_out}: amountIn = {amount_in}, amountOut = {amount_out}")
    amount_in = amount_out  

final_balance = amount_in
print(f"Final balance in tokenB: {final_balance}")