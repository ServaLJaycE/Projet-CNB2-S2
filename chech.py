import tkinter as tk

# Fonction pour importer les données
def importer_donnees():
    # Code pour importer les données
    donnees_importees = [1, 2, 3, 4] # Exemple de données importées
    return donnees_importees

# Fonction pour calculer la Terre
def calcul_terre(donnees):
    # Code pour calculer la Terre à partir des données
    resultat = sum(donnees)
    return resultat

# Fonction pour exécuter le calcul à partir des données importées
def executer_calcul():
    donnees_importees = importer_donnees()
    resultat = calcul_terre(donnees_importees)
    # Afficher le résultat dans la fenêtre principale
    resultat_label.configure(text="Résultat : " + str(resultat))

# Créer la fenêtre principale
root = tk.Tk()

# Créer les widgets
importer_button = tk.Button(root, text="Import", command=importer_donnees)
calcul_button = tk.Button(root, text="Calcul Terre", command=executer_calcul)
resultat_label = tk.Label(root, text="Résultat : ")

# Placer les widgets dans la fenêtre
importer_button.pack()
calcul_button.pack()
resultat_label.pack()

# Lancer la boucle principale de la fenêtre
root.mainloop()
