import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_simulations=100000):
    """
    Monte Carlo simulation of dice rolls
    
    Args:
        num_simulations: number of dice roll simulations to perform
    
    Returns:
        dict: sum frequencies and probabilities
    """
    sum_counts = {i: 0 for i in range(2, 13)}  # Possible sums: 2-12
    
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sum_counts[total] += 1
    
    # Convert counts to probabilities
    sum_probabilities = {}
    for sum_value, count in sum_counts.items():
        sum_probabilities[sum_value] = count / num_simulations
    
    return sum_counts, sum_probabilities


def analytical_probabilities():
    """
    Calculate analytical probabilities for dice sums
    
    Returns:
        dict: analytical probabilities for each sum
    """
    # All possible ways to get each sum
    sum_ways = {
        2: 1,   # (1,1)
        3: 2,   # (1,2), (2,1)
        4: 3,   # (1,3), (2,2), (3,1)
        5: 4,   # (1,4), (2,3), (3,2), (4,1)
        6: 5,   # (1,5), (2,4), (3,3), (4,2), (5,1)
        7: 6,   # (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
        8: 5,   # (2,6), (3,5), (4,4), (5,3), (6,2)
        9: 4,   # (3,6), (4,5), (5,4), (6,3)
        10: 3,  # (4,6), (5,5), (6,4)
        11: 2,  # (5,6), (6,5)
        12: 1   # (6,6)
    }
    
    total_outcomes = 36  # 6 * 6 possible combinations
    
    analytical_probs = {}
    for sum_value, ways in sum_ways.items():
        analytical_probs[sum_value] = ways / total_outcomes
    
    return analytical_probs


def create_probability_table(monte_carlo_probs, analytical_probs, num_simulations):
    """Create comparison table of probabilities"""
    print(f"\n=== Probability Comparison Table ({num_simulations:,} simulations) ===")
    print(f"{'Sum':<4} {'Monte Carlo':<12} {'Analytical':<12} {'Difference':<12} {'MC %':<8} {'Analytical %':<12}")
    print("-" * 70)
    
    table_data = []
    for sum_value in range(2, 13):
        mc_prob = monte_carlo_probs[sum_value]
        anal_prob = analytical_probs[sum_value]
        difference = abs(mc_prob - anal_prob)
        
        table_data.append({
            'Sum': sum_value,
            'Monte Carlo': mc_prob,
            'Analytical': anal_prob,
            'Difference': difference,
            'MC %': f"{mc_prob * 100:.2f}%",
            'Analytical %': f"{anal_prob * 100:.2f}%"
        })
        
        print(f"{sum_value:<4} {mc_prob:<12.6f} {anal_prob:<12.6f} {difference:<12.6f} "
              f"{mc_prob * 100:<8.2f} {anal_prob * 100:<12.2f}")
    
    return table_data


