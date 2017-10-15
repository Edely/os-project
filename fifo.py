#code to implement the simulation of the First-In First-Out algorithm.
# create class
#funcao para criar processos
#definir tempo dos processos
#rodar a cpu
#dar o tempo de execução
#criar um prompt que pede infos. interativo.


class Fifo():
    '''
    Implementation for simulating the First-In First-Out algorithm for scheduling process in a Operating System.
    '''
    def __init__(self, number_process=4):
        self.name = "First-In First-out"
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