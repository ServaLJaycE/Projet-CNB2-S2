from openpyxl import load_workbook
from tkinter import * 
from tkinter.filedialog import *
import tkinter as tk





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
def executer_air():
     donnees_importees = import_excel()
     calcul_air(donnees_importees)
     resultat="fin"
     resultat_label.configure(text="état : " + str(resultat))


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
        label_select.config(bg="#26242f", fg="white")
        label_select.pack()
        resultat_label.config(bg="#26242f", fg="white")
        resultat_label.pack()
        text_pre.config(bg="grey15", fg="white")
        text_pre.pack()
    else:
        switch.config(image=light, bg="white", 
                      activebackground="white")
        switch_value = True  
        #met la fenetre en blanc
        fenetre.config(bg="white") 
        #modifie couleur des textes
        label_titre.config(bg="white", fg="black")
        label_titre.pack()
        label_select.config(bg="white", fg="black")
        label_select.pack()
        resultat_label.config(bg="white", fg="black")
        resultat_label.pack()
        text_pre.config(bg="white", fg="black")
        text_pre.pack()





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


#zone de texte
##texte = Text(fenetre, width=largeur, height=hauteur)
#on definit la taille de la zone de texte
##texte.config(width=15, height=1)
##texte.pack()
#on pre-ecrit du texte dans la zone de texte
##texte.insert(END, "nom du fichier")

#bouton qui lance l'importation seulement quand on appuie dessus
#boutton = Button(fenetre, text="Importer", command=import_excel)
#boutton.pack()
 

#titre
label_select = Label(fenetre, text="Selectionez votre type de sol :", bg="white", fg="black")
label_select.pack(anchor="w", padx=10, pady=20)


#bouton importattion terre
boutton_t = Button(fenetre, text="terre", command=executer_terre)
boutton_t.pack(anchor="w", padx=10, pady=5)

#bouton importattion eau
boutton_e = Button(fenetre, text="eau", command=executer_eau )
boutton_e.pack(anchor="w", padx=10, pady=5)

#bouton importattion air
boutton_a = Button(fenetre, text="air",command=executer_air)
boutton_a.pack(anchor="w", padx=10, pady=5)

#bouton importattion feu
boutton_f = Button(fenetre, text="feu")
boutton_f.pack(anchor="w", padx=10, pady=5)

#bouton importattion electrique
boutton_el = Button(fenetre, text="electrique")
boutton_el.pack(anchor="w", padx=10, pady=5)

#bouton importattion poison
boutton_po = Button(fenetre, text="poison")
boutton_po.pack(anchor="w", padx=10, pady=5)


#état de la modification
resultat_label = tk.Label(fenetre, text="état : ")
resultat_label.pack(anchor="w", padx=90, pady=20)


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


