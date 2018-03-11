from .algorithm import Algorithm

class ROUNDROBIN(Algorithm):
    '''Implementation for simulating the Round Robin algorithm for scheduling process in a Operating System.'''
    def __init__(self, number_process=4):
        self.name = 'Round Robin'
        
        super(ROUNDROBIN, self).__init__()
        
    