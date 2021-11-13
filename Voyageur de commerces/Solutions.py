# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:47:32 2019

@author: lebre
"""

import random
from random import randint , randrange
from Donnees import nb_jours_U, nb_km_U, Budjet_max_U, H_depart_U, H_arrivee_U
from POI import*


class Jour(object):
    def __init__(self,seq_POI,nb_km,cout_jour):
        self.seq_POI = seq_POI
        self.nb_km = nb_km
        self.cout_jour = cout_jour

    def affiche(self):
        print("Séquence de POI :", self.seq_POI)
        print("Nombre de km :", self.nb_km)
        print("Coût total :", self.cout_jour)

    def Calcul_Distance_Totale(self):
        l = POI.Tableau_Distances_TpsTrajet()
        print(l)
        dist_totale = 0
        for i in range(len(self.seq_POI)-1):
            for j in range(len(l)):
                if l[j][0][0]==self.seq_POI[i] and l[j][0][1]==self.seq_POI[i+1]:
                    dist_totale+=int(l[j][1])
        print("Distance totale =", dist_totale)
        return dist_totale







class Solution(Jour):
    L_Solution = []
    def __init__(self,seq_POI,nb_km,cout_jour,nb_jours):
        Jour.__init__(self,seq_POI,nb_km,cout_jour)
        self.nb_jours = nb_jours
        Solution.L_Solution.append([self.seq_POI,self.nb_km,self.cout_jour])

    def affiche(self):
        print("Nombre de jours :",self.nb_jours)
        Jour.affiche(self)
        print("Liste solution :",Solution.L_Solution)


    def Fenetre_Temps(self):
        global H_depart_U, H_arrivee_U
        Indic_Erreur = 0
        l = POI.Tableau_Distances_TpsTrajet()
        print("Tableau Distances Tps Trajet :",l)
        heure = H_depart_U
        Heure_Ouverture = 0
        Heure_fermeture = 0
        Heure_Ouverture_Dernier_POI = 0
        Heure_Fermeture_Dernier_POI = 0
        for i in range(len(l)):
            if l[i][0][0]== 0 and l[i][0][1] == Solution.L_Solution[0][0][0]:
                heure+=l[i][2]
                print("heure après premier tps de trajet :", heure)

        for j in range(len(Solution.L_Solution[0][0])-1):
            if len(Solution.L_Solution[0][0]) != 1:
                Indice_fermeture = Solution.L_Solution[0][0][j:j+1]
                Indice_ouverture = Solution.L_Solution[0][0][j:j+1]
                Indice_ouverture = Indice_ouverture[0]
                Indice_fermeture = Indice_fermeture[0]
                for k in range(1,len(POI.L_scores)):
                        if POI.L_scores[k][0] == Indice_ouverture:
                            Heure_Ouverture = POI.L_scores[k][2][0]
                            print("heure ouverture :", Heure_Ouverture)
                            if heure < Heure_Ouverture:
                                heure = Heure_Ouverture
                                print("heure si attente ouverture :", heure)
                            if POI.L_scores[k][0] == Indice_fermeture:
                                Heure_fermeture = POI.L_scores[k][2][1]
                                print("Heure fermeture:",Heure_fermeture)
                            if heure > Heure_fermeture:
                                Indic_Erreur += 1
                                print("pb1")
                                print('Indic_Erreur =', Indic_Erreur)
                            if POI.L_scores[k][0] == Indice_ouverture and heure<Heure_fermeture:
                                print("Heure avant visite:",heure)
                                heure+=POI.L_scores[k][4]
                                print("Durée visite:",POI.L_scores[k][4])
                                print("Heure après visite : ",heure)
                for m in range(len(l)):
                    if l[m][0][0] == Solution.L_Solution[0][0][j] and l[m][0][1] == Solution.L_Solution[0][0][j+1]:
                        heure+=l[m][2]
                        print("Heure après temps de trajet:",heure)
        Indice_dernier_POI = Solution.L_Solution[0][0][len(Solution.L_Solution[0][0])-1]
        for q in range(1,len(POI.L_scores)):
            if POI.L_scores[q][0] == Indice_dernier_POI:
                Heure_Ouverture_Dernier_POI = POI.L_scores[q][2][0]
                print("Heure ouverture dernier POI:",Heure_Ouverture_Dernier_POI)
                Heure_Fermeture_Dernier_POI = POI.L_scores[q][2][1]
                print("Heure fermeture dernier POI:",Heure_Fermeture_Dernier_POI)
                if heure < Heure_Ouverture_Dernier_POI:
                    heure = Heure_Ouverture_Dernier_POI
                if heure > Heure_Fermeture_Dernier_POI:
                    Indic_Erreur += 1
                    print("pb2")
                    print('Indic_Erreur =',Indic_Erreur)
                if POI.L_scores[q][0] == Indice_ouverture and heure<Heure_fermeture:
                    print("Heure avant visite dernier POI:",heure)
                    heure += POI.L_scores[q][4]
                    print("Durée visite dernier POI:",POI.L_scores[q][4])
                    print("Heure après visite dernier POI: ",heure)
        for p in range(len(l)):
            if l[p][0][0]== Solution.L_Solution[0][0][(len(Solution.L_Solution[0][0])-1)] and l[p][0][1] == 0:
                heure+=l[p][2]

        return Indic_Erreur




    def Verif_Solution(self):
        global nb_jours_U, nb_km_U, Budjet_max_U, H_depart_U, H_arrivee_U
        Indic_Erreur = Solution.Fenetre_Temps(self)
        if self.nb_jours > nb_jours_U:
            Indic_Erreur+=1
        if self.nb_km > nb_km_U:
            Indic_Erreur+=1
        if self.cout_jour > Budjet_max_U:
            Indic_Erreur+=1
        print("Indication erreur:",Indic_Erreur)
        if Indic_Erreur != 0:
            print("La solution n'est pas bonne.")
        else:
            print("La solution est bonne.")



def Generation_Jours():
    Jours = dict()

    seq_POI = [1,2,3,4]
    nb_km = 200
    cout_jour = 60

    key = str(seq_POI)
    value = [seq_POI,nb_km,cout_jour]
    Jours[key] = value
    print(Jours)

    for keys in Jours:
        keys = Jour(Jours[keys][0],Jours[keys][1],Jours[keys][2])
        keys.affiche()
        keys.Calcul_Distance_Totale()

def Generation_Solution():
    Jours = dict()

    seq_POI = [1,2,3,4]
    nb_km = 200
    cout_jour = 60
    nb_jours = 3

    for compteur in range(1,nb_jours+1):
        key = str(compteur)
        value = [seq_POI,nb_km,cout_jour,nb_jours]
        Jours[key] = value
    print(Jours)

    for keys in Jours:
        keys = Solution(Jours[keys][0],Jours[keys][1],Jours[keys][2],Jours[keys][3])
        keys.affiche()
        keys.Fenetre_Temps()
        keys.Verif_Solution()
        keys.Calcul_Distance_Totale()


def Solutions_Aleatoires(nb_Solutions):

    global nb_jours_U, H_depart_U, Budjet_max_U, nb_km_U, H_arrivee_U
    Solutions = []

    if nb_Solutions > 2:
        nb_Solutions = int(nb_Solutions/2)*2            # au cas où le nombre choisi n'est pas divisible par 2

    for A in range(nb_Solutions):
        Liste_POI = []
        Solution = []
        Distances_parcourues = []
        a = 0
        heure = 0
        coût = 0
        nb_km = 0
        km_premier_dernier_poi = 0
        tps_trajet_premier_dernier_poi = 0

        for j in range(nb_jours_U):
            Solution.append([])
            Distances_parcourues.append([])

        for compteur in range(1,len(POI.L_scores)):
            if POI.L_scores[compteur][0]!=0:
                Liste_POI.append(POI.L_scores[compteur])
        random.shuffle(Liste_POI)

        while Liste_POI != []:
            POI_a_inserer = Liste_POI[0]
            del Liste_POI[0]

            for i in range(len(Solution)):
                a = 0
                nb_km = 0
                heure = H_depart_U

                if Solution[i]!=[]:        # cas où il y a déjà des POI dans la journée
                    coût = 0                # coût trop élevé
                    for o in range(len(Solution[i])):   # on calcule le coût de tous les poi de la journée
                        coût+=Solution[i][o][3]
                    coût+=POI_a_inserer[3]              # on y rajoute le coût du poi à insérer
                    if coût>Budjet_max_U:
                        a+=1

                                                            # nb km trop élevé
                    for r in range(len(POI.Tableau_Distances_TpsTrajet())): # calcul nb km entre pt départ et premier POI
                        if POI.Tableau_Distances_TpsTrajet()[r][0][0]==0 and POI.Tableau_Distances_TpsTrajet()[r][0][1]==POI_a_inserer[0]:
                            nb_km+=POI.Tableau_Distances_TpsTrajet()[r][1]
                            km_premier_dernier_poi = POI.Tableau_Distances_TpsTrajet()[r][1]
                    if len(Solution[i])>1:      # si il y a plus d'un poi dans la journée; calcul pour les poi après le premier (sans compter le poi à insérer)
                        for p in range(1,len(Solution[i])-1):
                            for q in range(len(POI.Tableau_Distances_TpsTrajet())):
                                if POI.Tableau_Distances_TpsTrajet()[q][0][0]==Solution[i][p][0] and POI.Tableau_Distances_TpsTrajet()[q][0][1]==Solution[i][p+1][0]:
                                    nb_km+=POI.Tableau_Distances_TpsTrajet()[q][1]
                    for s in range(len(POI.Tableau_Distances_TpsTrajet())): # calcul entre dernier poi et poi à insérer
                        if POI.Tableau_Distances_TpsTrajet()[s][0][0]==Solution[i][len(Solution[i])-1][0] and POI.Tableau_Distances_TpsTrajet()[s][0][1]==POI_a_inserer[0]:
                            nb_km+=POI.Tableau_Distances_TpsTrajet()[s][1]
                    nb_km+=km_premier_dernier_poi
                    if nb_km>nb_km_U:
                        a+=1

                             #teste si la visite est possible
                    for t in range(len(POI.Tableau_Distances_TpsTrajet())): # calcul tps entre pt départ et 1er poi
                        if POI.Tableau_Distances_TpsTrajet()[t][0][0]==0 and POI.Tableau_Distances_TpsTrajet()[t][0][1]==Solution[i][0][0]:
                            heure+=POI.Tableau_Distances_TpsTrajet()[t][2]  #tps trajet
                            tps_trajet_premier_dernier_poi = POI.Tableau_Distances_TpsTrajet()[t][2]
                            if heure<Solution[i][0][2][0]:
                                heure = Solution[i][0][2][0]
                            if heure>Solution[i][0][2][1]:
                                a+=1
                            heure+=Solution[i][0][4]       #tps visite
                    if len(Solution[i])>1:      # calculs entre 1er poi et les autres
                        for u in range(1,len(Solution[i])-1):
                            for v in range(len(POI.Tableau_Distances_TpsTrajet())):
                                if POI.Tableau_Distances_TpsTrajet()[v][0][0]==Solution[i][u][0] and POI.Tableau_Distances_TpsTrajet()[v][0][1]==Solution[i][u+1][0]:
                                    nb_km+=POI.Tableau_Distances_TpsTrajet()[v][2]  #tps_trajet
                                    if heure<Solution[i][u+1][2][0]:
                                        heure = Solution[i][u+1][2][0]
                                    if heure>Solution[i][u+1][2][1]:
                                        a+=1
                                    heure+=Solution[i][u+1][4]                      #tps visite
                    for w in range(len(POI.Tableau_Distances_TpsTrajet())): # calcul entre dernier poi et poi à insérer
                        if POI.Tableau_Distances_TpsTrajet()[w][0][0]==Solution[i][len(Solution[i])-1][0] and POI.Tableau_Distances_TpsTrajet()[w][0][1]==POI_a_inserer[0]:
                            heure+=POI.Tableau_Distances_TpsTrajet()[w][2]          #tps trajet
                            if heure<Solution[i][len(Solution[i])-1][2][0]:
                                heure = Solution[i][len(Solution[i])-1][2][0]
                            if heure>Solution[i][len(Solution[i])-1][2][1]:
                                a+=1
                    heure+=POI_a_inserer[4]                                         #tps visite poi à insérer
                    heure+=tps_trajet_premier_dernier_poi                           #tps trajet
                    if heure>H_arrivee_U:
                        a+=1


                elif Solution[i]==[]:         # cas où une journée de solution est vide -> OK
                    if POI_a_inserer[3]>Budjet_max_U :  # coût trop élevé
                        a+=1

                    for n in range(len(POI.Tableau_Distances_TpsTrajet())): # si le nb de km entre pt départ et premier POI trop élevé
                        if POI.Tableau_Distances_TpsTrajet()[n][0][0]==0 and POI.Tableau_Distances_TpsTrajet()[n][0][1]==POI_a_inserer[0] and POI.Tableau_Distances_TpsTrajet()[n][1]> nb_km_U:
                            a+=1

                       # teste si la visite est possible
                    for l in range(len(POI.Tableau_Distances_TpsTrajet())):
                        if POI.Tableau_Distances_TpsTrajet()[l][0][0]==0 and POI.Tableau_Distances_TpsTrajet()[l][0][1]==POI_a_inserer[0]:
                            heure+=POI.Tableau_Distances_TpsTrajet()[l][2]
                    if heure<POI_a_inserer[2][0]:
                        heure=POI_a_inserer[2][0]
                    if heure>POI_a_inserer[2][1]:
                        a+=1

                    for m in range(len(POI.Tableau_Distances_TpsTrajet())):
                        if POI.Tableau_Distances_TpsTrajet()[m][0][0]==0 and POI.Tableau_Distances_TpsTrajet()[m][0][1]==POI_a_inserer[0]:
                            if heure + POI_a_inserer[4] + POI.Tableau_Distances_TpsTrajet()[m][2]>H_arrivee_U:
                                a+=1

                if a == 0:
                    Solution[i].append(POI_a_inserer)
                    break
        Solutions.append(Solution)

    return Solutions

print(Solutions_Aleatoires(4))


