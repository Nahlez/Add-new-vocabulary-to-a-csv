import keyboard
import pyperclip
import csv
import time

shortcut = 'c+w' #If you want to change the shortcut just replace "c+w" for your pair of  favourite letters

while True:
    try:
        if keyboard.is_pressed(shortcut): # c + w come from "copy word"
            save_content = str(pyperclip.paste()).title()
            vocab_csv = open('vocab.csv', 'a+')
            print('"'+save_content+'"', 'was added.')
            vocab_csv.write(save_content+'\n')
            vocab_csv.close()
            time.sleep(0.1)
    except Exception as e:
        print(e)

        
            

# No añadir duplicados
# Not i did this way because it can works with any text in your laptop. Check if it works in linux
