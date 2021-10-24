import keyboard
import pyperclip
import csv
import time

shortcut = 'a+w' #If you want to change the shortcut, just replace "a + w" with your favorite pair.

#This function adds the word from your clipboard to vocab.csv.
def add_word(save_content):
            vocab_csv = open('vocab.csv', 'a+')
            csv_reader = csv.reader(vocab_csv)
            print('"'+save_content+'"', 'was added.')
            vocab_csv.write(save_content+'\n')
            vocab_csv.close()
            

# This one detects if you already have the word in the csv.
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
                
        return word_in_file
       

  
print('Welcome to the add vocabulary script.')
print('Steps:\n1)Copy the word that you don´t know. \n2) press the keys "'+shortcut+'" simultaneously. \nReady! this will add the word in a csv file')
print('Dont worry about duplicates. The script can detect them.')

while True:
    keyboard.wait(shortcut)
    try:
        if keyboard.is_pressed(shortcut): 
            save_content = str(pyperclip.paste()).title()
            if check_is_in_file(save_content) == False:
                add_word(save_content)

            
    except Exception as e:
        print(e)




            


