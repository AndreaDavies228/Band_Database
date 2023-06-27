from queries import *

def set_language():
    language = False
    while language == False:
        value = input("Please select a language: English / Deutsch ")
        if value == "English" or value == "english" or value == "Englisch" or value == "englisch" or value == "E" or value == "e":
            print("You have selected English.")
            language = "E"
            return language
        elif value == "Deutsch" or value == "deutsch" or value == "German" or value == "german" or value == "D" or value == "d":
            print("This database does not support German yet. Come back later.")
            #language = "D"
            #return language
            exit()
        else:
            print("Please select either English or German. Bitte Englisch oder Deutsch wählen.")

def selection():
    selection = False
    while selection == False:
        #if language == "E":
        value = input("Would you like to add an entry, update an entry, or search the database? Please press 'A', 'U', or 'S'. ")
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

def add():
    value = input("Would you like to add a band or a band member? ")
    if value == "band" or value == "Band" or value == "b" or value == "B":
        band_name = input("Please enter the name of the band. ")
        ideology = input("Please enter the ideology of the band. ")
        logo = input("Please enter a URL link to the band's logo. If you don't have a link please enter 'None'. ")
        print("Now accessing the database, please wait.")
        if logo == "none" or logo == "None" or logo == "n" or logo == "N":
            add_band(band_name, ideology)
        else:
            add_band(band_name, ideology, logo)
    
        value2 = input("Would you also like to add band members for this band?")
        if value2 == "Yes" or value2 == "yes" or value2 == "Y" or value2 == "y":
            name = input("Please enter the name of the band member. ")
            ideology = input("Please enter the ideology of the band member. If you don't know please enter 'None'. ")
            join_year = input("Please enter the year they joined the band. If you don't know please enter 'None'. ")
            leave_year = input("Please enter the year they left the band. If you don't know please enter 'None'. ")
            if ideology == "none" or ideology == "None" or ideology == "n" or ideology == "N":
                ideology = "NULL"
            if join_year == "none" or join_year == "None" or join_year == "n" or join_year == "N":
                join_year = "NULL"
            if leave_year == "none" or leave_year == "None" or leave_year == "n" or leave_year == "N":
                leave_year = "NULL"
            add_member(name, band_name, ideology, join_year, leave_year)
            print(f"You have added {name}.")

    if value.lower() == "member" or value.lower() == "band member" or value.lower() == "m":
        name = input("Please enter the name of the band member. ")
        band_name = input("Please enter the name of the band they belong to. ")
        ideology = input("Please enter the ideology of the band member. If you don't know please enter 'None'. ")
        join_year = input("Please enter the year they joined the band. If you don't know please enter 'None'. ")
        leave_year = input("Please enter the year they left the band. If you don't know please enter 'None'. ")
        if ideology == "none" or ideology == "None" or ideology == "n" or ideology == "N":
            ideology = "NULL"
        if join_year == "none" or join_year == "None" or join_year == "n" or join_year == "N":
            join_year = "NULL"
        if leave_year == "none" or leave_year == "None" or leave_year == "n" or leave_year == "N":
            leave_year = "NULL"
        add_member(name, band_name, ideology, join_year, leave_year)
        

def update():
    pass

def search():
    pass