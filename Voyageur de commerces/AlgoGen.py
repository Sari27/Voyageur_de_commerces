# Créé par Sarah, le 12/04/2019 en Python 3.2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:48:12 2019

@author: lebre
"""

from POI import*
from Donnees import nb_jours_U, nb_km_U, Budjet_max_U, H_depart_U, H_arrivee_U
from Solutions import*
from random import*
import time

temps_depart = time.time()
generation = 0
Generations = []     # cette matrice contiendra toutes les générations de population
Meilleures_Solutions = []   # cette matrice contiendra les meilleures solutions de toutes les générations
Scores_Meilleures_Solutions = []
Meilleure_Solution = []
Scores_moins_bonnes_solutions = []
Moins_bonne_solution = []

def Journee_a_inserer(L_POI_Enfant, num_Parent):     # fonction servant dans l'étape "croisement"
    global L_Parents, iteration_journee
    A_supprimer = []
    A_inserer = []
    for B in range(len(L_Parents[num_Parent][iteration_journee])):
        if L_Parents[num_Parent][iteration_journee][B][0] in L_POI_Enfant:
            A_supprimer.append(L_Parents[num_Parent][iteration_journee][B])
    for A2 in L_Parents[num_Parent][iteration_journee]:
        if A2 not in A_supprimer:
                A_inserer.append(A2)
    return A_inserer

def Calcul_Score_Solution(Solution):       # fonction servant dans la mise à jour de la population
    score = 0
    for A in Solution:
        for A2 in A:
            score+=A2[5]
    return score

population_initiale = Solutions_Aleatoires(50)
population = population_initiale
print("population initiale:", population)
Generations.append(population)
for G in population :
        if Calcul_Score_Solution(Meilleure_Solution)<Calcul_Score_Solution(G):
            Meilleure_Solution = G
Meilleures_Solutions.append(Meilleure_Solution)
Scores_Meilleures_Solutions.append(Calcul_Score_Solution(Meilleure_Solution))

Moins_bonne_solution = population[0]
for G2 in population :
        if Calcul_Score_Solution(Moins_bonne_solution)>Calcul_Score_Solution(G2):
            Moins_bonne_solution = G2
Scores_moins_bonnes_solutions.append(Calcul_Score_Solution(Moins_bonne_solution))

while generation < 20:

    generation+=1

    L_Individus_a_trier = []
    L_Meilleurs_Individus = []

    '''SELECTION PARENTS'''

    for j in range(int(len(population)/2)):
        L_Parents = []
        L_Enfants = [[[] for p in range(nb_jours_U)],[[] for q in range(nb_jours_U)]]
        for k in range(4):
            i = randint(0, (len(population)-1))
            parent = population[i]
            L_Parents.append(parent)


        if Calcul_Score_Solution(L_Parents[0])>Calcul_Score_Solution(L_Parents[1]):
            del L_Parents[1]
        else:
            del L_Parents[0]
        if Calcul_Score_Solution(L_Parents[1])>Calcul_Score_Solution(L_Parents[2]):
            del L_Parents[2]
        else:
            del L_Parents[1]

        print("L_Parents =", L_Parents)



        '''CROISEMENT'''

        L_iteration_journee = []

        for A in range(len(L_Parents[0])):

            POI_Enfant0 = []
            POI_Enfant1 = []

            for A3 in L_Enfants[0]:                                                                                          # création d'une liste pour chaque enfant où on stocke les nums des POIs déjà présents
                for A4 in A3:
                    for A5 in A4:
                        POI_Enfant0.append(A5[0])

            for A6 in L_Enfants[1]:
                for A7 in A6:
                    for A8 in A7:
                        POI_Enfant1.append(A8[0])

            iteration_journee = randint(0, len(L_Parents[0])-1)                                                             # on tire une journée au hasard
            while iteration_journee in L_iteration_journee:
                iteration_journee = randint(0, len(L_Parents[0])-1)                                                         #si la journée a déjà été recopiée, on tire une autre journée
            hasard = randint(0, 1)

            L_iteration_journee.append(iteration_journee)


            if hasard%2==0:                                                                                         # part de hasard : P1 -> E1 ; P2 -> E2

                L_Enfants[0][iteration_journee].append(Journee_a_inserer(POI_Enfant0, 0))

                L_Enfants[1][iteration_journee].append(Journee_a_inserer(POI_Enfant1, 1))

            else:                                                                                                            # hasard : P1 -> E2 ; P2 -> E1

                L_Enfants[0][iteration_journee].append(Journee_a_inserer(POI_Enfant0, 1))

                L_Enfants[1][iteration_journee].append(Journee_a_inserer(POI_Enfant1, 0))


        L_Enfants2 = [[],[]]                                                                                                     # réadaptation de la taille de la liste au niveau de celle de parents (pr pb nb matrices)
        for B in L_Enfants[0]:
            for B2 in B:
                L_Enfants2[0].append(B2)
        for B3 in L_Enfants[1]:
            for B4 in B3:
                L_Enfants2[1].append(B4)

        print("L_Enfants =", L_Enfants2)


        '''MUTATION'''

        for M in range(len(L_Enfants2)):                                                                                # possibilité de muter pour chaque enfant
            mutation = randint(0,10)                                                                                                 # proba de muter : 10%

            if mutation == 2:
                journee_a_reconstruire = randint(0, len(L_Enfants2[M])-1)
                del L_Enfants2[M][journee_a_reconstruire]                                                                       # on efface la journée selectionnée
                nouvelle_journee = Solutions_Aleatoires(1)[0][journee_a_reconstruire]                                                            # on crée une nouvelle solution, et on sélectionne la bonne itération de journée


                for M2 in L_Enfants2[M]:
                    for M3 in M2:
                        if M3 in nouvelle_journee :                                                                                 # si POI communs on les efface de la journée à ajouter
                            nouvelle_journee.remove(M3)

                L_Enfants2[M].append(nouvelle_journee)                                                                                           # la nouvelle journée est rajoutée à la suite des autres journées (l'ordre n'a pas d'importance)
                print("L_Enfant avec nouvelle journée =", L_Enfants2)



        '''MISE A JOUR DE LA POPULATION'''

        # Ici on choisit de prendre les 50% meilleurs parmi les enfants et les parents réunis

        for C in range(len(L_Enfants2)):                                                            # on commence par réunir tous les enfants de la génération
            L_Individus_a_trier.append(L_Enfants2[C])                                                                                    # dans une liste d'individus à trier

        for C2 in range(len(L_Parents)):                                                                                                                 # boucle for utilisée par souci de matrice(des matrices dans des matrices... trop nombreuses)
            L_Individus_a_trier.append(L_Parents[C2])                                                       # on y ajoute tous les parents de la génération

    L_Scores_Individus_a_trier = []
    z = 0
    
    for E in range(len(L_Individus_a_trier)):
        L_Scores_Individus_a_trier.append(Calcul_Score_Solution(L_Individus_a_trier[E]))
    
    for D in range(int(len(L_Individus_a_trier)/2)):                                                         # on cherche les 50% meilleurs
        for D1 in L_Individus_a_trier:
            D2 = max(L_Scores_Individus_a_trier)
            if Calcul_Score_Solution(D1) == D2:
                L_Meilleurs_Individus.append(D1)
                L_Individus_a_trier.remove(D1)
                L_Scores_Individus_a_trier.remove(D2)
                break

    print("meilleurs individus =", L_Meilleurs_Individus)
    print("len meilleurs individus =", len(L_Meilleurs_Individus))


    print("Meilleure Solution (génération précédente)", Meilleure_Solution)
    population = L_Meilleurs_Individus
    for F in population :
        if Calcul_Score_Solution(Meilleure_Solution)<Calcul_Score_Solution(F):
            Meilleure_Solution = F
            
    Moins_bonne_solution = population[0]        
    for F2 in population :
        if Calcul_Score_Solution(Moins_bonne_solution)>Calcul_Score_Solution(F2):
            Moins_bonne_solution = F2
    Scores_moins_bonnes_solutions.append(Calcul_Score_Solution(Moins_bonne_solution))
    
    Meilleures_Solutions.append(Meilleure_Solution)
    Generations.append(population)
    Scores_Meilleures_Solutions.append(Calcul_Score_Solution(Meilleure_Solution))
    print("Meilleure Solution =", Meilleure_Solution)
    print("Score Meilleure solution :", Calcul_Score_Solution(Meilleure_Solution))

temps_arrivee = time.time()
temps_resolution = int(temps_arrivee - temps_depart)
print("Generations :", Generations)
print("len Generations :", len(Generations))
print("Meilleures_Solutions", Meilleures_Solutions)
print("len Meilleures_Solutions :", len(Meilleures_Solutions))
print("Scores_Meilleures_Solutions :", Scores_Meilleures_Solutions)
print("Temps de résolution :", temps_resolution)

