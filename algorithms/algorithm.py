class Algorithm(object):
    '''The algorithm choosed to schedule process in a Operating System.'''
    def __init__(self, number_process=4):
        self.number_process = number_process
        self.process = {}
        
    def number_of_process(self):
        '''
        It changes the default number of process.
        '''
        number = None
        while type(number) is not int:
            try:
                number = int(input("How many process the scheduler will have?\n"))
            except(KeyboardInterrupt):
                quit()
            except:
                print('Duration must be an integer.')

        self.number_of_process = number


    def duration_of_process(self):
        '''
        Gives the duration of each process.
        '''        

        for i in range(self.number_of_process):
            self.process[i+1] = None 

        for k,v in self.process.items():
            while type(self.process[k]) is not int:            
                try:
                    self.process[k] = int(input('Insert the duration of the process {}:\n'.format(k)))  
                except(KeyboardInterrupt):
                    quit()
                except:
                    print('Duration must be an integer.')
        for k, v in self.process.items():
            print("Processo {} - Duration: {}".format(k, self.process[k]))    

    def scheduler(self):
        '''
        It schedules the process.
        '''
        print("=====")