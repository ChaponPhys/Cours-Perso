from lycee import *

# Rentrons dans le script du programme les valeurs de i1 et i2.
# i1 = valeurs de l'angle d'incidence.
# Taper entre les crochets les différentes valeurs de i1 et les séparer par des virgules.
i1 = np.array([0, 10, 20, 30, 40, 50, 60, 70])
# i1 = valeurs de l'angle de réfraction
# Taper entre les crochets les différentes valeurs de i2 et les séparer par des virgules.
i2 = np.array([0, 7, 15, 22, 29, 35, 41, 45])

# Calculons pour chacune des valeurs sin(i1) et sin(i2)
sin_i1 = np.sin(i1 * pi / 180.)
sin_i2 = np.sin(i2 * pi / 180.)

# Regression lineaire : sin_i2 = k * sin_i1
k, _, _, _, _ = linregress(sin_i1, sin_i2)

# Affichons le graphique à l'écran
repere.plot(sin_i1,      sin_i2, 'ob', markersize=4, label="mesures") # On représente sin_i2 en fontion de sin_i1.
repere.plot(sin_i1,  k * sin_i1, '-r',  linewidth=1, label="modele : sin(i2) = {:.3f} * sin(i1)".format(k))  # On représente le modèle lineaire de sin_i2 en fontion de sin_i1.
repere.legend()
repere.xlabel("sin(i1)")  # On donne un nom à l'axe des abscisses.
repere.ylabel("sin(i2)")  # On donne un nom à l'axe des ordonnées.
repere.axis("equal")      # On choisit une échelle identique pour les axes.
repere.title("Représentation du sinus de l'angle de réfraction \n en fonction du sinus de l'angle d'incidence") # On donne un titre à notre graphique.
repere.show() # Cette dernière ligne du script permet d'afficher à l'écran le graphique.

