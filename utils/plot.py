import numpy as np

class Plot:
    def __init__(self):
        self.data = None
        return
    
    def print_matrix(self, state):
        counter = 0
        for row in range(0, len(state), 3):
            if counter == 0 :
                print("-------------")
            for element in range(counter, len(state), 3):
                if element <= counter:
                    print("|", end=" ")
                print(int(state[element]), "|", end=" ")
            counter = counter +1
            print("\n-------------")
            
    def load_data(self, file_path):
        self.data = np.loadtxt(file_path)
        
    def plot_nodes(self):
        if(len(self.data[1]) != 9):
            raise Exception("Text file format is incorrect. Re-run main.")
        else:
            for i in range(0, len(self.data)):
                if (i == 0):
                    print(" .. START NODE .. \n")
                elif (i == len(self.data) - 1):
                    print(" .. GOAL NODE .. \n")
                else:
                    print(" .. STEP ..", i)
                self.print_matrix(self.data[i])
            return