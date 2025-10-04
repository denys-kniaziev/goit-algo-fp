# Woolf University. Basic Algorithms and Data Structures Course. Final Project

## Overview

This final project integrates key algorithmic and data structure topics — from linked lists to dynamic programming and Monte Carlo simulations.

---

## Task 1 – Linked List Operations

Implement a singly linked list with:

* **Reversal** – reverse node links in-place.
* **Sorting** – implement insertion sort or merge sort for the list.
* **Merging** – merge two sorted linked lists into one sorted list.

---

## Task 2 – Recursive Fractal “Pythagoras Tree”

Use recursion to draw the **Pythagoras tree** fractal. The user should be able to specify the recursion depth. Visualize the fractal graphically.

---

## Task 3 – Dijkstra’s Algorithm with Heap

Implement **Dijkstra’s shortest path algorithm** using a **binary heap** for vertex selection. Build a weighted graph and compute shortest paths from a start node to all others.

---

## Task 4 – Heap Visualization

Analyze the given binary tree visualization code and adapt it to display a **binary heap structure**. Use the node color and hierarchy logic from the base code to represent heap relationships.

---

## Task 5 – Binary Tree Traversal Visualization

Based on the visualization code, create a program that visually demonstrates:

* **Depth-first traversal** (using a stack)
* **Breadth-first traversal** (using a queue)

Each visited node should receive a unique RGB color code, changing from dark to light shades according to the traversal order.

---

## Task 6 – Greedy and Dynamic Food Selection

Given menu items with cost and calories, develop two approaches to maximize total calories within a limited budget:

* **Greedy algorithm** (`greedy_algorithm`) – maximize the calories-to-cost ratio.
* **Dynamic programming** (`dynamic_programming`) – compute the optimal combination.

```python
items = {
  "pizza": {"cost": 50, "calories": 300},
  "hamburger": {"cost": 40, "calories": 250},
  "hot-dog": {"cost": 30, "calories": 200},
  "pepsi": {"cost": 10, "calories": 100},
  "cola": {"cost": 15, "calories": 220},
  "potato": {"cost": 25, "calories": 350}
}
```

Compare both algorithms and analyze efficiency.

---

## Task 7 – Monte Carlo Dice Simulation

Simulate rolling two dice many times and estimate the probability of each possible sum (2–12).

* Count occurrences for each sum.
* Compute probabilities based on simulations.
* Visualize results as a **table or chart**.
* Compare simulated results with theoretical probabilities.
