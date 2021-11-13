# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:44:26 2019

@author: lebre
"""

from POI import*
from Donnees import*
from AlgoGen import*
from Solutions import*

f=open('Analyses.csv', 'w')
f.write('Analyses de l algorithme génétique\n\n')

f.write('Nombre de générations :'+';'+str(len(Generations))+'\n')   # DONNEES SUR LE TEST
f.write('Nombre de solutions par génération :'+';'+str(len(Generations[0]))+'\n')
f.write('Temps de résolution :'+';'+str(temps_resolution)+'\n'+'\n')

f.write('Données utilisateur :'+'\n')       # DONNEES UTILISATEUR
f.write('Nombre de jours de visite :'+';'+str(nb_jours_U)+'\n')
f.write('Nombre de kilomètres max par jour :'+';'+str(nb_km_U)+'\n')
f.write('Budget max par jour :'+';'+str(Budjet_max_U)+'\n')
f.write('Heure de départ :'+';'+str(H_depart_U)+'\n')
f.write('Heure d arrivée :'+';'+str(H_arrivee_U)+'\n')
f.write('\n')

f.write('Moyennes des scores des solutions des générations :'+'\n') # MOYENNES SCORES
f.write('Générations :'+';')
for i in range (len(Generations)):
    num_generation = str(i)+';'
    f.write(num_generation)
f.write('\n')
f.write('Moyennes scores :'+';')
for i2 in range (len(Generations)): #population
    moyenne_score_generation = 0
    for i3 in range(len(Generations[i2])):  #solution
        moyenne_score_generation+=Calcul_Score_Solution(Generations[i2][i3])
    moyenne_score_generation = round(moyenne_score_generation/len(Generations[i2]))
    f.write(str(moyenne_score_generation)+';')
f.write('\n'+'\n')

f.write('Scores des meilleures solutions :'+'\n')   # MEILLEURES SOLUTIONS
f.write('Générations :'+';')
for j in range (len(Generations)):
    num_generation = str(j)+';'
    f.write(num_generation)
f.write('\n')
f.write('Meilleurs scores :'+';')
meilleurs_scores = str(Scores_Meilleures_Solutions).replace(',',';').strip('[]')+'\n'
f.write(meilleurs_scores)
f.write('\n')

f.write('Scores des moins bonnes solutions :'+'\n')   # MOINS BONNES SOLUTIONS
f.write('Générations :'+';')
for k in range (len(Generations)):
    num_generation = str(k)+';'
    f.write(num_generation)
f.write('\n')
f.write('Moins bons scores :'+';')
moins_bons_scores = str(Scores_moins_bonnes_solutions).replace(',',';').strip('[]')+'\n'
f.write(moins_bons_scores+'\n'+'\n')

f.write('Scores des solutions :')             # TOUTES SOLUTIONS
for l in range ((len(Generations))):
    f.write('\n'+'Génération'+str(l)+';')
    for L in Generations[l]:
        f.write(str(Calcul_Score_Solution(L))+';')

f.write('\n'+'\n')
f.write("Meilleure solution :"+str(Meilleures_Solutions[1:])+';')

f.close()
