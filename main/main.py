import numpy as np
from helper.helper import BFS

if __name__ == "__main__":
    # Define states
    goal_state = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])
    initial_state = np.array([[4, 7, 8], [2, 1, 5], [3, 6, 0]])
    
    # Instantiate BFS class
    bfs = BFS()
    
    # Call Member functions
    bfs.algorithm()
    bfs.write_nodes("./test_case")
    bfs.write_path_generated("./test_case")
    