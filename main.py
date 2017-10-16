class Algorithm():
    '''	The algorithm choose to schedule process in a Operating System.	'''
    def __init__(self, number_process=4):
        self.number_of_process = number_process
        self.process = {}
        
        for i in range(number_process):
            self.process[i] = None

        
    def duration_of_process(self):
        '''
        Gives the duration of each process.
        '''        
        for k,v in self.process.items():
            while type(self.process[k]) is not int:            
                try:
                    self.process[k] = int(input('Insert the duration of the process {}:\n'.format(k)))
                except:
                    print('Duration must be an integer.')
            print('Duration of process: {} is {}'.format(k, v))