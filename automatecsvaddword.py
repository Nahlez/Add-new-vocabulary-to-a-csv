import keyboard
import pyperclip
import csv
import time

while True:
    time.sleep(0.1)
    if keyboard.is_pressed('a+w'): #a + w come from "add word"
        time.sleep(0.1)
        save_content = str(pyperclip.paste())
        vocab_csv = open('vocab.csv', 'a+')
        print('The word',save_content, 'was added')
        vocab_csv.write(save_content.title()+'\n')
        vocab_csv.close()
    
    else:
        continue

# No añadir duplicados