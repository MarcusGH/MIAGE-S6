import random
import time

print("Exercice 1")

print("\n")

nbAlea = []
i = 0

while i < 100:
	nbAlea.append(round(random.uniform(0,10),2))
	i += 1

print ("Liste des nombres :\n")
i = 0

while i < 100:
	print('{0:10} {1:10} {2:10} {3:10} {4:10}'.format(nbAlea[i],nbAlea[i+1],nbAlea[i+2],nbAlea[i+3],nbAlea[i+4]))
	i += 5

def effectifInter(a,b,tab):
	compteur = 0
	for value in tab:
		if value >= a and value < b:
			compteur += 1
	return compteur

def effectifFreq(a,b,tab):
	compteur = 0
	for value in tab:
		if value >= a and value < b:
			compteur += 1
	return compteur/len(tab)

def effectifDens(a,b,tab):
	compteur = 0
	for value in tab:
		if value >= a and value < b:
			compteur += 1
	return compteur/(b-a)

print("\n")

print ("Effectif sur l'intervalle [0;1[ :", effectifInter(0,1,nbAlea))
print ("Effectif sur l'intervalle [1;3[ :", effectifInter(1,3,nbAlea))
print ("Effectif sur l'intervalle [3;7[ :", effectifInter(3,7,nbAlea))
print ("Effectif sur l'intervalle [7;9[ :", effectifInter(7,9,nbAlea))
print ("Effectif sur l'intervalle [9;10[ :", effectifInter(9,10,nbAlea))

print("\n")

print ("Fréquence sur l'intervalle [0;1[ :", effectifFreq(0,1,nbAlea))
print ("Fréquence sur l'intervalle [1;3[ :", effectifFreq(1,3,nbAlea))
print ("Fréquence sur l'intervalle [3;7[ :", effectifFreq(3,7,nbAlea))
print ("Fréquence sur l'intervalle [7;9[ :", effectifFreq(7,9,nbAlea))
print ("Fréquence sur l'intervalle [9;10[ :", effectifFreq(9,10,nbAlea))

print("\n")

print ("Densité sur l'intervalle [0;1[ :", effectifDens(0,1,nbAlea))
print ("Densité sur l'intervalle [1;3[ :", effectifDens(1,3,nbAlea))
print ("Densité sur l'intervalle [3;7[ :", effectifDens(3,7,nbAlea))
print ("Densité sur l'intervalle [7;9[ :", effectifDens(7,9,nbAlea))
print ("Densité sur l'intervalle [9;10[ :", effectifDens(9,10,nbAlea))

print("\n")

print("Exercice 2")

lettre = ["A","B","C","D"]
mot = []
i = 0

while i<7:
	mot.append(random.choice(lettre))
	i += 1

print(mot)
print(mot[0])


def verifMot(mot, Amot):
	nblettre1 = [0,0,0,0]
	nblettre2 = [0,0,0,0]
	i = 0
	for value in mot:
		if value == "A":
			nblettre1[0] += 1
		if value == "B":
			nblettre1[1] += 1
		if value == "C":
			nblettre1[2] += 1
		if value == "D":
			nblettre1[3] += 1

	for value in Amot:
		if value == "A":
			nblettre2[0] += 1
		if value == "B":
			nblettre2[1] += 1
		if value == "C":
			nblettre2[2] += 1
		if value == "D":
			nblettre2[3] += 1

	while i<4:
		if(nblettre1[i]<nblettre2[i]):
			return False
		i += 1
	return True



def testAjoutLettre(mot, Amot, lettre):
	return verifMot(mot, Amot+lettre)


def ajoutLettre(mot, Amot, lettre):
	result = []
	for value in lettre:
		if (testAjoutLettre(mot, Amot, value)):
			resultat.append(Amot+value)
	return result

"""
def ajoutelettresliste(mot, Amot, lettre):
	result = []
	for value in Amot:
		result.append(ajoutLettre(mot,value,lettre))
	return result

test = []
for value in mot:
	test.append(ajoutelettresliste(mot,test,lettre))
"""

print(ajoutLettre(mot,'ABA',lettre))

"""
print(testAjoutLettre(mot,'ABA','C'))
"""
quit = ""
while quit != "q":
	quit = input("Pour quitter entrez q : ")