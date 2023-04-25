from openpyxl import load_workbook
from tkinter import * 
from tkinter.filedialog import *
import tkinter as tk
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image #1





#Toutes les fonctions :


#Fonction pour modifier le excel
def import_excel():
    #on charge le fichier excel
    ##nom_fichier = texte.get("1.0", "end-1c")
    ##nom_fichier = nom_fichier + ".xlsx"
    ##workbook = load_workbook(filename=nom_fichier)
    donnees_importees = askopenfilename(title="Ouvrir un fichier",filetypes=[('xlsx files','.xlsx')])
    return donnees_importees
  

#Les fonction de calcul
def calcul_terre(donnees):
     workbook = load_workbook(filename=donnees)
     #on ouvre le fichier excel
     sheet = workbook.active
     #on modifie la cellule A1
     sheet["A1"] = "terre"
     #on sauvegarde le fichier
     workbook.save(filename="value.xlsx")
     afficher_graphique()
def executer_terre():
     donnees_importees = import_excel()
     calcul_terre(donnees_importees)
     resultat="fin"
     resultat_label.configure(text="état : " + str(resultat))

def calcul_eau(donnees):
     workbook = load_workbook(filename=donnees)
     #on ouvre le fichier excel
     sheet = workbook.active
     #on modifie la cellule A1
     sheet["A1"] = "eau"
     #on sauvegarde le fichier
     workbook.save(filename="value.xlsx")
     afficher_graphique()
def executer_eau():
     donnees_importees = import_excel()
     calcul_eau(donnees_importees)
     resultat="fin"
     resultat_label.configure(text="état : " + str(resultat))

def calcul_air(donnees):
     workbook = load_workbook(filename=donnees)
     #on ouvre le fichier excel
     sheet = workbook.active
     #on modifie la cellule A1
     sheet["A1"] = "air"
     #on sauvegarde le fichier
     workbook.save(filename="value.xlsx")
     afficher_graphique()
def executer_air():
     donnees_importees = import_excel()
     calcul_air(donnees_importees)
     resultat="fin"
     resultat_label.configure(text="état : " + str(resultat))

def calcul_perso(alpha,beta,omega,donnees):
    workbook=load_workbook(filename=donnees)
    #on ouvre le fichier excel
    sheet=workbook.active
    #on modifie les cellules
    sheet["A1"]=alpha
    sheet["A2"]=beta
    sheet["A3"]=omega
    #on sauvegarde lefichier
    workbook.save(filename="value.xlsx")
    afficher_graphique()
def executer_perso():
    alpha = float(valeur_alpha.get())
    beta = float(valeur_beta.get())
    omega = float(valeur_omega.get())
    donnees_importees=import_excel()
    calcul_perso(alpha,beta,omega,donnees_importees)
    resultat="fin"
    resultat_label.configure(text="état : "+str(resultat))


# Afficher le nouveau tableau excel
def afficher_excel():
     #on charge le fichier excel
     workbook = load_workbook("value.xlsx")
     #on ouvre le fichier excel
     sheet = workbook.active
     #on vide la zone de texte
     text_pre.delete("1.0", "end-1c")
     #on affiche tout le tableau
     for row in sheet.iter_rows():
        for cell in row:
            value = cell.value
            text_pre.insert(tk.END, f"{value}\t")
        text_pre.insert(tk.END, "\n")    


# Afficher le graphique
def afficher_graphique():
    largeur = fenetre.winfo_screenwidth()
    hauteur = fenetre.winfo_screenheight()
    #on charge le fichier excel
    workbook = load_workbook(filename="value.xlsx")
    #on ouvre le fichier excel
    sheet = workbook.active
    #on dessine le graphique avec x la 1ere colonne et y la 2eme colonne
    x = []
    y = []
    for row in sheet.iter_rows(min_row=2):
        x.append(row[0].value)
        y.append(row[1].value)
    fig = plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.get_tk_widget().place(relx=0.6, rely=0.05, width=largeur/3, height=hauteur/3)
    #on met des bordures épaisses noire
    canvas.get_tk_widget().config(highlightthickness=1, highlightbackground="black")
    canvas.draw()


