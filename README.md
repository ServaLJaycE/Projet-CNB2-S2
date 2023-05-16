# Projet CNB2 S2
 Projet du 2eme semestre de l'année CNB2
 
 Ce code permet de transformer les valeurs csv renvoyés par les sondes hydroscout en volt, en valeur plus compréhensible (Pourcentage d'eau).
Il y est compris :

-Une zone pour connaitre son type de sol (identification via le triangle des sols et les pourcentage de grain).

-Une zone de choix de son type de sol qui entrainera le selection du fichier csv a modifié.

-Une zone de preview du resultat du fichier csv, et la création de bouton pour chaque différents site, qui nous montre, chacun un graphe du pourcentage d'eau, en moyenne selon la profondeur du site en question.


Le csv d'origine ne sera pas modifié, il sera a la place créée un nouveau fichier ("neww.csv"), qui lui sera identique, a l'exception que chaque colonne "Hygro_", aura maintenant une voisine "HygroTrue_", contenant les valeurs en pourcentages.

Voici l'application en mode dark, avec la zone de determination des sols utilisé et un fichier modifié puis montré dans la zone preview :
![image](https://github.com/ServaLJaycE/Projet-CNB2-S2/assets/105350341/586bb18a-69ef-400c-b80b-aa89c268c17c)



Voici l'application, en mode light (mode par default, qui est switchable avec le bouton en haut a droite) :
![image](https://github.com/ServaLJaycE/Projet-CNB2-S2/assets/105350341/5654f1e0-616b-4f30-a674-46b448d7146f)







