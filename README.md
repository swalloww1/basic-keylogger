# basic-keylogger

enregistrement des saisies clavier développé en Python à l'aide de la bibliothèque pynput.

-fonctionalité:

  Capture en Temps Réel : Écoute continue des événements clavier via un Listener permettant d'intercepter chaque touche pressée par l'utilisateur.

  Distinction des Touches : Différenciation automatique entre les caractères alphanumériques standards et les touches spéciales (Espace, Entrée, Maj, etc.), encadrées entre crochets dans le journal.

  Horodatage des Événements : Ajout dynamique de la date et de l'heure exactes (AAAA-MM-JJ HH:MM:SS) lors de l'utilisation de touches spéciales.

  Journalisation et Export : Sauvegarde brute des entrées en continu dans un fichier texte (keylog.txt) et fonction de conversion structurée vers le format JSON (keylog.json).   
  main.py

-Technique

  Langage : Python 3

  Bibliothèque de contrôle : pynput

  Modules natifs : datetime, json et os
