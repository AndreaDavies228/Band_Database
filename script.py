while language == False:
  value = input("Welcome to the band database. Please select a language: English / Deutsch")
  if value == "English" or value == "english" or value == "Englisch" or value == "englisch" or value == "E" or value == "e":
    language = "E"
    print("You have selected English.")
  elif value == "Deutsch" or value == "deutsch" or value == "German" or value == "german" or value == "D" or vale == "d":
    language = "D"
    print("This database does not support German yet. Come back later.)
    exit()
  else:
    print("Please select either English or German. Bitte Englisch oder Deutsch wählen.")

 while selection == False:
  if langauge == "E":
    value = input("Would you like to add an entry, update an entry, or search the database? Please press 'A', 'U', or 'S'.)
    if value == "A" or value == "a" or value == "Add" or value == "add":
                  selection = "A"
                  print("You have selected 'Add'.)
    if value == "U" or value == "u" or value == "Update" or value == "update":
                        selection = "U"
                        print("You have selected 'Update'.)
    if value == "S" or value == "s" or value == "Search" or value == "s":
                              selection = "S"
                              print("You have selected 'Search'.)
    else:
                                    print("Invalid input. Please select Add, Update or Search.")
                                    
if selection == "A":
                                    add()
                                    
if selection == "U":
                                    update()
if selection == "S":
                                    search()

print("Thank you for using the band database")
                                    exit()
                                    
                                    
   
