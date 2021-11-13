# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:46:10 2019

@author: lebre
"""

import random
from random import randint , randrange
from math import sqrt

class POI(object):
    L_scores = []
    def __init__(self,nom,coords,horaires,cout,duree_visite,score):#Initialisation de la classe
        self.nom = nom
        self.coords = coords
        self.horaires = horaires
        self.cout = cout
        self.duree_visite = duree_visite
        self.score = score
        POI.L_scores.append([self.nom,self.coords,self.horaires,self.cout,self.duree_visite,self.score])

    def affiche(self):
        print(self.nom,self.coords,self.horaires,self.cout,self.duree_visite,self.score)


    def tri():
        global P_score
        L_POI_Tries = []
        a = 0
        for j in range(len(P_score)):
            a+=100
            for i in range(len(POI.L_scores)):
                if POI.L_scores[i][5] == a:
                    L_POI_Tries.append(POI.L_scores[i])
        print("Liste triée :", L_POI_Tries)
        return L_POI_Tries

    def Tableau_Distances_TpsTrajet():
       l = POI.L_scores
       distances = []
       for i in range(len(l)):
           for j in range(len(l)):
               a = 0
               D = []
               D.append([l[i][0],l[j][0]])
               a = round(sqrt((float(l[j][1][0])-float(l[i][1][0]))**2+(float(l[j][1][1])-float(l[i][1][1]))**2),2)
               D.append(a)
               D.append(int((a/40)*60))
               distances.append(D)
       return distances



P_cout = [5,10,15,20]
P_score = [100,200,300,400,500]
P_horaires = [[360,840],[480,720],[600,1200],[960,1440],[480,1080],[360,1260]]
P_duree_visite = [30,60,90,120,150,180]

def Generation_Instances():

    global P_cout, P_score, P_horaires, P_duree_visite

    i = 16
    POIs=dict()
    L_POI = []

    for compteur in range(0,i):
        cout = random.choice(P_cout)
        horaires = random.choice(P_horaires)
        duree_visite = random.choice(P_duree_visite)
        score = random.choice(P_score)
        coords = ((randrange(0,101),randrange(0,101)))
        L_POI.append([str(compteur),coords,horaires,cout,duree_visite,score])

    for compteur in range(0,i):
        key = str(compteur)
        value = [compteur,(randrange(0,101),randrange(0,101)), 
                 random.choice(P_horaires),random.choice(P_cout), 
                 random.choice(P_duree_visite), random.choice(P_score)]
        POIs[key] = value

    for keys in POIs:
        keys = POI(POIs[keys][0],POIs[keys][1],POIs[keys][2],POIs[keys][3],POIs[keys][4],POIs[keys][5])
        keys.affiche()


POI0 = [0, (1, 86), [360, 840], 20, 30, 500]
POI1 = [1, (25, 96), [960, 1440], 5, 180, 400]
POI2 = [2, (28, 47), [480, 720], 15, 90, 200]
POI3 = [3, (29, 69), [480, 720], 5, 150, 300]
POI4 = [4, (90, 51), [480, 720], 5, 90, 300]
POI5 = [5, (78, 88), [360, 1260], 5, 90, 400]
POI6 = [6, (44, 44), [360, 840], 10, 90, 200]
POI7 = [7, (83, 14), [600, 1200], 5, 90, 500]
POI8 = [8, (100, 89), [480, 720], 10, 180, 300]
POI9 = [9, (11, 4), [360, 840], 5, 150, 400]
POI10 = [10, (42, 86), [480, 1080], 20, 30, 400]
POI11 = [11, (95, 40), [600, 1200], 20, 60, 500]
POI12 = [12, (84, 47), [360, 840], 20, 150, 400]
POI13 = [13, (32, 2), [600, 1200], 5, 120, 100]
POI14 = [14, (32, 55), [480, 720], 10, 120, 500]
POI15 = [15, (78, 59), [360, 1260], 15, 180, 100]

L_POIs = [POI0, POI1, POI2, POI3, POI4, POI5, POI6, POI7, POI8, POI9, POI10, POI11, POI12, POI13, POI14, POI15]
POIs = dict()

for compteur in range(16):
    key = str(compteur)
    value = [L_POIs[compteur][0], L_POIs[compteur][1], L_POIs[compteur][2], L_POIs[compteur][3], L_POIs[compteur][4], L_POIs[compteur][5]]
    POIs[key] = value
    
for keys in POIs:
    keys = POI(POIs[keys][0],POIs[keys][1],POIs[keys][2],POIs[keys][3],POIs[keys][4],POIs[keys][5])
    keys.affiche()

