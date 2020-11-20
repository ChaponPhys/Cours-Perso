import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

# Valeurs expérimentales
...=np.array([...,...,...,...,...,...,...,...,... ]) #I en mA
...=np.array([...,...,...,...,...,...,...,...,... ]) #U en V

# Représentation d'un nuage de points
plt.plot(I,U,'o',color='green')  

# Modélisation d'une courbe : lignes à compléter à l'aide du doc 3      
droite=sc.linregress(...,...) 
coefficient=droite.slope 
print("Coefficient directeur :",coefficient) 
oorigine=droite.intercept 
print("Ordonnée à l'origine :",oorigine)

# Tracé de la droite de régression : lignes à compléter à l'aide du doc 3
U_modele=...*I+...
plt.plot(I,U_modele,color='red')  

### Configuration de l'aspect du graphique : renommer les axes et le titre 
plt.xlabel("...")  
plt.ylabel("...")
plt.title("...")
plt.grid()   

# Affichage
plt.show()
