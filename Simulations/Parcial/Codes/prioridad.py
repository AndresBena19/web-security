#!/usr/bin/python

import numpy as np

def prioridad(Priority,Arrival_t,Service_t):
    #ordenamos los datos de menor a mayor
    for i in range(0, len(Priority)):
        for j in range (0, len(Priority)):
            if (Priority[i]<Priority[j]):
                aux = Priority[i]
                Priority[i] = Priority[j]
                Priority[j] = aux
                #Change in the same way the service time
                aux = Service_t[i]
                Service_t[i] = Service_t[j]
                Service_t[j] = aux
                #Change in the same way the arrival time
                aux = Arrival_t[i]
                Arrival_t[i]=Arrival_t[j]
                Arrival_t[j]=aux
    #Retornando datos
    return Priority,Arrival_t,Service_t



if __name__ == "__main__":
  Tie = [49, 66, 87, 33, 60, 67, 64, 52, 47, 44, 87, 63, 68, 80, 8, 30, 14, 71, 33, 46, 110, 31, 34, 51, 19, 77, 51, 54, 93, 37, 76, 76, 87, 46, 52, 51, 71, 47, 57, 58, 48, 37, 35, 46, 16, 54, 50, 54, 56, 32]

  Tiew = [3, 5, 5, 1, 4, 1, 5, 5, 6, 1, 3, 6, 1, 3, 5, 2, 4, 4, 1, 5, 4, 1, 3, 3, 5, 5, 3, 1, 3, 3, 4, 2, 3, 5, 6, 1, 5, 2, 2, 2, 2, 6, 4, 2, 4, 3, 5, 3, 2, 4]

  Pri = [5, 1, 1, 3, 2, 0, 2, 0, 1, 4, 0, 3, 1, 4, 0, 3, 5, 3, 0, 0, 4, 0, 3, 1, 5, 2, 4, 2, 2, 3, 1, 0, 3, 5, 3, 3, 2, 5, 5, 4, 1, 0, 4, 2, 5, 4, 0, 2, 3, 4]

  a,b,c=prioridad(Pri,Tie,Tiew)
 
  print a
  print b
  print c
