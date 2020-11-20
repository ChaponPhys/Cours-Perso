import numpy as np
import matplotlib.pyplot as plt

#Positions du point M
x=[10,10,10,10,10,10,10]# a compléter 
y=[20,19.56,18.24,16.04,12.96,9.03,4.25] # a compléter 

#Tracé de la chronophotographie
plt.plot(x,y,'o',markersize=4)
plt.xlabel("axe des x (en m)")# a compléter nom axe + unité
plt.ylabel(" m y (en)")# a compléter nom axe + unité 
plt.title("trajectoire du point M") # a compléter title : titre

#Tracé des vecteurs vitesse
N= 7 # a compléter
dt=0.3 # a compléter
for k in range(0, N-1) :
    Vy=(y[k+1]- y[k])/dt  # a compléter
    
    echelle=0.02
    Vy=Vy*echelle
    
    plt.quiver(x[k],y[k],0,Vy, color="red",scale=1,scale_units='xy')# a compléter

#Affichage
plt.show()


