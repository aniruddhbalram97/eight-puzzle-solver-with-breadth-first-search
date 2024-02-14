import numpy as np

import sys

sys.setrecursionlimit(1000000000)

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
        
        self.initial_node = PuzzleNode(self.initial_state, 0, None)
        self.visited_nodes.append(self.initial_node)
        self.node_queue.append(self.initial_node)
        
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
    
    def algorithm(self, node):
        moved = False
        if(node.node_state_i == self.goal_state).all():
            self.visited_nodes.append(node)
            self.generate_paths(node)
            return
        else:
            status, new_node = self.ActionMoveLeft(node)
            if (status):
                self.visited_nodes.append(new_node)
                self.node_queue.append(new_node)
                moved = True
            if(new_node.node_state_i == self.goal_state).all():
                print("GOAL!")
                self.generate_paths(new_node)
                return
            status, new_node = self.ActionMoveRight(node)
            if (status):
                self.visited_nodes.append(new_node)
                self.node_queue.append(new_node)
                moved = True
            if(new_node.node_state_i == self.goal_state).all():
                print("GOAL!")
                self.generate_paths(new_node)
                return
            status, new_node = self.ActionMoveUp(node)
            if (status):
                self.visited_nodes.append(new_node)
                self.node_queue.append(new_node)
                moved = True
            if(new_node.node_state_i == self.goal_state).all():
                print("GOAL!")
                self.generate_paths(new_node)
                return
            status, new_node = self.ActionMoveDown(node)
            if (status):
                self.visited_nodes.append(new_node)
                self.node_queue.append(new_node)
                moved = True
            if(new_node.node_state_i == self.goal_state).all():
                print("GOAL!")
                self.generate_paths(new_node)
                return
            if (not moved):
                self.node_queue.pop(0) 
            self.algorithm(self.node_queue[0])
            
    def generate_paths(self, node):
        last_node = self.create_node_copy(node)
        if(last_node.parent_node_index_i == None):
            return last_node
        else:
            while(last_node.parent_node_index_i != None):
                self.path_taken.append(last_node)
                for node_i in self.visited_nodes:
                    if(node_i.node_index_i == last_node.parent_node_index_i):
                        last_node = node_i
                        break
            self.path_taken.append(last_node)
    
    def get_path_taken(self):
        return self.path_taken
    
    def get_visited_nodes(self):
        return self.visited_nodes
    
    def get_initial_node(self):
        return self.initial_node
    
    def write_nodes(self, file_path):
        f = open(file_path + "/Nodes.txt", "w")
        for n in self.visited_nodes:
            f.write(str(n.node_state_i.ravel()) + "\n")
            
    def write_path_generated(self, file_path):
        self.path_taken.reverse()
        f = open(file_path + "/NodePath.txt", "w")
        for n in self.path_taken:
            f.write(str(n.node_state_i.ravel())[1: -1] + "\n")