def plot_probability_comparison(monte_carlo_probs, analytical_probs, num_simulations):
    """Create visualization comparing Monte Carlo and analytical results"""
    sums = list(range(2, 13))
    mc_probs = [monte_carlo_probs[s] for s in sums]
    anal_probs = [analytical_probs[s] for s in sums]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Bar chart comparison
    x = range(len(sums))
    width = 0.35
    
    ax1.bar([i - width/2 for i in x], mc_probs, width, 
            label=f'Monte Carlo ({num_simulations:,} sims)', alpha=0.8, color='skyblue')
    ax1.bar([i + width/2 for i in x], anal_probs, width, 
            label='Analytical', alpha=0.8, color='orange')
    
    ax1.set_xlabel('Sum of Two Dice')
    ax1.set_ylabel('Probability')
    ax1.set_title('Probability Comparison: Monte Carlo vs Analytical')
    ax1.set_xticks(x)
    ax1.set_xticklabels(sums)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Error plot
    errors = [abs(monte_carlo_probs[s] - analytical_probs[s]) for s in sums]
    ax2.bar(sums, errors, color='red', alpha=0.7)
    ax2.set_xlabel('Sum of Two Dice')
    ax2.set_ylabel('Absolute Error')
    ax2.set_title('Absolute Error: |Monte Carlo - Analytical|')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Additional statistical chart
    plt.figure(figsize=(12, 8))
    
    # Create percentage comparison
    mc_percentages = [p * 100 for p in mc_probs]
    anal_percentages = [p * 100 for p in anal_probs]
    
    plt.bar([i - 0.2 for i in sums], mc_percentages, 0.4, 
            label=f'Monte Carlo ({num_simulations:,})', alpha=0.8, color='lightcoral')
    plt.bar([i + 0.2 for i in sums], anal_percentages, 0.4, 
            label='Analytical', alpha=0.8, color='lightgreen')
    
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability (%)')
    plt.title('Dice Roll Probability Distribution')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(sums)
    
    # Add percentage labels on bars
    for i, (mc_pct, anal_pct) in enumerate(zip(mc_percentages, anal_percentages)):
        plt.text(sums[i] - 0.2, mc_pct + 0.2, f'{mc_pct:.1f}%', 
                ha='center', va='bottom', fontsize=9)
        plt.text(sums[i] + 0.2, anal_pct + 0.2, f'{anal_pct:.1f}%', 
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.show()


def analyze_convergence():
    """Analyze how Monte Carlo results converge to analytical values"""
    print("\n=== Convergence Analysis ===")
    
    analytical_probs = analytical_probabilities()
    simulation_sizes = [1000, 10000, 50000, 100000, 500000, 1000000]
    
    convergence_data = []
    
    for sim_size in simulation_sizes:
        _, mc_probs = monte_carlo_simulation(sim_size)
        
        # Calculate average absolute error
        total_error = sum(abs(mc_probs[s] - analytical_probs[s]) for s in range(2, 13))
        avg_error = total_error / 11  # 11 possible sums
        
        convergence_data.append({
            'Simulations': sim_size,
            'Average Error': avg_error,
            'Max Error': max(abs(mc_probs[s] - analytical_probs[s]) for s in range(2, 13))
        })
        
        print(f"Simulations: {sim_size:>7,} | Avg Error: {avg_error:.6f} | Max Error: {convergence_data[-1]['Max Error']:.6f}")
    
    # Plot convergence
    plt.figure(figsize=(10, 6))
    sim_counts = [data['Simulations'] for data in convergence_data]
    avg_errors = [data['Average Error'] for data in convergence_data]
    max_errors = [data['Max Error'] for data in convergence_data]
    
    plt.loglog(sim_counts, avg_errors, 'o-', label='Average Error', linewidth=2, markersize=8)
    plt.loglog(sim_counts, max_errors, 's-', label='Maximum Error', linewidth=2, markersize=8)
    
    plt.xlabel('Number of Simulations')
    plt.ylabel('Error')
    plt.title('Monte Carlo Convergence Analysis')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def demo():
    """Main demonstration of Monte Carlo dice simulation"""
    print("=== Task 7: Monte Carlo Dice Roll Simulation ===")
    
    # Set random seed for reproducibility (optional)
    random.seed(42)
    
    # Run simulation
    num_simulations = 1000000
    print(f"Running Monte Carlo simulation with {num_simulations:,} dice rolls...")
    
    sum_counts, monte_carlo_probs = monte_carlo_simulation(num_simulations)
    analytical_probs = analytical_probabilities()
    
    # Display results
    create_probability_table(monte_carlo_probs, analytical_probs, num_simulations)
    
    # Create visualizations
    plot_probability_comparison(monte_carlo_probs, analytical_probs, num_simulations)
    
    # Analyze convergence
    analyze_convergence()
    
    # Summary analysis
    print(f"\n=== Summary Analysis ===")
    total_diff = sum(abs(monte_carlo_probs[s] - analytical_probs[s]) for s in range(2, 13))
    avg_diff = total_diff / 11
    
    print(f"Average absolute difference: {avg_diff:.6f}")
    print(f"Average percentage error: {(avg_diff * 100):.4f}%")
    
    print(f"\nWith {num_simulations:,} simulations, the Monte Carlo method")
    print(f"approximates the theoretical probabilities very closely.")
    print(f"The largest errors typically occur for the least probable sums (2 and 12).")
    print(f"As the number of simulations increases, the results converge to the analytical values.")


if __name__ == "__main__":
    demo()
