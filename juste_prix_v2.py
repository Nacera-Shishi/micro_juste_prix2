# j'importe random
import random

# c'est pour afficher un message de Bienvenu
print("|-------------------------------------------------------------------------|")
print("  Bienvenu(e) à tous et toutes dans le juste prix Amusez-vous bien \(^_^)/  ")
print("|-------------------------------------------------------------------------|")

#On compte le nombre d'essais qu'il a fallu à l'ordinateur
#Pour trouver la réponse
nbr_essai_min = 0
nbr_essai_max = 9

# ceci choisi un nombre au hasard entre 1 et 100
juste_prix = random.randint(1,100)

# j'invite la personne a indiquer un nombre
prix = int(input("Entrer un prix entre 1 et 100: "))

# j'utilise une boucle + condition pour pas depasser 10 essaie
while juste_prix != prix and nbr_essai_min <= nbr_essai_max:
       
    nbr_essai_min +=1
       
    if juste_prix < prix:
        
        print(f" vous avez utiliser {nbr_essai_min} essaie sur 10")
        
        print("C’est moin recommencer.")
        
        prix = int(input("Entrer un prix entre 1 et 100 vous n'avez que 10 essaie: "))
        
    elif juste_prix > prix:
        
        print(f" vous avez utiliser {nbr_essai_min} essaie sur 10")
        print("C’est plus recommencer.")
        
        prix = int(input("Entrer un prix  entre 1 et 100 vous n'avez que 10 essaie: "))
            
if juste_prix != prix:
        print(" il vous reste plus d'essaie")
        print(f"Vous avez perdu le bon nombre etait ({juste_prix})")
   
else:
     
    print(f"BRAVO \(^_^)/ le numero ({juste_prix}) est le numero gagnant,\n vous avez trouvez apres ({nbr_essai_min}) essaie \n de ce fait la parti est terminer au revoir au plaisir de vous revoir à tres bientôt.\n")