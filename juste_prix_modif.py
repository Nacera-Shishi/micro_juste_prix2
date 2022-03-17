                    #----------------------------------------------------------------#
                   #|              Python : Le juste Prix Finaliser                  |#
                    #----------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------#
                    #                        Mode facile                             #
#------------------------------------------------------------------------------------------------------------------#
    
import random

Debutant = 1
Normal = 2
Personnaliser = 3
Menu = 0

Games = int(input("Choisisez entres c'est 3 modes:  \n * Pour Personaliser Taper (3) \n * Pour Normal Taper (2) \n * Pour Facile Taper (1) \n choisissez entre 1 et 3 :  " ))

while Games == Menu or Games != Menu:
    
    if Games == Menu:
            
        Games = int(input("Choisisez entres c'est 3 modes:  \n * Pour Personaliser Taper (3) \n * Pour Normal Taper (2) \n * Pour Facile Taper (1) \n choisissez entre 1 et 3 :  " ))

    if Games == Debutant:
        
        print("|--------------------------------------------------------------------------------------------------------|--------")
        print("  Bienvenu(e) à tous et toutes dans le juste prix vous avez choisi la version Debutant Amusez-vous bien\(^_^)/  ")
        print("|-------------------------------------------------------------------------------------------------------|--------")

    prix = int(input("Entrer un prix entre 1 et 100: "))

    juste_prix = random.randint(1, 100)

    while juste_prix != prix and prix != 0:
        
        if prix < juste_prix:
            print("C’est plus")
            prix = int(input("Entrer un prix entre 1 et 100 : "))

        elif prix > juste_prix:
            print("C’est moin")
            prix = int(input("Entrer un prix  entre 1 et 100: "))

    else:
        
        if prix == 0:
                
            Games = int(input("Choisisez entres c'est 3 modes:  \n * Pour Personaliser Taper (3) \n * Pour Normal Taper (2) \n * Pour Facile Taper (1) \n choisissez entre 1 et 3 :  " ))
            
        else:    
            print(" ")
            print(f"Bravo vous avez gagner Felicitation!!! \(^_^)/ \n{prix} est le numero gagnant.")
            print(" ")
            exit

                                                # FIN #

    #--------------------------------------------------------------------------------------------------------------#    
                        #                       Mode normale                              #
    #--------------------------------------------------------------------------------------------------------------#

    if Games == Normal :

        print("|-------------------------------------------------------------------------------------------------------|--------")
        print("  Bienvenu(e) à tous et toutes dans le juste prix Vous avez choisi la version Normal Amusez-vous bien \(^_^)/  ")
        print("|--------------------------------------------------------------------------------------------------------|--------")

    nbr_essai_min = 0
    nbr_essai_max = 9

    juste_prix = random.randint(1,100)

    # j'invite la personne a indiquer un nombre
    prix = int(input("Entrer un prix entre 1 et 100 Vous n'avez que 10 essaie: "))

    # j'utilise une boucle + condition pour pas depasser 10 essaie
    while juste_prix != prix and nbr_essai_min <= nbr_essai_max:
        
        nbr_essai_min +=1
        
        if juste_prix < prix and prix != 0:
            
            print(f" vous avez utiliser {nbr_essai_min} essaie sur 10")
            
            print("C’est moin recommencer.")
            
            prix = int(input("Entrer un prix entre 1 et 100 vous n'avez que 10 essaie: "))
            
        elif juste_prix > prix:
            
            print(f" vous avez utiliser {nbr_essai_min} essaie sur 10")
            print("C’est plus recommencer.")
            
            prix = int(input("Entrer un prix  entre 1 et 100 vous n'avez que 10 essaie: "))
                    
    if juste_prix != prix:
            print(" ")
            print(" il vous reste plus d'essaie")
            print(f"Vous avez perdu le bon nombre etait ({juste_prix}) \n")
    
    else:   
        
        if prix == 0:
                
            Games = int(input("Choisisez entres c'est 3 modes:  \n * Pour Personaliser Taper (3) \n * Pour Normal Taper (2) \n * Pour Facile Taper (1) \n choisissez entre 1 et 3 :  " ))
        else:    
            print(" ")
            print(f"BRAVO \(^_^)/ le numero ({juste_prix}) est le numero gagnant,\n vous avez trouvez apres ({nbr_essai_min}) essaie \n de ce fait la parti est terminer au revoir au plaisir de vous revoir à tres bientôt.\n")
            exit
                                                    # FIN #
                                                
    #--------------------------------------------------------------------------------------------------------------# 
                        #                       Mode Personnalisé                        #
    #--------------------------------------------------------------------------------------------------------------#
    
    if Games == Personnaliser:
    
            
        print("|----------------------------------------------------------------------------------------|")
        print("  Bienvenu(e) à tous et toutes dans le juste prix Personnaliser Amusez-vous bien \(^_^)/  ")
        print("|----------------------------------------------------------------------------------------|")
        
        # Mes variables essais
        nbr_essai_min = 1
        nbr_essai_max = int(input("Choisissez le nombre d'essaie : "))
        
        # je demande a l'utilisateur d'entrer un nombre max qui ensuite generera alors un nombre aleatoire entre le max et le min grace la boucle for qui contient le randint    
        prix_maximum = int(input("Choisissez un nombre aleatoire qui sera le maximum: "))
    
        prix_minimum = 0
        
        for i in range(prix_maximum):
            
            aleatoire=random.randint(prix_minimum,prix_maximum)
        
        prix = int(input(f"Entrer un nombre entre 1 et {prix_maximum} : "))
        
        while aleatoire != prix and nbr_essai_min < nbr_essai_max and prix != 0:
            
            if aleatoire < prix:
                print(" ")
                print("c'est moin reessayer\n")
                print (f"Vous avez utiliser {nbr_essai_min} essai sur {nbr_essai_max}\n")
                prix = int(input(f"Entre nombre entre 1 et {prix_maximum} : "))
            elif aleatoire > prix:
                print(" ")
                print("c'est plus reessayer\n")
                print (f"Vous avez utiliser {nbr_essai_min} essai sur {nbr_essai_max}\n")
                prix = int(input(f"Entre nombre entre 1 et {prix_maximum} : "))
            nbr_essai_min +=1
        else:
            
            if prix == 0:
                
                Games = int(input("Choisisez entres c'est 3 modes:  \n * Pour Personaliser Taper (3) \n * Pour Normal Taper (2) \n * Pour Facile Taper (1) \n choisissez entre 1 et 3 :  " ))
            
            if aleatoire != prix:
                print(" ")
                print("-il ne vous reste plus d'essai ")
                print(f"-Vous avez perdu le bon nombre etait ({aleatoire})\n")
                
            else:
                print(" ")
                print(f"BRAVO \(^_^)/ \nle numero ({aleatoire}) est le numero gagnant,\nvous avez trouvé apres ({nbr_essai_min}) essai \nde ce fait la parti est terminer au revoir au plaisir de vous revoir à tres bientôt.\n") 
                
                                                        # FIN #
            
        #-------------------------------------------------------------------------------------------------------------#