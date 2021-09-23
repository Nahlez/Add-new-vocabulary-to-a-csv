import keyboard
import pyperclip
import csv
import time

def check_is_in_file(save_content):
    with open('vocab.csv','r+') as vocab_csv:
        reader = csv.reader(vocab_csv, delimiter=';')
        
        word_in_file = False
        
        for row in reader:
            if save_content in row[0]:
                word_in_file = True              
                print(word_in_file)
                break
                
            else: 
                pass
        return word_in_file
       
def add_word(save_content):
            vocab_csv = open('vocab.csv', 'a+')
            csv_reader = csv.reader(vocab_csv)
            print('"'+save_content+'"', 'was added.')
            vocab_csv.write(save_content+'\n')
            vocab_csv.close()
            time.sleep(0.1)


shortcut = 'a+w' #If you want to change the shortcut just replace "c+w" for your pair of  favourite letters
#try:
save_content = str(pyperclip.paste()).title()
if check_is_in_file(save_content) == False:
    add_word(save_content)

            
#except Exception as e:
    print(e)

input()



            

# No añadir duplicados
# Not i did this way because it can works with any text in your laptop. Check if it works in linux