# Fonction pour changer le theme
def toggle():
    global switch_value
    if switch_value == True:
        switch.config(image=dark, bg="#26242f",
                      activebackground="#26242f")
        switch_value = False
        #met la fenetre en noir
        fenetre.config(bg="#26242f") 
        #modifie couleur des textes
        label_titre.config(bg="#26242f", fg="white")
        label_titre.pack()
        label_select1.config(bg="#26242f", fg="white")
        label_select1.pack()
        label_select2.config(bg="#26242f", fg="white")
        label_select2.pack()
        sandy_label.config(bg="#26242f", fg="white")
        sandy_label.pack()
        loam_label.config(bg="#26242f", fg="white")
        loam_label.pack()
        clay_label.config(bg="#26242f", fg="white")
        clay_label.pack()
        resultat_label.config(bg="#26242f", fg="white")
        resultat_label.pack()
        text_pre.config(bg="black", fg="white") #bg ="grey15"
        text_pre.pack()
        cadre_utilisateur.config(bg="#26242f")
        cadre_utilisateur.pack(side="left",anchor="nw",padx=0, pady=(30,0))
        cadre_resultat.config(bg="#26242f")
        cadre_resultat.pack(side="top", anchor="nw", padx=0, pady=0)
        cadre_sol.config(bg="#26242f")
        cadre_sol.pack(side="top", anchor="nw", padx=(10,0), pady=(0,50))
        cadre_boutons.config(bg="#26242f")
        cadre_boutons.pack(side="top", anchor="sw", padx=(10,0), pady=0)
        valeurs_perso_label.config(bg="#26242f", fg="white")
        valeurs_perso_label.pack(anchor="w", padx=10, pady=0)
        #couleur du graphique
        plt.style.use('dark_background')
        if os.path.exists("value.xlsx"):
          afficher_graphique()
    else:
        switch.config(image=light, bg="white", 
                      activebackground="white")
        switch_value = True  
        #met la fenetre en blanc
        fenetre.config(bg="white") 
        #modifie couleur des textes
        label_titre.config(bg="white", fg="black")
        label_titre.pack()
        label_select1.config(bg="white", fg="black")
        label_select1.pack()
        label_select2.config(bg="white", fg="black")
        label_select2.pack()
        sandy_label.config(bg="white", fg="black")
        sandy_label.pack()
        clay_label.config(bg="white", fg="black")
        clay_label.pack()
        loam_label.config(bg="white", fg="black")
        loam_label.pack()
        resultat_label.config(bg="white", fg="black")
        resultat_label.pack()
        text_pre.config(bg="white", fg="black")
        text_pre.pack()
        cadre_utilisateur.config(bg="white")
        cadre_utilisateur.pack(side="left",anchor="nw",padx=0, pady=(30,0))
        cadre_resultat.config(bg="white")
        cadre_resultat.pack(side="top", anchor="nw", padx=0, pady=0)
        cadre_sol.config(bg="white")
        cadre_sol.pack(side="top", anchor="nw", padx=(10,0), pady=(0,50))
        cadre_boutons.config(bg="white")
        cadre_boutons.pack(side="top", anchor="sw", padx=(10,0), pady=0)
        valeurs_perso_label.config(bg="white", fg="black")
        valeurs_perso_label.pack(anchor="w", padx=10, pady=0)
        #couleur du graphique
        plt.style.use('default')
        if os.path.exists("value.xlsx"):
          afficher_graphique()


# Définition de la fonction pour récupérer les valeurs entrées par l'utilisateur #2
def recup_valeurs():
    sandy = float(sandy_entry.get())
    clay = float(clay_entry.get())
    loam = float(loam_entry.get())
    tracer_barres(sandy, clay, loam)


#Fonction pour dessiner les barres #3
def tracer_barres(sandy, clay, loam):
    x1 = 2.5*(clay/2)
    y1 = 2.5*(100 - clay)
    x2 = 2.5*(0.5*loam +50)
    y2 = 2.5*(loam)
    x3 = 2.5*(100-sandy)
    y3 = 2.5*(100)
    canvas.create_line(x1, y1, 2.5*100, y1, fill="red", width=3) #clay
    canvas.create_line(x2, y2, 2.5*-900, 2.5*2000, fill="blue", width=3) #loam
    canvas.create_line(x3, y3, 2.5*-10000, 2.5*-20000, fill="green", width=3)
        




#On met le code principal :





#on cree la fenetre
fenetre = Tk()
fenetre.title("S-EAU-L")
fenetre.geometry("500x500")
fenetre.config(bg="white") 
  

# Ajout des logos pour le theme
light = PhotoImage(file="light.png")
light = light.subsample(30, 30) #on redefinit leurs tailles
dark = PhotoImage(file="dark.png")
dark = dark.subsample(30, 30) #on redefinit leurs tailles
switch_value = True


#on demande les données de tailles de la fenetre
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()


#bouton pour quitter
boutton = Button(fenetre, text="Quitter", command=fenetre.quit)
boutton.place(x=largeur-50, y=0)


#bouton de bienvenue
label_titre = Label(fenetre, text="Bienvenue dans S-EAU-L", bg="white", fg="black")
label_titre.pack()


#Les deux cadres principaux 
cadre_utilisateur = tk.Frame(fenetre)
cadre_utilisateur.config(bg="white")
cadre_utilisateur.pack(side="left",anchor="nw",padx=0, pady=(30,0))

cadre_resultat = tk.Frame(fenetre)
cadre_resultat.config(bg="white")
cadre_resultat.pack(side="top", anchor="nw", padx=0, pady=0)

# Cadre pourcentage de sol
cadre_sol = tk.Frame(cadre_utilisateur)
cadre_sol.config(bg="white")
cadre_sol.pack(side="top", anchor="nw", padx=(10,0), pady=(0,50))

