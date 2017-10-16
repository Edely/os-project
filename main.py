class Algorithm():
    '''	The algorithm choose to schedule process in a Operating System.	'''
    def __init__(self, number_process=4):
        self.number_of_process = number_process
        self.process = {}
        
        for i in range(number_process):
            self.process[i] = None

        
    def duration_of_process(self, process, duration):
        '''
        Give the duration of each process.
        '''        
        for k,v in self.process.items():
            print('Duration of process: {} is {}'.format(k, v))