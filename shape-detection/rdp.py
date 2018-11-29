from math import sqrt
from functools import partial
import numpy as np
import sys

def pldist(punto, inicio, final):
    #calcula la distnacia entre los puntos dados
    if np.all(np.equal(inicio, final)):
        return np.linalg.norm(punto - inicio)

    return np.divide(
            np.abs(np.linalg.norm(np.cross(final - inicio, inicio - punto))), np.linalg.norm(final - inicio))

def madDist(M):
    perimetro = 0
    for i in range (1, len(M) -1):
        perimetro = perimetro + np.linalg.norm(M[i-1]-M[i])

    perimetro = perimetro + np.linalg.norm(M[0] - M[len(M)-1])

    return perimetro


def rdp(M, epsilon, dist=pldist): #def rdp(M, inicio, final, epsilon, dist=pldist):
    stk = []
    #madDist(M)
    inicio = 0;
    final = len(M) - 1
    #maximum = madDist(M)
    #print (maximum)
    #stk.append([inicio, maximum])
    stk.append([inicio, final])
    #print (stk)
    global_start_index = inicio
    indices = np.ones(final - inicio + 1, dtype=bool)

    while stk:
        inicio, final = stk.pop()

        dmax = 0.0
        index = inicio

        for i in range(index + 1, final):
            if indices[i - global_start_index]:
                d = dist(M[i], M[inicio], M[final])
                if d > dmax:
                    index = i
                    dmax = d

        if dmax > epsilon:
            stk.append([inicio, index])
            stk.append([index, final])
        else:
            for i in range(inicio + 1, final):
                indices[i - global_start_index] = False

        #print (len(stk))
    if (np.linalg.norm(M[0]-M[len(M) - 1]) < epsilon):
        indices[len(M) - 1] = False
    #print (indices)
    return M[indices]