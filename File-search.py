fname = input ("Enter a file name: ") 
fopner = open(fname) # Brukeren skirver en input fil og python åpner filen
count = 0
line_number = 0

content = input ("Enter the content you want to find: ")
for line in fopner:
    line_number += 1
    words = line.split()
    if content in line: # Når linjen med det brukeren skrev matcher
        count += 1
        ()
        for word in words:
            if word == content:
                print ("It is a",'"' + content + '"', "at line number", line_number, "at position", words.index(word) + 1, "from", fname)
print("There was", count, '"' + content + '"', "in the file")
input ("press enter to continue...")