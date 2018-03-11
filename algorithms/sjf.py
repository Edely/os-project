from .algorithm import Algorithm

class SJF(Algorithm):
    '''Implementation for simulating the Shortest Job First algorithm for scheduling process in a Operating System.'''
    def __init__(self, number_process=4):
        self.name = 'Shortest Job First'
        
        super(SJF, self).__init__()
        
    