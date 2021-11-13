# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:46:53 2019

@author: lebre
"""

import random
from random import randint , randrange

class Donnees(object):
    def __init__(self,nb_jours_U,nb_km_U,Budjet_max_U,H_depart_U,H_arrivee_U):
        self.nb_jours_U = nb_jours_U
        self.nb_km_U = nb_km_U
        self.Budjet_max_U = Budjet_max_U
        self.H_depart_U = H_depart_U
        self.H_arrivee_U = H_arrivee_U

    def affiche(self):
        print("Nombre de jours (données) :",self.nb_jours_U)
        print("Nombre de km (données) :",self.nb_km_U)
        print("Budjet (données) :",self.Budjet_max_U)
        print("Heure de départ (données) :",self.H_depart_U)
        print("Heure d'arrivée (données) :",self.H_arrivee_U)



nb_jours_U = 4          #randint(1,10)
nb_km_U = 250           #randint(250,500)
H_depart_U = 450        #randint(480,600)
H_arrivee_U = 1260      #randint(960,1140)
Budjet_max_U = 100      #randint(70,150)

donnees = Donnees(nb_jours_U,nb_km_U,Budjet_max_U,H_depart_U,H_arrivee_U)
donnees.affiche()



