def main():
    fname = input ("Enter a file name: ") 
    fopner = open(fname) # Brukeren beskriver en fil og python åpner filen

    print ("Enter 1 if you want to find the line number")
    print ("Enter 2 if you want to know the amount of matches")
    UserInput = input("Enter a number: ")
    if UserInput == "1":
        LineNumber()
    elif UserInput == "2":
        MatchCount()
    else:
        print ("Invalid input. Please enter 1 or 2.")
        main()
    
    def LineNumber():
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
                        print ("It is a",'"' + content + '"', "at line number", line_number, "at position", words.index(word), "from", fname)
    def MatchCount():
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
                        print("There was", count, '"' + content + '"', "in the file")
main()

restart = input ("Do you want to seach again? (y/n): ")
if restart == "y":
    main()
else:
    exit()

main()