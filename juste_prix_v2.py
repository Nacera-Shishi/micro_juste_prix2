# j'importe random
import random

# c'est pour afficher un message de Bienvenu
print("|-------------------------------------------------------------------------|")
print("  Bienvenu(e) a tous et toute dans le juste prix Amusez-vous bien \(^_^)/  ")
print("|-------------------------------------------------------------------------|")

#On compte le nombre d'essais qu'il a fallu à l'ordinateur
#Pour trouver la réponse
nbr_essaie1 = 1
nbr_essaie10 = 9

# ceci choisi un nombre au hasard entre 1 et 100
prix = random.randint(1,100)

# j'invite la personne a indiquer un nombre
just_prix = int(input("Entrer un prix entre 1 et 100: "))

# j'utilise une boucle + condition pour pas depasser 10 essaie
while just_prix != prix and nbr_essaie1 <= nbr_essaie10:
       
    nbr_essaie1 +=1
       
    if prix < just_prix:
        
        print(f" vous avez utiliser {nbr_essaie1} essaie sur 10")
        
        print("C’est moin recommencer.")
        
        just_prix = int(input("Entrer un prix entre 1 et 100 vous n'avez que 10 essaie: "))
        
    elif prix > just_prix:
        
        print(f" vous avez utiliser {nbr_essaie1} essaie sur 10")
        print("C’est plus recommencer.")
        
        just_prix = int(input("Entrer un prix  entre 1 et 100: "))
        

    elif prix != just_prix:
        print(" il vous reste plus d'essaie")
        print(f"Vous avez perdu le bon nombre etait {prix}")
        
        
   
else:
     
    print(f"Bravo vous avez gagner yahouu !!! \(^_^)/ le numero {prix} est le numero gagnant,\n vous avez trouvez apres {nbr_essaie1} essaie de ce fait la parti est terminer au revoir au plaisir de vous revoir tres bientôt.")