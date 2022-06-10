# Exercice 1 : Créer une fonction qui renvoie un tableau:
#       - Contenant les n premiers nombres entiers positifs (à partir de 0), où n est l'argument de la fonction
#       - Contenant les n premiers nombres entiers impairs, où n est l'argument de la fonction.
def tableau():
    n=int(input("Saisir la valeur de 'n' : "))
    tableau_entiers=[]
    for i in range(n + 1):
        tableau_entiers.append(i)
    print(tableau_entiers)

def tableau1():
    n=int(input("Saisir la valeur de 'n' : "))
    tableau_entiers=[]
    for i in range(n + 1):
        if i % 2 != 0:
            tableau_entiers.append(i)
    print(tableau_entiers)

# Exercice 2 : Ecrire une fonction qui prend en argument un élément de x et un tableau, t
# , et qui détermine si l'élément x apparaît dans le tableau t (si x apparait dans t, retourne
# son indice).
#           Remarque: Il existe en Python le mot clé break. Lorsque le programme
#           atteint ce mot clé lors de son execution, il sort immédiatement de la
#           boucle dans laquelle il se trouvait.

import random

def exercice_2(x,t):

    for i in range(0,100):
        t.append(random.randint(0,99))
    for i in range(len(t)):
        if t[i] == x:
            print(f"{x} est contenue dans le tableau 't' à l'indice {i + 1}.")
            break
    else:
        print("'x' n'est pas contenue dans 't'.")

# Autre mnière de faire :

def exercice_2_1(x,t):
    for i in range(0,100):
        t.append(random.randint(0,99))
    print(t)
    if x in t:
        indice=t.index(x)
    print(indice)

# Exercice 3 : Ecrire un proogramme (compter_voyelless.py) qui fait saisir une phrase par l'utilisateur, puis qui compte ne nombre
# de voyelles dans cette phrase, et enfin qui affiche ce nombre à l'écran.

def compter_voyelles():
    voyelles=['a','e','i','o','u','y']
    resultat=0

    phrase=input("Saisir une phrase : ")

    for i in range(len(phrase)):
        if phrase[i] in voyelles:
            resultat+=1
    print(resultat)

# Exercice 4 : Ecrire un programme (compter_mots.py) qui affectera les
# tâches suivantes : 
#   - Faire saisir une phrase avec input()
#   - Compter les mots de cette phrase, puis afficher ce nombre de mots.
#   - On considérera que le séparateur des mots est le caractère 'espace'.

def compter_mots():
    espace = ' '
    resultat=0
    
    phrase=input('Saisir une phrase : ')
    for i in range(len(phrase)):
        if phrase[i] == espace:
            resultat+=1
    print(resultat)

# Exercice 5 : Ecrire une fonction qui implémente l'une des méthodes de tri étudiées
# (le tri à bulles, par séléction, par insertion, par fusion) sur le tableau 't' passé
# en argument.

def tri_bullees(t):
    for a in range(100):
        t.append(random.randint(0,100))
    for i in range(len(t)):
        for j in range(0, len(t)-i-1):
            if t[j] > t[j+1]:
                t[j], t[j+1] = t[j+1], t[j]
    print(t)

def tri_selection(t):
    for a in range(100):
        t.append(random.randint(0,100))
    for i in range(len(t)):
        min = i
        for j in range(i+1, len(t)):
            if t[min]>t[j]:
                min=j
                
        tmp=t[i]
        t[i]=t[min]
        t[min]=tmp
        
    print(t)
    
def tri_insertion(t):
    for a in range(100):
        t.append(random.randint(0,100))
    for i in range(len(t)-1):
        x = t[i]
        j = i
        while (j > 0) and (t[j-1] > x):
            t[j] = t[j-1]
            j-=1
        t[j] = x

    print(t)
    
    
    
#Tri fusion fonction de division du tableau
def tri_fusion(tableau):
    if  len(tableau) <= 1: 
        return tableau
    pivot = len(tableau)//2
    tableau1 = tableau[:pivot]
    tableau2 = tableau[pivot:]
    gauche = tri_fusion(tableau1)
    droite = tri_fusion(tableau2)
    fusionne = fusion(gauche,droite)
    return fusionne
#Tri fusion fonction de fusion de 2 listes
def fusion(tableau1,tableau2):
    indice_tableau1 = 0
    indice_tableau2 = 0    
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []
    while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:
        if tableau1[indice_tableau1] < tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1 += 1
        else:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2 += 1
    while indice_tableau1<taille_tableau1:
        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1+=1
    while indice_tableau2<taille_tableau2:
        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2+=1
    return tableau_fusionne


def compte_itterations():
    cylabe=input("Saisir la cylabe : ")
    phrase=input("Saisir une phrase : ")
    resultat = 0

    if cylabe in phrase:
        for i in range(0, len(phrase)):
            if phrase[i:len(cylabe)]==cylabe:
                resultat+=1
        print(resultat)
    else:
        print('Occurence non trouvée.')    
            
# ----------------------------------------------------------------------------------------------------------------------------------

if __name__=='__main__':
    t = []
    tableau = []
    # tableau()
    # tableau1()
    # x = int(input("Saisir la valeur de 'x' : "))
    # exercice_2_1(x,t)
    # compter_voyelles()
    # compter_mots()
    # tri_bullees(t)
    # tri_selection(t)
    # tri_insertion(t)
# for a in range(100):
#         tableau.append(random.randint(0,100))
# tableau_trie = tri_fusion(tableau)
# print(tableau_trie)
    compte_itterations()