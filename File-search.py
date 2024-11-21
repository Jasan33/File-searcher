def start():
    print ("welcome to the word searcher")
    print ("Make sure that your file and this scri2 is in the same directory")
    print ("Option 1: Tells you the cordinates of the word(s)")
    print ("Option 2: shows you the amount of maches of the word(s)")
    meny = input("choose option 1 or 2: ")
    options(meny)

def options(number):
    if number == "1":
        find_word_cordinates()
    elif number == "2":
        find_word_amount()
    else:
        print ("Invalid option. Please choose 1 or 2.")
        start()
    


def find_word_cordinates():
    fname = input ("Enter a file name: ") 
    fopner = open(fname) # Brukeren beskriver en fil og python åpner filen
    count = 0
    line_number = 0

    content = input ("Enter the content you want to find: ")
    for line in fopner: # for vær linje i filen
        line_number += 1
        words = line.split() # splitter alle ordene per linje
        if content in line: # Når python finner ordet
            ()
            for word in words: # for alle ord i ord-linjen
                if word == content:
                    count += 1
                    print ("It is a",'"' + content + '"', "at line number", line_number, "after", words.index(word) + 1, "words from the start line")

def find_word_amount():
    fname = input ("Enter a file name: ") 
    fopner = open(fname)
    count = 0
    line_number = 0

    content = input ("Enter the content you want to find: ")
    for line in fopner:
        line_number += 1
        words = line.split()
        if content in line:
            ()
            for word in words:
                if word == content:
                    count += 1
    print ("There is", count,'"' + content + '"', "in this file")

start()
restart = input ("Do you want to seach again? (y/n): ")
if restart == "y":
    start()
else:
    exit() # avslutter 