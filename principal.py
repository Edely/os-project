#!/usr/bin/python
class Algorithm():
    '''The algorithm choosed to schedule process in a Operating System.'''
    def __init__(self, number_process=4):
        self.number_of_process = number_process
        self.process = {}
        
        for i in range(number_process):
            self.process[i] = None
            
        print(self.process)
        
    def duration_of_process(self):
        '''
        Gives the duration of each process.
        '''        
        for k,v in self.process.items():
            while type(self.process[k]) is not int:            
                try:
                    self.process[k] = int(input('Insert the duration of the process {}:\n'.format(k)))
                    print('Duration of process: {} is {}'.format(k, v))
                except:
                    print('Duration must be an integer.')
            
            
def main():
    algo = Algorithm()
    algo.duration_of_process()

if __name__ == '__main__':
    main()