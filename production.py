def grille(tab):
    print("")
    for i in range(len(tab)):
        if i!=2 and i!=5 and i!=8:
            print(tab[i], end="|")
        else:
            print(tab[i], end="\n")
        
def placer(tab):
    symbole=str(input("\nEntrez votre symbole\n"))
    col=0
    while col<1 or col>3:
        col=int(input("Quelle colonne ? (1-2-3)\n"))
    ligne=0
    while ligne<1 or ligne>3:
        ligne=int(input("Quelle ligne ? (1-2-3)\n"))
    if ligne==1 and col==1:
        tab[0]=symbole
    if ligne==1 and col==2:
        tab[1]=symbole
    if ligne==1 and col==3:
        tab[2]=symbole
    if ligne==2 and col==1:
        tab[3]=symbole
    if ligne==2 and col==2:
        tab[4]=symbole
    if ligne==2 and col==3:
        tab[5]=symbole
    if ligne==3 and col==1:
        tab[6]=symbole
    if ligne==3 and col==2:
        tab[7]=symbole
    if ligne==3 and col==3:
        tab[8]=symbole

def verif_ligne(tab):
    if tab[0]!=" ":
        if (tab[0]==tab[1] and tab[1]==tab[2]):
            print("Gagné !")
            return True
    if tab[3]!=" ":
        if (tab[3]==tab[4] and tab[4]==tab[5]):
            print("Gagné !")
            return True
    if tab[6]!=" ":
        if (tab[6]==tab[7] and tab[7]==tab[8]):
            print("Gagné !")
            return True
        else:
            return False
    else:
        return False
    
def verif_col(tab):
    if tab[0]!=" ":
        if (tab[0]==tab[3] and tab[3]==tab[6]):
            print("Gagné !")
            return True
    if tab[1]!=" ":
        if (tab[1]==tab[4] and tab[4]==tab[7]):
            print("Gagné !")
            return True
    if tab[2]!=" ":
        if (tab[2]==tab[5] and tab[5]==tab[8]):
            print("Gagné !")
            return True
        else:
            return False
    else:
        return False
    
def verif_diago(tab):
    if tab[0]!=" ":
        if (tab[0]==tab[4] and tab[4]==tab[8]):
            print("Gagné !")
            return True
    if tab[2]!=" ":
        if (tab[2]==tab[4] and tab[4]==tab[6]):
            print("Gagné !")
            return True
        else:
            return False
    else:
        return False

def grille_complete(tab):
    for i in range(len(tab)):
        if tab[i]==" ":
            return False
    print("Égalité...")
    return True


tableau=[" "," "," "," "," "," "," "," "," "]
while not (verif_ligne(tableau) or verif_col(tableau) or verif_diago(tableau) or grille_complete(tableau)):
    placer(tableau)
    grille(tableau)
    print("")



'''
Pour programmer un jeu de Puissance 4, il faudra tout d'abord créer une grille (et donc un tableau) plus grande.
De plus, on ne peut pas choisir de ligne puisque les jetons sont soumis à la gravité. Ainsi, seule la colonne est choisie, le jeton sera forcément sur la ligne la plus basse.
Il faut également établir les conditions de victoire : lorsque 4 jetons ou plus sont alignés, la partie s'arrête. De même si la grille est pleine.
'''