import numpy as np

class PuzzleNode:
    def __init__(self, node_state_i, node_index_i, parent_node_index_i):
        self.node_state_i = node_state_i
        self.node_index_i = node_index_i
        self.parent_node_index_i = parent_node_index_i

class BFS:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.visited_nodes = []
        self.node_queue = []
        self.path_taken = []
        
        initial_node = PuzzleNode(self.initial_state, 0, None)
        self.visited_nodes.append(initial_node)
        self.node_queue.append(initial_node)