import numpy as np
import matplotlib.pyplot as plt

#Positions du point M
x=[...,...,...,...,...,...] # a compléter 
y=[...,...,...,...,...,...] # a compléter 

#Tracé de la chronophotographie
plt.plot(x,y,'o',markersize=4)
plt.xlabel("........")# a compléter nom axe + unité
plt.ylabel(".....)")# a compléter nom axe + unité 
plt.title(".......") # a compléter title : titre

#Tracé des vecteurs vitesse
N=... # a compléter
dt=...# a compléter
for k in range(N-1) :
    Vy=(y[...]- y[...])/dt  # a compléter
    
    echelle=0.2
    Vy=Vy*echelle
    
    plt.quiver(x[...],y[...],0,..., color="red",scale=1,scale_units='xy')# a compléter

#Affichage
plt.show()


