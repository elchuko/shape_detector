import cv2
from math import sqrt
from functools import partial
from rdp import rdp
from rdp import madDist
import numpy as np
import sys

class ShapeDetector:
        pepe = 0

        def __init__(self):
                pass

        def detect(self, c):
                #print ("entra?")
                shape = "unidentified"
                #peri = cv2.arcLength(c, True)
                #print (peri)
                peri = madDist(c)
                #print (peri)
                epsilon = peri *0.03
                #print (epsilon)
                #aprox = cv2.approxPolyDP(c, 0.04 * peri, True)
                #print (c)
                aprox = rdp(c, epsilon)
                #print(aprox)
                #aprox = rdp(aprox, 0, len(aprox) - 1, epsilon)
                #generar otra funcion que descarte lados muy pequeños

                if len(aprox) == 3:
                        shape = "triangulo"

                elif len(aprox) == 4:
                        (x, y, w, h) = cv2.boundingRect(aprox)
                        ar = w / float(h)
                        shape = "cuadrado" if ar >= 0.95 and ar <= 1.05 else "rectangulo"
                        #print (aprox)

              
                elif len(aprox) == 5:
                        shape = "pentagono"

                elif len(aprox) == 6:
                        shape = "hexagono"

                elif len(aprox) == 7:
                        shape = "heptagono"

                else:
                        shape = "circulo"
                        #print (aprox)

                return shape