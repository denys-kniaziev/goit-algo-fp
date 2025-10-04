from typing import Optional
import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    """Node class for binary tree visualization"""
    def __init__(self, key, color="skyblue"):
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Add edges and positions for tree visualization"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def generate_color_gradient(steps):
    """Generate color gradient from dark to light"""
    colors = []
    for i in range(steps):
        # Create gradient from dark blue to light blue
        intensity = 0.2 + 0.8 * (i / (steps - 1)) if steps > 1 else 1.0
        # RGB in hex format
        blue_value = int(255 * intensity)
        green_value = int(200 * intensity)
        red_value = int(100 * intensity)
        
        color = f"#{red_value:02x}{green_value:02x}{blue_value:02x}"
        colors.append(color)
    
    return colors


def draw_tree_with_traversal(tree_root, visited_order, traversal_type):
    """Draw tree showing traversal order with color gradient"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    # Generate colors for traversal order
    colors_gradient = generate_color_gradient(len(visited_order))
    node_colors = {}
    
    # Map each node to its traversal order color
    for i, node in enumerate(visited_order):
        node_colors[node.id] = colors_gradient[i]
    
    # Get node colors and labels
    colors = []
    labels = {}
    for node_id in tree.nodes():
        colors.append(node_colors.get(node_id, "lightgray"))
        # Find node by id to get its value
        labels[node_id] = next(node.val for node in visited_order if node.id == node_id)
    
    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, 
            node_color=colors, font_size=12, font_weight='bold')
    
    plt.title(f'{traversal_type} - Order: {[node.val for node in visited_order]}', 
              fontsize=14, fontweight='bold')
    
    # Add legend showing traversal order
    legend_text = f"Traversal Order ({traversal_type}):\n"
    for i, node in enumerate(visited_order):
        legend_text += f"{i + 1}. Node {node.val}\n"
    
    plt.figtext(0.02, 0.95, legend_text, fontsize=10, 
                verticalalignment='top', bbox=dict(boxstyle='round', 
                facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.show()


def dfs_traversal(root):
    """
    Depth-First Search using explicit stack (non-recursive)
    
    Args:
        root: root node of the tree
    
    Returns:
        list: nodes in DFS order
    """
    if not root:
        return []
    
    visited = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        visited.append(node)
        
        # Add children to stack (right first, then left)
        # This ensures left subtree is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return visited


def bfs_traversal(root):
    """
    Breadth-First Search using queue
    
    Args:
        root: root node of the tree
    
    Returns:
        list: nodes in BFS order
    """
    if not root:
        return []
    
    visited = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        visited.append(node)
        
        # Add children to queue (left first, then right)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited


def create_sample_tree():
    """Create sample binary tree for demonstration"""
    # Create tree from the provided example
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    
    return root


def create_larger_tree():
    """Create a larger tree for better visualization"""
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    
    return root


def demo():
    """Demonstration of tree traversal visualization"""
    print("=== Task 5: Binary Tree Traversal Visualization ===")
    
    # Test with original tree structure
    print("\n1. Original tree structure:")
    root1 = create_sample_tree()
    
    print("DFS Traversal (using stack):")
    dfs_result = dfs_traversal(root1)
    print(f"Visit order: {[node.val for node in dfs_result]}")
    draw_tree_with_traversal(root1, dfs_result, "Depth-First Search (DFS)")
    
    print("\nBFS Traversal (using queue):")
    bfs_result = bfs_traversal(root1)
    print(f"Visit order: {[node.val for node in bfs_result]}")
    draw_tree_with_traversal(root1, bfs_result, "Breadth-First Search (BFS)")
    
    # Test with larger tree
    print("\n2. Larger tree structure:")
    root2 = create_larger_tree()
    
    print("DFS Traversal (using stack):")
    dfs_result2 = dfs_traversal(root2)
    print(f"Visit order: {[node.val for node in dfs_result2]}")
    draw_tree_with_traversal(root2, dfs_result2, "DFS - Larger Tree")
    
    print("\nBFS Traversal (using queue):")
    bfs_result2 = bfs_traversal(root2)
    print(f"Visit order: {[node.val for node in bfs_result2]}")
    draw_tree_with_traversal(root2, bfs_result2, "BFS - Larger Tree")
    
    # Compare traversals
    print("\n=== Comparison ===")
    print(f"Original tree - DFS: {[node.val for node in dfs_result]}")
    print(f"Original tree - BFS: {[node.val for node in bfs_result]}")
    print(f"Larger tree - DFS: {[node.val for node in dfs_result2]}")
    print(f"Larger tree - BFS: {[node.val for node in bfs_result2]}")


if __name__ == "__main__":
    demo()