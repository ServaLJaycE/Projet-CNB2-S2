from tkinter import * 
from tkinter.filedialog import *
import tkinter as tk
import matplotlib.pyplot as plt
import os
import csv
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image 


#/////////////////////////////////////////////////////////////////////////////////////////
#Les fonctions :
#/////////////////////////////////////////////////////////////////////////////////////////


  
#Fonction pour avoir chemin d'accées de depot
#def chemin_fichier():
#    global filepath
#    filepath = askdirectory(title="Ouvrir un fichier")
#idée abandonné car necessaire de lancer l'application en mode administrateur, ce qui peut etre contraignant et effrayant pour l'utilisateur
#Mais il suffirait d'utiliser dans ce cas la open(filepath,...) dans les fonctions 
#De base cette fonction était éxecuté en appuyant sur le bouton "zone de depot"

#Les fonction de calcul
def calcul_sable(tableau):
#   global filepath ( a ne pas oublier si vous voulez restaurer la fonction chemin_fichier)
    #ouverture du csv en mode lecture
    with open(tableau, 'r') as f:
        donnees = list(csv.reader(f, delimiter=";"))
    #extrait l'entete du csv
    entetes = donnees[0]
    #créée variable de stockage
    new_entetes = []
    new_donnees = []
    #On rajoute "HygroTrue_" devant chaque "Hygro_"
    for entete in entetes:
        new_entetes.append(entete)
        if entete.startswith("Hygro_"):
            num = entete.split("_")[1]
            new_entetes.append("HygroTrue_" + num)
    #On duplique les "Hygro_" en modifiant les valeurs
    for i in range(1, len(donnees)):
        ligne = donnees[i]
        new_ligne = []
        for j in range(len(ligne)):
            new_ligne.append(ligne[j])
            if entetes[j].startswith("Hygro_"):
                new_ligne.append(str(float(ligne[j])*0.4853 - 10.836))
        new_donnees.append(new_ligne)
     #on écrit le nouveau csv avec nos variables de stockage
    with open("neww.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(new_entetes)
        writer.writerows(new_donnees)
def executer_sable():
    donnees_importees = askopenfilename(title="Ouvrir un fichier",filetypes=[('csv files','.csv'), ('xlsx files','.xlsx')])
    calcul_sable(donnees_importees)
    resultat="fin"
    resultat_label.configure(text="état : " + str(resultat))

def calcul_limon_sableux(tableau):
    #ouverture du csv en mode lecture
    with open(tableau, 'r') as f:
        donnees = list(csv.reader(f, delimiter=";"))
    #extrait l'entete du csv
    entetes = donnees[0]
    #créée variable de stockage
    new_entetes = []
    new_donnees = []
    #On rajoute "HygroTrue_" devant chaque "Hygro_"
    for entete in entetes:
        new_entetes.append(entete)
        if entete.startswith("Hygro_"):
            num = entete.split("_")[1]
            new_entetes.append("HygroTrue_" + num)
    #On duplique les "Hygro_" en modifiant les valeurs
    for i in range(1, len(donnees)):
        ligne = donnees[i]
        new_ligne = []
        for j in range(len(ligne)):
            new_ligne.append(ligne[j])
            if entetes[j].startswith("Hygro_"):
                new_ligne.append(str(float(ligne[j])*0.2072 + 11.107))
        new_donnees.append(new_ligne)
    #on écrit le nouveau csv avec nos variables de stockage
    with open("neww.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(new_entetes)
        writer.writerows(new_donnees)
def executer_limon_sableux():
    donnees_importees = askopenfilename(title="Ouvrir un fichier",filetypes=[('csv files','.csv'), ('xlsx files','.xlsx')])
    calcul_limon_sableux(donnees_importees)
    resultat="fin"
    resultat_label.configure(text="état : " + str(resultat))

def calcul_limon_argileux(tableau):
    #ouverture du csv en mode lecture
    with open(tableau, 'r') as f:
        donnees = list(csv.reader(f, delimiter=";"))
    #extrait l'entete du csv
    entetes = donnees[0]
    #créée variable de stockage
    new_entetes = []
    new_donnees = []
    #On rajoute "HygroTrue_" devant chaque "Hygro_"
    for entete in entetes:
        new_entetes.append(entete)
        if entete.startswith("Hygro_"):
            num = entete.split("_")[1]
            new_entetes.append("HygroTrue_" + num)
    #On duplique les "Hygro_" en modifiant les valeurs
    for i in range(1, len(donnees)):
        ligne = donnees[i]
        new_ligne = []
        for j in range(len(ligne)):
            new_ligne.append(ligne[j])
            if entetes[j].startswith("Hygro_"):
                new_ligne.append(str(float(ligne[j])*0.5052 - 14.891))
        new_donnees.append(new_ligne)
    #on écrit le nouveau csv avec nos variables de stockage
    with open("neww.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(new_entetes)
        writer.writerows(new_donnees)
def executer_limon_argileux():
    donnees_importees = askopenfilename(title="Ouvrir un fichier",filetypes=[('csv files','.csv'), ('xlsx files','.xlsx')])
    calcul_limon_argileux(donnees_importees)
    resultat="fin"
    resultat_label.configure(text="état : " + str(resultat))

def calcul_argile_sableux(tableau):
    #ouverture du csv en mode lecture
    with open(tableau, 'r') as f:
        donnees = list(csv.reader(f, delimiter=";"))
    #extrait l'entete du csv
    entetes = donnees[0]
    #créée variable de stockage
    new_entetes = []
    new_donnees = []
    #On rajoute "HygroTrue_" devant chaque "Hygro_"
    for entete in entetes:
        new_entetes.append(entete)
        if entete.startswith("Hygro_"):
            num = entete.split("_")[1]
            new_entetes.append("HygroTrue_" + num)
    #On duplique les "Hygro_" en modifiant les valeurs
    for i in range(1, len(donnees)):
        ligne = donnees[i]
        new_ligne = []
        for j in range(len(ligne)):
            new_ligne.append(ligne[j])
            if entetes[j].startswith("Hygro_"):
                new_ligne.append(str(float(ligne[j])*0.2305 + 7.3944))
        new_donnees.append(new_ligne)
    #on écrit le nouveau csv avec nos variables de stockage
    with open("neww.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(new_entetes)
        writer.writerows(new_donnees)
def executer_argile_sableux():
    donnees_importees = askopenfilename(title="Ouvrir un fichier",filetypes=[('csv files','.csv'), ('xlsx files','.xlsx')])
    calcul_limon_argileux(donnees_importees)
    resultat="fin"
    resultat_label.configure(text="état : " + str(resultat))

def calcul_generique(tableau):
    #ouverture du csv en mode lecture
    with open(tableau, 'r') as f:
        donnees = list(csv.reader(f, delimiter=";"))
    #extrait l'entete du csv
    entetes = donnees[0]
    #créée variable de stockage
    new_entetes = []
    new_donnees = []
    #On rajoute "HygroTrue_" devant chaque "Hygro_"
    for entete in entetes:
        new_entetes.append(entete)
        if entete.startswith("Hygro_"):
            num = entete.split("_")[1]
            new_entetes.append("HygroTrue_" + num)
    #On duplique les "Hygro_" en modifiant les valeurs
    for i in range(1, len(donnees)):
        ligne = donnees[i]
        new_ligne = []
        for j in range(len(ligne)):
            new_ligne.append(ligne[j])
            if entetes[j].startswith("Hygro_"):
                new_ligne.append(str(float(ligne[j])*0.2689 + 3.4664))
        new_donnees.append(new_ligne)
    #on écrit le nouveau csv avec nos variables de stockage
    with open("neww.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(new_entetes)
        writer.writerows(new_donnees)
def executer_generique():
    donnees_importees = askopenfilename(title="Ouvrir un fichier",filetypes=[('csv files','.csv'), ('xlsx files','.xlsx')])
    calcul_limon_argileux(donnees_importees)
    resultat="fin"
    resultat_label.configure(text="état : " + str(resultat))

def calcul_perso(alpha,beta,tableau):
    #ouverture du csv en mode lecture
    with open(tableau, 'r') as f:
        donnees = list(csv.reader(f, delimiter=";"))
    #extrait l'entete du csv
    entetes = donnees[0]
    #créée variable de stockage
    new_entetes = []
    new_donnees = []
    #On rajoute "HygroTrue_" devant chaque "Hygro_"
    for entete in entetes:
        new_entetes.append(entete)
        if entete.startswith("Hygro_"):
            num = entete.split("_")[1]
            new_entetes.append("HygroTrue_" + num)
    #On duplique les "Hygro_" en modifiant les valeurs
    for i in range(1, len(donnees)):
        ligne = donnees[i]
        new_ligne = []
        for j in range(len(ligne)):
            new_ligne.append(ligne[j])
            if entetes[j].startswith("Hygro_"):
                new_ligne.append(str(float(ligne[j])*beta + alpha))
        new_donnees.append(new_ligne)
    #on écrit le nouveau csv avec nos variables de stockage
    with open("neww.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(new_entetes)
        writer.writerows(new_donnees)
def executer_perso():
    #essayer d'executer ses lignes sinon ..
    try :
        alpha = float(valeur_alpha.get())
        beta = float(valeur_beta.get())
        donnees_importees = askopenfilename(title="Ouvrir un fichier",filetypes=[('csv files','.csv'), ('xlsx files','.xlsx')])
        calcul_perso(alpha,beta,donnees_importees)
        resultat="fin"
        resultat_label.configure(text="état : "+str(resultat))
    except:
        os.system("alerte_val_perso.vbs")


# Afficher le nouveau tableau excel
def afficher_tab():
    with open("neww.csv", 'r') as f:
        donnees = list(csv.reader(f, delimiter=";"))
    # Trouver la largeur maximale de chaque colonne
    largeurs_colonnes = [max(len(element) for element in colonne) for colonne in zip(*donnees)]
    #largeurs_colonnes =[10,10,10,10,10,10,etc..libre de modifier les valeurs et taille du tableau pour tester.] commentaire qui permet de comprendre ce que fait la ligne du dessus si besoin 
    text_pre.delete(1.0, END)
    for ligne in donnees:
        # Ajouter chaque élément de la ligne en ajustant la largeur
        ligne_formatee = '  '.join(element.ljust(largeur) for element, largeur in zip(ligne, largeurs_colonnes))
        #Ici la largeur va regarder tout le long de la ligne la plus grande taille pour chaque colonne de toute la colonne et avec ljust va rajouter des espaces jusqu'a que la case de la colonne écrite actuellement soit de la taille de la plus grande case de la colonne.
        text_pre.insert(END, ligne_formatee)
        text_pre.insert(END, "\n")


# Afficher le graphique
def afficher_graphique(fenetre):
    # Lecture du fichier CSV et création d'un DataFrame avec pandas
    data = pd.read_csv("neww.csv", delimiter=';')
    # Création du canvas pour afficher les boutons
    canvas = tk.Canvas(fenetre)
    canvas.place(relx=0.8, rely=0.1, anchor=tk.NE)
    if switch_value==1:
        canvas.config(highlightthickness=1, highlightbackground="black")
    else :
        canvas.config(highlightthickness=1, highlightbackground="black", bg="#26242f")

    # Lecture ET save des différents sites
    with open("neww.csv", 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        sites = set(row['Site'] for row in reader)
    # Variables pour organiser les boutons en colonnes de 3 lignes
    num_columns = 3
    current_row = 0
    current_column = 0
    # Création d'un bouton pour chaque site
    for site in sites:
        button = tk.Button(canvas, text=site, command=lambda site=site: afficher_graphe(site))
        button.grid(row=current_row, column=current_column, padx=5, pady=5)
        current_row += 1
        if current_row >= num_columns:
            current_row = 0
            current_column += 1
    
    # Fonction pour afficher le graphe du site sélectionné
    def afficher_graphe(site):
        # Filtrer les données pour le site sélectionné
        site_data = data[data['Site'] == site]
        # Calculer la valeur moyenne des "Hygro_" par colonne
        moyennes = site_data.filter(regex='HygroTrue_').mean()
        # Création du graphe
        plt.figure()
        plt.plot(moyennes, range(10, 70, 10), marker='o')
        plt.tick_params(axis='x', top=True)
        plt.xlabel('Valeur moyenne des "Hygrotrue_"   (en %)')
        #on met xlabel en haut 
        plt.gca().xaxis.set_label_position('top')
        plt.ylabel('Prondeur_   (en cm)')
        plt.title('Graphe Hydrométrique pour : {}'.format(site))
        plt.gca().xaxis.set_ticks_position('top')  # Déplace les valeurs de l'axe x en haut
        plt.gca().invert_yaxis()
        plt.show()


#Afficher graphique et excel
def afficher():
    afficher_tab()
    afficher_graphique(fenetre)


# Fonction pour changer le theme (dark/light)
def toggle():
    global switch_value, img, canvas_image
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
        #image triangle des sols
        img = Image.open("imgd.png")
        affiche_image()
        #couleur du graphique
        plt.style.use('dark_background')
        if os.path.exists("neww.csv"):
          afficher_graphique(fenetre)
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
        #image triangle des sols
        img = Image.open("imgl.png")
        affiche_image()
        #couleur du graphique
        plt.style.use('default')
        if os.path.exists("neww.csv"):
          afficher_graphique(fenetre)


# Définition de la fonction pour récupérer les valeurs entrées par l'utilisateur puis tracer barres
def recup_valeurs():
    sandy = float(sandy_entry.get())
    clay = float(clay_entry.get())
    loam = float(loam_entry.get())
    tracer_barres(sandy, clay, loam)


#Fonction pour dessiner les barres
lignes =[]
def tracer_barres(sandy, clay, loam):
    global lignes, canvas_image
    #on efface les anciennes barres
    for ligne in lignes :
        canvas_image.delete(ligne)
    lignes.clear()
    if (sandy+clay+loam) != 100:
        #on run l'alerte_triangle_sol.vbs
        os.system("alerte_triangle.vbs")
    else :
        #on trace les traits
        x1 = 3*(clay/2)
        y1 = 3*(100 - clay)
        x2 = 3*(0.5*loam +50)
        y2 = 3*(loam)
        x3 = 3*(100-sandy)
        y3 = 3*(100)
        lignes.append(canvas_image.create_line(x1, y1, 3*100, y1, fill="red", width=3) )#clay
        lignes.append(canvas_image.create_line(x2, y2, 3*-900, 3*2000, fill="blue", width=3)) #loam
        lignes.append(canvas_image.create_line(x3, y3, 3*-10000, 3*-20000, fill="green", width=3))
        






#/////////////////////////////////////////////////////////////////////////////////////////
#La fenetre principale :
#/////////////////////////////////////////////////////////////////////////////////////////





#on cree la fenetre
fenetre = Tk()
fenetre.title("S-EAU-L")
#fenetre.geometry("500x500") innutile car fullscreen
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
def quit() :
    fenetre.quit()
boutton = Button(fenetre, text="Quitter", command=quit)
boutton.place(x=largeur-50, y=0)



#bouton de bienvenue
label_titre = Label(fenetre, text="Bienvenue dans S-EAU-L", bg="white", fg="black", font=("Helvetica", 10))
label_titre.pack()


#Les deux cadres principaux, ne pas hésiter a recolorier les bg pour comprendre l'organisation
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

#bouton importattion sable
boutton_s = Button(cadre_boutons, text="Sable", command=executer_sable)
boutton_s.pack(anchor="w", padx=10, pady=5)

#bouton importattion limon sableux
boutton_ls = Button(cadre_boutons, text="Limon sableux", command=executer_limon_sableux)
boutton_ls.pack(anchor="w", padx=10, pady=5)

#bouton importattion limon argileux
boutton_la = Button(cadre_boutons, text="Limon argileux",command=executer_limon_argileux)
boutton_la.pack(anchor="w", padx=10, pady=5)

#bouton importattion argile sableux
boutton_as = Button(cadre_boutons, text="Argile sableux",command=executer_argile_sableux)
boutton_as.pack(anchor="w", padx=10, pady=5)

#bouton importattion generique
boutton_el = Button(cadre_boutons, text="Generique",command=executer_generique)
boutton_el.pack(anchor="w", padx=10, pady=5)


#bouton importattion valeurs perso
boutton_pers= Button(cadre_boutons, text="valeurs précises",command=executer_perso)
boutton_pers.pack(anchor="w", padx=10, pady=(15,5))
#Indication zone de texte valeurs perso
valeurs_perso_label = tk.Label(cadre_boutons, text=" Alpha     Beta",width=12, height=1)
valeurs_perso_label.pack(anchor="w", padx=10, pady=0)
#Zone de texte pour entrer valeurs perso
valeur_alpha = tk.Entry(cadre_boutons,width=3) #height=1
valeur_alpha.pack(side="left",ipadx=4, padx=(25,0), pady=(5,0))
valeur_beta = tk.Entry(cadre_boutons, width=3)
valeur_beta.pack(side="left", ipadx=4, padx=(10,0), pady=(5,0))



#état de la modification
resultat_label=tk.Label(cadre_boutons,text="etat : ")
resultat_label.pack(anchor="w",padx=90,pady=0)



canvas_image = None
# Chargement de l'image du triangle des sols
img = Image.open("imgl.png")
def affiche_image():
    global img, canvas_image, lignes
    img = img.resize((300, 300), Image.LANCZOS) #LANCZOS plutot que ANTIALIAS, car ANTIALIAS est bientot plus supporté
    img = ImageTk.PhotoImage(img)
    # Création du canevas pour afficher l'image
    if canvas_image != None:
        canvas_image.destroy()
    canvas_image = tk.Canvas(cadre_image, width=300, height=300, highlightthickness=0)
    canvas_image.pack(side="top")
    canvas_image.create_image(0, 0, anchor=tk.NW, image=img)
affiche_image()


#Bouton de preview du nouveau fichier excel 
button_pre = Button(fenetre, text="Afficher les valeurs", command=afficher)
button_pre.pack()


#zone de texte preview
text_pre = tk.Text(fenetre, width=largeur//3, height=hauteur//3, wrap="none")
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


# coucou :)

#Pour toutes questions :

#logan.doceul@student.junia.com
#evann.semens@...
#henri.oms@...
#vincent.damery@...

#Pour acceder au Github du projet :
# https://github.com/ServaLJaycE/Projet-CNB2-S2



