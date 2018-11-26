import cv2
from math import sqrt
from functools import partial
from rdp import rdp
import numpy as np
import sys

class ShapeDetector:
        pepe = 0

        def __init__(self):
                pass

        def detect(self, c):
                shape = "unidentified"
                peri = cv2.arcLength(c, True)
                epsilon = peri *0.04
                #print (epsilon)
                #aprox = cv2.approxPolyDP(c, 0.04 * peri, True)
                aprox = rdp(c, 0, len(c)-1, epsilon)

                if len(aprox) == 3:
                        shape = "triangulo"

                elif len(aprox) == 4:
                        (x, y, w, h) = cv2.boundingRect(aprox)
                        ar = w / float(h)
                        shape = "cuadrado" if ar >= 0.95 and ar <= 1.05 else "rectangulo"

              
                elif len(aprox) == 5:
                        shape = "pentagono"

                elif len(aprox) == 6:
                        shape = "hexagono"

                else:
                        shape = "circulo"

                return shape