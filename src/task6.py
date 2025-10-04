def greedy_algorithm(items, budget):
    """
    Greedy algorithm for food selection based on calories/cost ratio
    
    Args:
        items: dictionary with food items and their cost/calories
        budget: maximum budget available
    
    Returns:
        tuple: (selected_items list, total_cost, total_calories)
    """
    # Calculate efficiency (calories per cost unit) for each item
    efficiency_list = []
    for name, info in items.items():
        efficiency = info['calories'] / info['cost']
        efficiency_list.append((efficiency, name, info['cost'], info['calories']))
    
    # Sort by efficiency in descending order
    efficiency_list.sort(reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for efficiency, name, cost, calories in efficiency_list:
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories
    
    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    """
    Dynamic programming solution for optimal food selection
    
    Args:
        items: dictionary with food items and their cost/calories
        budget: maximum budget available
    
    Returns:
        tuple: (selected_items list, total_cost, total_calories)
    """
    # Convert items to lists for easier indexing
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]
    n = len(items)
    
    # Create DP table: dp[i][w] = maximum calories with first i items and budget w
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(budget + 1):
            # Don't take the current item
            dp[i][w] = dp[i-1][w]
            
            # Take the current item if it fits
            if costs[i-1] <= w:
                with_current = dp[i-1][w - costs[i-1]] + calories[i-1]
                dp[i][w] = max(dp[i][w], with_current)
    
    # Backtrack to find which items were selected
    selected_items = []
    total_cost = 0
    total_calories = dp[n][budget]
    
    w = budget
    for i in range(n, 0, -1):
        # If the value comes from including the current item
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_names[i-1])
            total_cost += costs[i-1]
            w -= costs[i-1]
    
    return selected_items, total_cost, total_calories


def compare_algorithms(items, budget):
    """Compare greedy and dynamic programming solutions"""
    print(f"\n=== Comparison for budget: {budget} ===")
    
    # Greedy algorithm
    greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
    
    # Dynamic programming
    dp_items, dp_cost, dp_calories = dynamic_programming(items, budget)
    
    print("\nGreedy Algorithm Results:")
    print(f"Selected items: {greedy_items}")
    print(f"Total cost: {greedy_cost}")
    print(f"Total calories: {greedy_calories}")
    if greedy_cost > 0:
        print(f"Cost efficiency: {greedy_calories/greedy_cost:.2f} calories per unit cost")
    else:
        print("Cost efficiency: N/A (no items selected)")
    
    print("\nDynamic Programming Results:")
    print(f"Selected items: {dp_items}")
    print(f"Total cost: {dp_cost}")
    print(f"Total calories: {dp_calories}")
    if dp_cost > 0:
        print(f"Cost efficiency: {dp_calories/dp_cost:.2f} calories per unit cost")
    else:
        print("Cost efficiency: N/A (no items selected)")
    
    print(f"\nComparison:")
    print(f"Calories difference: {dp_calories - greedy_calories}")
    print(f"Cost difference: {dp_cost - greedy_cost}")
    
    if greedy_calories > 0 and dp_calories > greedy_calories:
        improvement = ((dp_calories - greedy_calories) / greedy_calories) * 100
        print(f"DP provides {improvement:.1f}% more calories than greedy")
    elif dp_calories == greedy_calories:
        print("Both algorithms provide the same total calories")
    elif greedy_calories == 0:
        print("No items can be selected within the budget")
    else:
        print("Greedy algorithm performed better (unlikely scenario)")
    
    return (greedy_items, greedy_cost, greedy_calories), (dp_items, dp_cost, dp_calories)


def analyze_item_efficiency(items):
    """Analyze the efficiency of each food item"""
    print("\n=== Food Item Analysis ===")
    print(f"{'Item':<12} {'Cost':<6} {'Calories':<9} {'Efficiency':<12}")
    print("-" * 45)
    
    efficiency_data = []
    for name, info in items.items():
        efficiency = info['calories'] / info['cost']
        efficiency_data.append((name, info['cost'], info['calories'], efficiency))
        print(f"{name:<12} {info['cost']:<6} {info['calories']:<9} {efficiency:<12.2f}")
    
    # Sort by efficiency and show ranking
    efficiency_data.sort(key=lambda x: x[3], reverse=True)
    print(f"\nEfficiency Ranking (calories per cost unit):")
    for i, (name, cost, calories, eff) in enumerate(efficiency_data, 1):
        print(f"{i}. {name}: {eff:.2f}")
    
    return efficiency_data


def demo():
    """Demonstration of greedy and dynamic programming algorithms"""
    print("=== Task 6: Greedy Algorithm vs Dynamic Programming ===")
    
    # Food items data
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    # Analyze item efficiency
    analyze_item_efficiency(items)
    
    # Test with different budgets
    budgets = [50, 100, 150, 200]
    
    for budget in budgets:
        compare_algorithms(items, budget)
    
    # Additional analysis
    print(f"\n=== Summary Analysis ===")
    print("The greedy algorithm selects items based on calories/cost ratio,")
    print("which works well when items are 'fractionally' divisible.")
    print("However, since we can't buy fractions of food items, dynamic")
    print("programming often finds better combinations by considering")
    print("all possible selections within the budget constraint.")

if __name__ == "__main__":
    demo()
