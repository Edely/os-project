# -*- coding: utf-8 -*-
import algorithms
from algorithms import Algorithm
from algorithms.main import running_scheduler
from algorithms.main import selects_algorithm

algoritmo = selects_algorithm()
algoritmo.number_of_process = 2
algoritmo.duration_of_process()

#running_scheduler()