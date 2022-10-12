# Thomas Deleuze Bisson
# 9 Octobre 2022

string = input("Quelle est ta phrase : ")


# je cree une fonction qui me permet d effectuer l operation de compter le nombre de mots
def count_word(string):
    count = 0
    if string == "":
        print(0)
    else:
        # je creer une for loop afin d itterer sur chaque caracteres
        for characteres in string:
            # j'etablie que si le caractere est un espace, j ajoute un mot au compteur
            if characteres == " ":
                count += 1
    # je definis que le nombre de mots = compteur_de_mots + 1 puis je le return ensuite
    nombre_de_mots = count + 1
    return nombre_de_mots


# Je definis une variable portant la valeur de la fonction afin de ne pas faire appel a une fonction dans une autre
# fonction
resultat_final = count_word(string)
print(resultat_final)
