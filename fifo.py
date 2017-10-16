from main import Algorithm
#code to implement the simulation of the First-In First-Out algorithm.
# create class
#funcao para criar processos
#definir tempo dos processos
#rodar a cpu
#dar o tempo de execução
#criar um prompt que pede infos. interativo.

class Fifo(Algorithm):
    ''' Implementation for simulating the First-In First-Out algorithm for scheduling process in a Operating System. '''
    def __init__(self, number_process=4):
        self.name = 'First-In First-Out'
        
        super(Fifo, self).__init__()