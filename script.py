from openpyxl import load_workbook
from tkinter import * 
from tkinter.filedialog import *


#Toutes les fonctions :
#Fonction pour modifier le excel
def import_excel():
    #on charge le fichier excel
    ##nom_fichier = texte.get("1.0", "end-1c")
    ##nom_fichier = nom_fichier + ".xlsx"
    ##workbook = load_workbook(filename=nom_fichier)
    files = askopenfilename(title="Ouvrir un fichier",filetypes=[('xlsx files','.xlsx')])
    return files
   
def calcul_terre(files):
     workbook = load_workbook(filename=files)
     #on ouvre le fichier excel
     sheet = workbook.active
     #on modifie la cellule A1
     sheet["A1"] = "ca change"
     #on sauvegarde le fichier
     workbook.save(filename="value.xlsx")
    
    
# Fonction pour changer le theme
def toggle():
    global switch_value
    if switch_value == True:
        switch.config(image=dark, bg="#26242f",
                      activebackground="#26242f")
        switch_value = False
        #met la fenetre en noir
        fenetre.config(bg="#26242f") 
        
        #suprime le label deja existant
        #a ajouter
        label=Label(fenetre, text="Bienvenue dans S-EAU-L", bg="#26242f", fg="white")
        label.pack()
        
  
    else:
        switch.config(image=light, bg="white", 
                      activebackground="white")
        switch_value = True  
        #met la fenetre en blanc
        fenetre.config(bg="white") 
    
        #suprime le label deja existant
        #a ajouter       
        label=Label(fenetre, text="Bienvenue dans S-EAU-L", bg="white", fg="black")
        label.pack()
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
label = Label(fenetre, text="Bienvenue dans S-EAU-L", bg="white", fg="black")
label.pack()

#zone de texte
##texte = Text(fenetre, width=largeur, height=hauteur)
#on definit la taille de la zone de texte
##texte.config(width=15, height=1)
##texte.pack()
#on pre-ecrit du texte dans la zone de texte
##texte.insert(END, "nom du fichier")



#bouton qui lance l'importation seulement quand on appuie dessus
boutton = Button(fenetre, text="Importer", command=import_excel)
boutton.pack()

#titre
label = Label(fenetre, text="Selectionez votre type de sol", bg="white", fg="black")
label.pack(anchor="w", padx=10, pady=20)

#bouton importattion terre
boutton_t = Button(fenetre, text="terre", command=calcul_terre(import_excel()))
boutton_t.pack(anchor="w", padx=10, pady=5)

#bouton importattion eau
boutton_e = Button(fenetre, text="eau"  )
boutton_e.pack(anchor="w", padx=10, pady=5)

#bouton importattion air
boutton_a = Button(fenetre, text="air")
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


