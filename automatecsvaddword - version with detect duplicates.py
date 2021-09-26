import keyboard
import pyperclip
import csv
import time

shortcut = 'a+w' #If you want to change the shortcut just replace "c+w" for your pair favourite.

#This fuction adds the word from your clipboard to the csv
def add_word(save_content):
            vocab_csv = open('vocab.csv', 'a+')
            csv_reader = csv.reader(vocab_csv)
            print('"'+save_content+'"', 'was added.')
            vocab_csv.write(save_content+'\n')
            vocab_csv.close()
            

# This one  detects if you already have the word in the csv.
def check_is_in_file(save_content):
    with open('vocab.csv','r+') as vocab_csv:
        reader = csv.reader(vocab_csv, delimiter=';')
        
        word_in_file = False
        
        for row in reader:
            if save_content in row[0]:
                word_in_file = True
                time.sleep(0.1)              
                print('"'+save_content+'"', 'has not been added because it was already in the file.')
                break
                
            else: 
                pass
        return word_in_file
       

  
while True:
    try:
        if keyboard.is_pressed(shortcut):
            time.sleep(0.1) 
            save_content = str(pyperclip.paste()).title()
            if check_is_in_file(save_content) == False:
                add_word(save_content)

            
    except Exception as e:
        print(e)

input()



            

# No añadir duplicados
# Not i did this way because it can works with any text in your laptop. Check if it works in linux
