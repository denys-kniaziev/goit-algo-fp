from typing import Optional

import uuid
import heapq
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


def draw_tree(tree_root, title="Binary Tree"):
    """Draw binary tree using networkx"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, 
            node_color=colors, font_size=12, font_weight='bold')
    plt.title(title, fontsize=16, fontweight='bold')
    plt.show()


def heapify_up(heap, index):
    """Helper function to maintain heap property upward"""
    if index == 0:
        return
    
    parent_index = (index - 1) // 2
    if heap[index] < heap[parent_index]:  # Min heap
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        heapify_up(heap, parent_index)


def array_to_heap_tree(heap_array):
    """
    Convert array representation of heap to binary tree
    
    Args:
        heap_array: list representing binary heap
    
    Returns:
        Node: root of the binary tree
    """
    if not heap_array:
        return None
    
    # Create nodes for all elements
    nodes = [Node(val) for val in heap_array]
    
    # Build tree structure following heap indexing
    for i in range(len(heap_array)):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        
        if left_child_index < len(heap_array):
            nodes[i].left = nodes[left_child_index]
        
        if right_child_index < len(heap_array):
            nodes[i].right = nodes[right_child_index]
    
    return nodes[0]  # Return root


def visualize_heap(values):
    """
    Visualize binary heap from array of values
    
    Args:
        values: list of values to create heap from
    """
    # Create min heap
    heap = values.copy()
    heapq.heapify(heap)
    
    print(f"Original array: {values}")
    print(f"Min heap array: {heap}")
    
    # Convert to tree and visualize
    root = array_to_heap_tree(heap)
    draw_tree(root, f"Binary Min Heap: {heap}")
    
    return heap


def demonstrate_heap_operations():
    """Demonstrate various heap operations with visualization"""
    print("=== Task 4: Binary Heap Visualization ===")
    
    # Example 1: Simple heap
    print("\n1. Creating heap from simple array:")
    values1 = [4, 10, 3, 5, 1, 6, 8]
    heap1 = visualize_heap(values1)
    
    # Example 2: Adding elements one by one
    print("\n2. Building heap step by step:")
    heap2 = []
    elements_to_add = [15, 10, 20, 8, 25, 5, 7]
    
    for elem in elements_to_add:
        heapq.heappush(heap2, elem)
        print(f"Added {elem}, heap: {heap2}")
        root = array_to_heap_tree(heap2)
        draw_tree(root, f"Heap after adding {elem}: {heap2}")
    
    # Example 3: Extracting minimum elements
    print("\n3. Extracting minimum elements:")
    heap3 = [1, 3, 6, 5, 2, 8, 10, 15, 9, 12]
    heapq.heapify(heap3)
    print(f"Initial heap: {heap3}")
    
    original_heap = heap3.copy()
    root = array_to_heap_tree(original_heap)
    draw_tree(root, f"Original Heap: {original_heap}")
    
    extracted = []
    for _ in range(3):
        min_val = heapq.heappop(heap3)
        extracted.append(min_val)
        print(f"Extracted {min_val}, remaining heap: {heap3}")
        
        if heap3:  # Only visualize if heap is not empty
            root = array_to_heap_tree(heap3)
            draw_tree(root, f"Heap after extracting {min_val}: {heap3}")
    
    print(f"Extracted elements in order: {extracted}")


def create_custom_heap():
    """Interactive heap creation"""
    print("\n=== Custom Heap Creation ===")
    print("Enter numbers separated by spaces (or press Enter for default):")
    
    user_input = input().strip()
    
    if user_input:
        try:
            values = list(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. Using default values.")
            values = [20, 15, 8, 10, 5, 7, 6, 2, 9, 1]
    else:
        values = [20, 15, 8, 10, 5, 7, 6, 2, 9, 1]
    
    print(f"Creating heap from: {values}")
    visualize_heap(values)


def demo():
    """Main demonstration function"""
    demonstrate_heap_operations()
    create_custom_heap()


if __name__ == "__main__":
    demo()
