from openpyxl import load_workbook
from tkinter import * 



#Toutes les fonctions :
# Fonction pour modifier le excel
def import_excel():
    #on demande un nom de fichier dans la fenetre
    #nom_fichier = input("Quel est le nom du fichier ?")
    #on import le fichier excel
    workbook = load_workbook(filename="test.xlsx")
    #on ouvre le fichier excel
    sheet = workbook.active
    #on modifie la cellule A1
    sheet["A1"] = "ca change"
    #on sauvegarde le fichier
    workbook.save(filename="test.xlsx")

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

#bouton de prise de données
boutton = Button(fenetre, text="importer vos données", command=import_excel)
boutton.place(x=200, y=200)
boutton.pack()


  

  
  
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


