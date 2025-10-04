import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def draw_rectangle(ax, x, y, width, height, angle, color=(0.6, 0.3, 0.1)):
    """Draw a rotated rectangle"""
    # Calculate rectangle corners
    corners = np.array([
        [-width/2, -height/2],
        [width/2, -height/2],
        [width/2, height/2],
        [-width/2, height/2]
    ])
    
    # Rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Rotate and translate corners
    rotated_corners = np.dot(corners, rotation_matrix.T) + [x, y]
    
    # Create and add rectangle
    rectangle = patches.Polygon(rotated_corners, closed=True, 
                              facecolor=color, edgecolor='black', linewidth=0.5)
    ax.add_patch(rectangle)


def pythagoras_tree(ax, x, y, width, height, angle, level, max_level):
    """
    Recursively draw Pythagoras tree fractal
    
    Args:
        ax: matplotlib axes
        x, y: center position of current rectangle
        width, height: dimensions of current rectangle
        angle: rotation angle
        level: current recursion level
        max_level: maximum recursion level
    """
    if level > max_level:
        return
    
    # Color intensity based on level (darker for deeper levels)
    intensity = 0.3 + 0.7 * (max_level - level) / max_level
    color = (0.6 * intensity, 0.3 * intensity, 0.1 * intensity)
    
    # Draw current rectangle
    draw_rectangle(ax, x, y, width, height, angle, color)
    
    if level < max_level:
        # Calculate positions for next level rectangles
        # Top edge center
        top_x = x + height/2 * np.sin(angle)
        top_y = y + height/2 * np.cos(angle)
        
        # Left branch (45 degrees)
        left_angle = angle + np.pi/4
        left_size = width * np.sqrt(2) / 2
        left_x = top_x + left_size/2 * np.sin(left_angle)
        left_y = top_y + left_size/2 * np.cos(left_angle)
        
        # Right branch (45 degrees)
        right_angle = angle - np.pi/4
        right_size = width * np.sqrt(2) / 2
        right_x = top_x + right_size/2 * np.sin(right_angle)
        right_y = top_y + right_size/2 * np.cos(right_angle)
        
        # Recursive calls
        pythagoras_tree(ax, left_x, left_y, left_size, left_size, 
                       left_angle, level + 1, max_level)
        pythagoras_tree(ax, right_x, right_y, right_size, right_size, 
                       right_angle, level + 1, max_level)


def create_pythagoras_tree(recursion_level):
    """
    Create and display Pythagoras tree fractal
    
    Args:
        recursion_level: number of recursion levels (0-10 recommended)
    """
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    
    # Set up the plot
    ax.set_xlim(-8, 8)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    ax.set_title(f'Pythagoras Tree Fractal (Level {recursion_level})', 
                 fontsize=16, fontweight='bold')
    ax.axis('off')
    
    # Start drawing from the trunk
    trunk_width = 1.7
    trunk_height = 2
    trunk_x = 0
    trunk_y = 1
    
    pythagoras_tree(ax, trunk_x, trunk_y, trunk_width, trunk_height, 
                   0, 0, recursion_level)
    
    plt.tight_layout()
    plt.show()


def demo():
    """Demonstration of Pythagoras tree with different recursion levels"""
    print("=== Task 2: Pythagoras Tree Fractal ===")
    print("Generating Pythagoras tree fractals with different recursion levels...")
    
    # Demo with different levels
    levels = [3, 5, 7]
    
    for level in levels:
        print(f"\\nDisplaying Pythagoras tree with recursion level {level}")
        create_pythagoras_tree(level)
    
    # Interactive mode
    print("\\nInteractive mode:")
    while True:
        try:
            user_level = input("Enter recursion level (0-10, or 'q' to quit): ")
            if user_level.lower() == 'q':
                break
            
            level = int(user_level)
            if 0 <= level <= 10:
                create_pythagoras_tree(level)
            else:
                print("Please enter a level between 0 and 10")
        except ValueError:
            print("Please enter a valid number or 'q' to quit")
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    demo()