# Cadre pour les boutons de choix de sol
cadre_boutons = tk.Frame(cadre_utilisateur)
cadre_boutons.config(bg="white")
cadre_boutons.pack(side="top", anchor="sw", padx=(10,0), pady=0)

# Cadre pour image triangle des sols
cadre_image = tk.Frame(cadre_resultat)
cadre_image.pack(side="top", padx=(10,500), pady=10)



#titre de la zone de choix des pourcentages
label_select1 = Label(cadre_sol, text="Trouvez votre type de sol :", bg="white", fg="black")
label_select1.pack(anchor="w", padx=10, pady=20)

# Création des boîtes pour entrer les valeurs en pourcentage
sandy_label = tk.Label(cadre_sol, text="Sable (en %) :")
sandy_label.pack()
sandy_entry = tk.Entry(cadre_sol)
sandy_entry.pack()

clay_label = tk.Label(cadre_sol, text="Argile (en %) :")
clay_label.pack()
clay_entry = tk.Entry(cadre_sol)
clay_entry.pack()

loam_label = tk.Label(cadre_sol, text="Limon (en %) :")
loam_label.pack()
loam_entry = tk.Entry(cadre_sol)
loam_entry.pack()

# Création du bouton pour lancer l'affichage des barres sur l'image
valider_button = tk.Button(cadre_sol, text="Valider", command=recup_valeurs)
valider_button.pack()



#titre de la zone bouton de choix de sol
label_select2 = Label(cadre_boutons, text="Selectionez votre type de sol :", bg="white", fg="black")
label_select2.pack(anchor="w", padx=10, pady=20)

#bouton importattion terre
boutton_t = Button(cadre_boutons, text="terre", command=executer_terre)
boutton_t.pack(anchor="w", padx=10, pady=5)

#bouton importattion eau
boutton_e = Button(cadre_boutons, text="eau", command=executer_eau )
boutton_e.pack(anchor="w", padx=10, pady=5)

#bouton importattion air
boutton_a = Button(cadre_boutons, text="air",command=executer_air)
boutton_a.pack(anchor="w", padx=10, pady=5)

#bouton importattion feu
boutton_f = Button(cadre_boutons, text="feu")
boutton_f.pack(anchor="w", padx=10, pady=5)

#bouton importattion electrique
boutton_el = Button(cadre_boutons, text="electrique")
boutton_el.pack(anchor="w", padx=10, pady=5)

#bouton importattion poison
boutton_po = Button(cadre_boutons, text="poison")
boutton_po.pack(anchor="w", padx=10, pady=5)

#bouton importattion valeurs perso
boutton_pers= Button(cadre_boutons, text="valeurs précises",command=executer_perso)
boutton_pers.pack(anchor="w", padx=10, pady=(15,5))
#Indication zone de texte valeurs perso
valeurs_perso_label = tk.Label(cadre_boutons, text="Alpha   Beta    Omega",width=20, height=1)
valeurs_perso_label.pack(anchor="w", padx=10, pady=0)
#Zone de texte pour entrer valeurs perso
valeur_alpha = tk.Entry(cadre_boutons,width=3) #height=1
valeur_alpha.pack(side="left",ipadx=4, padx=(25,0), pady=(5,0))
valeur_beta = tk.Entry(cadre_boutons, width=3)
valeur_beta.pack(side="left", ipadx=4, padx=(10,0), pady=(5,0))
valeur_omega = tk.Entry(cadre_boutons,width=3)
valeur_omega.pack(side="left", ipadx=4, padx=(10,0), pady=(5,0))




#état de la modification
resultat_label=tk.Label(cadre_boutons,text="etat : ")
resultat_label.pack(anchor="w",padx=90,pady=0)




# Chargement de l'image du triangle des sols
img = Image.open("img.png")
img = img.resize((250, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
# Création du canevas pour afficher l'image
canvas = tk.Canvas(cadre_image, width=250, height=250)
canvas.pack(side="top")
canvas.create_image(0, 0, anchor=tk.NW, image=img)



#Bouton de preview du nouveau fichier excel 
button_pre = Button(fenetre, text="Afficher les valeurs", command=afficher_excel)
button_pre.pack()


#zone de texte preview
text_pre = tk.Text(fenetre, width=largeur//3, height=hauteur//3)
scrollbar_y = tk.Scrollbar(fenetre, orient="vertical", command=text_pre.yview)
scrollbar_x = tk.Scrollbar(fenetre, orient="horizontal", command=text_pre.xview)
text_pre.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
# pack les scrollbars et text_pre
scrollbar_y.pack(side="right", fill="y",padx=(0,0), pady=(6,34))
scrollbar_x.pack(side="bottom", fill="x", padx=20, pady=5)
text_pre.pack(expand=True, padx=(20,10), pady=5)

  

# Bouton pour changer le theme
switch = Button(fenetre, image=light, 
                bd=0, bg="white",
                activebackground="white", 
                command=toggle)
switch.pack(padx=50, pady=150)
#on le place en haut a droite
switch.place(x=0, y=0)





#on ouvre fenetre en plein ecran
fenetre.attributes('-fullscreen', True)

fenetre.mainloop()


