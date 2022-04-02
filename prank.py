from pynput.keyboard import Key, Controller
kb = Controller()
import time
x = int(input("Pick your choice of spam: \n 1. HAPPY APRIL FOOLS \n 2. You Got Jebaited! \n 3. Classic Navy Seal Copypasta \n 4. BAKA \n 5. Blackpink! \n 6. TRUMP's SPEECH \n 7. Grandfather \n 8. Prego Copypasta \n 9. NAvy Seal Part 2 \n 10. Darth Plagueis The Wise \n 100. Test Script \n \n"))
if (x == 1):
    file = open('HAPPY APRIL FOOLS.txt', 'r')
if (x == 2):
    file = open('You Got Jebaited!.txt', 'r')
if (x == 3):
    file = open('NavySeal Copypasta (NSFW).txt', 'r')
if (x == 4):
    file = open('baka.txt', 'r')
if (x == 5):
    file = open('blackpink.txt', 'r')
if (x == 6):
    file = open('Donald Trump.txt', 'r')
if (x == 7):
    file = open('Grandfather.txt', 'r')
if (x == 8):
    file = open('prego copypasta.txt', 'r')
if (x == 9):
    file = open('NavySeal Pt 2.txt', 'r')
if (x == 10):
    file = open('Darth Plagueis.txt', 'r')
if (x == 100):
    file = open('Test Script.txt', 'r')

# Customise your own spam messages and save it as a txt file (and continue the list of choices)! Note that spam messages will be sent one at a time!

print ("Spambot runs in... \n")  #For countdown
count = 10
while (count > 0):
    time.sleep(1)
    print (count)
    count = count - 1
    if (count == 3):
        print("\tHave Fun!")


while (True):      #loop for continuous spamming
    char = file.read(1) #reads file, returns specified number of bytes from the file, in this case it reads 1 byte (1 char)
    
    def type_string(string): #Defining a function
        for char in string:  #Loop over each character within the string (word)
            kb.type(char)    #Type each character one by one
    
    type_string(char) #Function Call

    if (char == " "):  #if char is a space (in between the words in the spam file)
        kb.press(Key.enter) #press enter key (allowing it to send and actually make spam)
        time.sleep(0.3)  #Time taken between each spam word/after every 'enter'
    
    #time.sleep(0.3)  #Put the time.sleep here instead if you want each letter to type slowly

    if not char: #if there are no more messages left to send, exit loop and proceed to close file
        kb.press(Key.enter) #final enter key to send the last message
        break
    
file.close()
