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
    
    def move_zero(self, curr_node, del_x, del_y):
        node = self.create_node_copy(curr_node)
        zero_position = np.argwhere(node.node_state_i==0)[0]
        new_pos_y, new_pos_x = (zero_position[0] + del_y), (zero_position[1] + del_x)
        if(new_pos_y >= 0 and new_pos_y < node.node_state_i.shape[0] and new_pos_x >= 0 and new_pos_x < node.node_state_i.shape[1]):
            node = self.swap_position(node, zero_position[0], zero_position[1], new_pos_y, new_pos_x)
            node.node_index_i = len(self.visited_nodes)
            node.parent_node_index_i = curr_node.node_index_i
            if not self.already_exists(node):
                new = True
                return new, node
            else:
                new = False
                return new, curr_node
        else:
            new = False
            return new, curr_node
    
    def already_exists(self, node):
        for i in self.visited_nodes:
            if(i.node_state_i == node.node_state_i).all():
                return True
        return False
    
    def ActionMoveLeft(self, node):
        status, new_node = self.move_zero(node , -1, 0)
        return status, new_node

    def ActionMoveUp(self, node):
        status, new_node = self.move_zero(node , 0, -1)
        return status, new_node

    def ActionMoveRight(self, node):
        status, new_node = self.move_zero(node , 1, 0)
        return status, new_node

    def ActionMoveDown(self, node):
        status, new_node = self.move_zero(node , 0, 1)
        return status, new_node