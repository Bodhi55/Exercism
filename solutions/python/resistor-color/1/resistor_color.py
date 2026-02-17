# La liste ordonnée des couleurs

colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def color_code(color):
    # Chercher l'index d'une couleur spécifique
    return colors_list.index(color.lower())

def colors():
    # Lister toutes les couleurs disponibles
    return colors_list    