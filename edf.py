from algorithm import Algorithm

class EDF(Algorithm):
    '''Implementation for simulating the First-In First-Out algorithm for scheduling process in a Operating System.'''
    def __init__(self, number_process=4):
        self.name = 'First-In First-Out'
        
        super(EDF, self).__init__()
        
  