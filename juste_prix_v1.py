#PYTHON J'appelle l'element random pour que  ma fonction randint  fonctionne.
import random

# Ici, j'affiche un message qui dit bienvenu au joueur avec un print.
print("Bienvenu tres cher joueur dans le juste prix")

#J'affecte à ma variable  un input (qui permet a l'utilisateur d'entrer un nombre dans le terminal)
number = int(input("Entrer un prix entre 1 et 100: "))


#J'affecte à ma variable 2 prix dans la fonction randint que j'appelle price, 
# cette fonction va générer un nombre aléatoires de 1000 a 10000 compris.
price = random.randint(1, 100)


# ici j'utilise une boucle que temps que le nombre entré par l'utilisateur dans le terminal est différent du nombre qui a été généré par la fonction randint. 
# On continue de vérifier avec les conditions ci-dessous.
while number != price:
    
    
 #Si le nombre générer par randint est inférieur au nombre que l'utilisateur a entrer.
 #On indique que c'est moins, on l'invite à recommencer    
    if price < number:
        print("C’est moin veuillez renoté un prix.")
        number = int(input("Entrer un prix entre 1 et 100 : "))

 
 #Si le nombre générer par randint est supérieure au nombre que l'utilisateur a entrer.
 #On indique que c'est plus, on l'invite à recommencer 
    elif price > number:
        print("C’est plus veuillez renoté un prix")
        number = int(input("Entrer un prix  entre 1 et 100: "))

#Ici pour notre dernière condition, c'est que une fois que l'utilisateur trouve le bon nombre, on affiche a ce moment la un message ou on le félicitations, d'avoir trouver le bon nombre.
else:
    print(f"Bravo vous avez gagner yahouu !!! (^_^) {price} est le numero gagnant.")