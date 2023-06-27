def set_language():
    language = False
    while language == False:
        value = input("Welcome to the band database. Please select a language: English / Deutsch")
        if value == "English" or value == "english" or value == "Englisch" or value == "englisch" or value == "E" or value == "e":
            print("You have selected English.")
            language = "E"
            return language
        elif value == "Deutsch" or value == "deutsch" or value == "German" or value == "german" or value == "D" or value == "d":
            print("This database does not support German yet. Come back later.")
            language = "D"
            return language
            exit()
        else:
            print("Please select either English or German. Bitte Englisch oder Deutsch wählen.")

def selection(language):
    selection = False
    while selection == False:
        if language == "E":
            value = input("Would you like to add an entry, update an entry, or search the database? Please press 'A', 'U', or 'S'.")
            if value == "A" or value == "a" or value == "Add" or value == "add":
                selection = "A"
                print("You have selected 'Add'.")
                return selection
            if value == "U" or value == "u" or value == "Update" or value == "update":
                selection = "U"
                print("You have selected 'Update'.")
                return selection
            if value == "S" or value == "s" or value == "Search" or value == "s":
                selection = "S"
                print("You have selected 'Search'.")
                return selection
            if value == "Q" or value == "q" or value == "Quit" or value == 'quit':
                print("Thank you for using the band database. We hope to see you again soon.")
                exit()
            else:
                print("Invalid input. Please select Add, Update, Search or Quit.")

