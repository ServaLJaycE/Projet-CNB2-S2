# Projet CNB2 S2
 Projet du 2eme semestre de l'année CNB2
 
 Ce code permet de transformer les valeurs csv renvoyés par les sondes hydroscout en volt, en valeur plus compréhensible (Pourcentage d'eau).
Il ya est compris :
-Une zone pour connaitre son type de sol (identification via le triangle des sols et les pourcentage de grain).
-Une zone de choix de son type de sol qui entrainera le selection du fichier csv a modifié.
-Une zone de preview du resultat du fichier csv, avec affichage des graphes du pourcentage d'eau, selon le temp.

Le csv d'origine ne sera pas modifié, il sera a la place créée un nouveau fichier ("neww.csv"), qui lui sera identique, a l'exception que chaque colonne "Hygro_", aura maintenant une voisine "HygroTrue_", contenant les valeurs en pourcentages.


![image](https://user-images.githubusercontent.com/105350341/236453847-491aacc2-8d70-4e81-a4d0-77971cb1c7b1.png)

