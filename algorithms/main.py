import time
from .algorithm import Algorithm
from .fifo import FIFO
from .edf import EDF
from .sjf import SJF
from .roundrobin import ROUNDROBIN

def selects_algorithm():
    '''
    It selects the algorithm used by the programm and initialize.
    '''
    
    algorithms = {
        "0":"FIRST-IN, FIRST-OUT",
        "1":"SHORTEST JOB FIRST",
        "2":"EARLIEST DEADLINE FIRST",
        "3":"ROUND ROBIN"
    }
    
    option_algorithm = None
    
    for k, v in algorithms.items():
        print("{}: {}".format(k, algorithms[k]))           
            
    while type(option_algorithm) is not int or option_algorithm < 0 or option_algorithm > 3:
                
        try:
            option_algorithm = int(input('\nChoose the algorithm:\n')) 
        except(KeyboardInterrupt):
            quit()
        except:
            print("Invalid Option.\n")
            for k, v in algorithms.items():
                print("{}: {}".format(k, algorithms[k]))            
        
        
    if option_algorithm == 0:
        algo = FIFO()
    if option_algorithm == 1:
        algo = SJF()
    if option_algorithm == 2:
        algo = EDF()
    if option_algorithm == 3:
        algo = ROUNDROBIN()

    return(algo)    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
     