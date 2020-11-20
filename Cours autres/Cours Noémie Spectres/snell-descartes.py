from lycee import *

 #Rentrons dans le script du programme les coordonnées (x,y) des positions successives de la balle au cours du temps.

x=np.array([...])
 #x = abscisse (axe horizontal)
 #Taper entre les crochets les différentes valeurs de x et les séparer par des virgules.
 #Arrondir les valeurs à 3 chiffres après la virgule. Ex : [1.261,1.343,...]

y=np.array([...])
 #y = ordonnée (axe vertical)
 #Taper entre les crochets les différentes valeurs de y et les séparer par des virgules.
 #Arrondir les valeurs à 3 chiffres après la virgule. Ex : [0.746,0.939,...]

 #Représentons les positions successives de la balle au cours du temps sur un repère.

repere.plot(x,y,'o',markersize=4) #On représente x en fontion de y. Les positions seront représentées par le symbole o de taille 4.
repere.xlabel("x (en m)") #On donne un nom à l'axe des abscisses et on précise l'unité : x (en m)
repere.ylabel("y (en m)") #On donne un nom à l'axe des ordonnées et on précise l'unité : y (en m)
repere.axis([0.5,1.5,0,1.5]) #On choisit une échelle adaptée pour les axes.
repere.title("Trajectoire de la balle") #On donne un titre à notre graphique : Trajectoire de la balle

#Affichons le graphique à l'écran

repere.show() #Cette dernière ligne du script permet d'afficher à l'écran le graphique.

