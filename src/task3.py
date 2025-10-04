import heapq
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    """Weighted graph implementation for Dijkstra's algorithm"""
    
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        self.vertices.add(vertex)
    
    def add_edge(self, from_vertex, to_vertex, weight):
        """Add a weighted edge between two vertices"""
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)
        self.edges[from_vertex].append((to_vertex, weight))
        # For undirected graph, add reverse edge
        self.edges[to_vertex].append((from_vertex, weight))
    
    def get_neighbors(self, vertex):
        """Get neighbors of a vertex with weights"""
        return self.edges[vertex]


def dijkstra(graph, start_vertex):
    """
    Dijkstra's algorithm using binary heap for shortest paths
    
    Args:
        graph: Graph object
        start_vertex: starting vertex
    
    Returns:
        tuple: (distances dict, previous vertices dict)
    """
    # Initialize distances and previous vertices
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    previous = {vertex: None for vertex in graph.vertices}
    distances[start_vertex] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start_vertex)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Skip if already processed
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Check all neighbors
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if neighbor in visited:
                continue
            
            # Calculate new distance
            new_distance = current_distance + weight
            
            # Update if shorter path found
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (new_distance, neighbor))
    
    return distances, previous


def reconstruct_path(previous, start, end):
    """Reconstruct path from start to end using previous vertices"""
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    
    # Check if path exists
    if path[0] != start:
        return None
    
    return path


def visualize_graph_with_paths(graph, start_vertex, distances, previous):
    """Visualize graph with shortest paths"""
    # Create networkx graph for visualization
    G = nx.Graph()
    
    # Add edges with weights
    for vertex in graph.vertices:
        for neighbor, weight in graph.get_neighbors(vertex):
            if not G.has_edge(vertex, neighbor):  # Avoid duplicate edges
                G.add_edge(vertex, neighbor, weight=weight)
    
    # Create layout
    pos = nx.spring_layout(G, seed=42, k=3, iterations=50)
    
    plt.figure(figsize=(12, 8))
    
    # Draw graph
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=800, alpha=0.9)
    
    # Highlight start vertex
    nx.draw_networkx_nodes(G, pos, nodelist=[start_vertex], 
                          node_color='red', node_size=800)
    
    nx.draw_networkx_edges(G, pos, alpha=0.5, width=1)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)
    
    plt.title(f'Graph with Shortest Paths from Vertex {start_vertex}', 
              fontsize=14, fontweight='bold')
    plt.axis('off')
    
    # Add distance information
    distance_text = "Shortest Distances:\n"
    for vertex in sorted(graph.vertices):
        dist = distances[vertex]
        if dist == float('infinity'):
            distance_text += f"{start_vertex} → {vertex}: ∞\n"
        else:
            distance_text += f"{start_vertex} → {vertex}: {dist}\n"
    
    plt.figtext(0.02, 0.98, distance_text, fontsize=10, 
                verticalalignment='top', bbox=dict(boxstyle='round', 
                facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.show()


def create_sample_graph():
    """Create a sample weighted graph for demonstration"""
    graph = Graph()
    
    # Add edges with weights
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3)
    ]
    
    for from_v, to_v, weight in edges:
        graph.add_edge(from_v, to_v, weight)
    
    return graph


def demo():
    """Demonstration of Dijkstra's algorithm"""
    print("=== Task 3: Dijkstra's Algorithm ===")
    
    # Create sample graph
    graph = create_sample_graph()
    
    print(f"Graph vertices: {sorted(graph.vertices)}")
    print("Graph edges:")
    for vertex in sorted(graph.vertices):
        neighbors = graph.get_neighbors(vertex)
        if neighbors:
            print(f"  {vertex}: {neighbors}")
    
    # Test Dijkstra from different starting points
    start_vertices = ['A', 'D']
    
    for start in start_vertices:
        print(f"\n--- Shortest paths from vertex {start} ---")
        
        distances, previous = dijkstra(graph, start)
        
        print("Distances:")
        for vertex in sorted(graph.vertices):
            dist = distances[vertex]
            if dist == float('infinity'):
                print(f"  {start} → {vertex}: ∞")
            else:
                print(f"  {start} → {vertex}: {dist}")
        
        print("\nPaths:")
        for vertex in sorted(graph.vertices):
            if vertex != start and distances[vertex] != float('infinity'):
                path = reconstruct_path(previous, start, vertex)
                if path:
                    path_str = " → ".join(path)
                    print(f"  {start} → {vertex}: {path_str} (distance: {distances[vertex]})")
        
        # Visualize
        print(f"\nVisualizing graph with shortest paths from {start}...")
        visualize_graph_with_paths(graph, start, distances, previous)


if __name__ == "__main__":
    demo()