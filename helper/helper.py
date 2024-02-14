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
        
    def create_node_copy(self, node):
        copied_node = PuzzleNode(None, None, None)
        copied_node.node_index_i = node.node_index_i
        copied_node.parent_node_index_i = node.parent_node_index_i
        copied_node.node_state_i = node.node_state_i.copy()
        return copied_node

    def swap_position(self, node, curr_y, curr_x, new_y, new_x):
        curr_val = node.node_state_i[curr_y][curr_x]
        new_val = node.node_state_i[new_y][new_x]
        node.node_state_i[curr_y][curr_x] = new_val
        node.node_state_i[new_y][new_x] = curr_val
        return node