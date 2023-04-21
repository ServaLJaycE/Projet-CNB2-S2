import tkinter as tk
from PIL import ImageTk, Image

# Définition de la fonction pour tracer les barres sur l'image du triangle des sols
def tracer_barres(sandy, clay, loam):
    x1 = 5*(clay/2)
    y1 = 5*(100 - clay)
    x2 = 5*(0.5*loam +50)
    y2 = 5*(loam)
    x3 = 5*(100-sandy)
    y3 = 5*(100)
    canvas.create_line(x1, y1, 5*100, y1, fill="red", width=3) #clay
    canvas.create_line(x2, y2, 5*-900, 5*2000, fill="blue", width=3) #loam
    canvas.create_line(x3, y3, 5*-10000, 5*-20000, fill="green", width=3)

# Définition de la fonction pour récupérer les valeurs entrées par l'utilisateur
def recup_valeurs():
    sandy = float(sandy_entry.get())
    clay = float(clay_entry.get())
    loam = float(loam_entry.get())
    tracer_barres(sandy, clay, loam)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Triangle des sols")

# Chargement de l'image du triangle des sols
img = Image.open("img.png")
img = img.resize((500, 500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Création du canevas pour afficher l'image
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Création des boîtes de dialogue pour entrer les valeurs en pourcentage
sandy_label = tk.Label(root, text="Sable (en %) :")
sandy_label.pack()
sandy_entry = tk.Entry(root)
sandy_entry.pack()

clay_label = tk.Label(root, text="Argile (en %) :")
clay_label.pack()
clay_entry = tk.Entry(root)
clay_entry.pack()

loam_label = tk.Label(root, text="Limon (en %) :")
loam_label.pack()
loam_entry = tk.Entry(root)
loam_entry.pack()

# Création du bouton pour lancer l'affichage des barres sur l'image
valider_button = tk.Button(root, text="Valider", command=recup_valeurs)
valider_button.pack()

# Lancement de la boucle principale
root.mainloop()
