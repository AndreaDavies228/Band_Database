from queries import *

def selection():
    selection = False
    while selection == False:
        value = input("Would you like to add an entry, update an entry, or search the database? Please press 'A', 'U', or 'S'. Press 'Q' to quit. ")
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
    value = input("Would you like to add a band or a band member? Press 'C' to cancel. ")
    if value == "band" or value == "Band" or value == "b" or value == "B":
        band_name = input("Please enter the name of the band. ")
        ideology = input("Please enter the ideology of the band. ")
        logo = input("Please enter a URL link to the band's logo. If you don't have a link please enter 'None'. ")
        print("Now accessing the database, please wait.")
        if logo == "none" or logo == "None" or logo == "n" or logo == "N":
            print("Now accessing the database, please wait...")
            add_band(band_name, ideology)
        else:
            print("Now accessing the database, please wait...")
            add_band(band_name, ideology, logo)
    
        value2 = input("Would you also like to add band members for this band? ")
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
            print("Now accessing the database, please wait...")
            add_member(name, band_name, ideology, join_year, leave_year)
        else:
            return    

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
        print("Now accessing the database, please wait...")
        add_member(name, band_name, ideology, join_year, leave_year)
    
    else:
        return
        

def update():
    value = input("Would you like to update a band or a band member? Press 'C' to cancel. ")

    if value.lower() == "band" or "b":
        band_name = input("Please enter the name of the band you want to update. ")
        while True:
            check = name_check(band_name)
            if check == True:
                break
            else:
                band_name = input("This band isn't in the database. Check your spelling and enter it again. Press Q to quit. ")
                if band_name.lower() == "q" or band_name.lower() == "quit":
                    return
                else:
                    continue

        value = input("Would you like to delete the band, or update band information. Press 'D' or 'U'. ")
        if value.lower() == "delete" or "d":
            print("Now accessing the database, please wait...")
            update_function(type="delete_band", band_name=band_name)
        
        if value.lower() == "update" or "u":
            value = input("Would you like to update the band name, ideology or logo?" )
            if value.lower() == "band name" or value.lower() == "name" or value.lower() == "n":
                new_band_name = input("Please enter the new band name. ")
                print("Now accessing the database, please wait...")
                update_function(type="update_band_name", band_name=band_name, new_band_name=new_band_name)

            if value.lower() == "ideology" or value.lower() == "i":
                ideology = input("Please enter the new band ideology. ")
                print("Now accessing the database, please wait...")
                update_function(type="update_band_ideology", band_name=band_name, ideology=ideology)

            if value.lower() == "logo" or value.lower() == "l":
                logo = input("Please enter the new link to the band logo. ")
                print("Now accessing the database, please wait...")
                update_function(type="update_band_logo", band_name=band_name, logo=logo)

            else:
                return               


        else:
            return


    if value.lower() == "member" or value.lower == "b" or value.lower() == "band member":
    
        member_name = input("Please enter the name of the member name you want to update. ")
        while True:
            check = name_check(member_name)
            if check == True:
                break
            else:
                member_name = input("This band member isn't in the database. Check your spelling and enter it again. Press Q to quit. ")
                if member_name.lower() == "q" or member_name.lower() == "quit":
                    return
                else:
                    continue      
        
        
        value = input("Would you like to delete the band member, or update band member information. Press 'D' or 'U'. ")  
        if value.lower() == "delete" or "d":
            print("Now accessing the database, please wait...")
            update_function(type="delete_member", member_name=member_name)
        
        if value.lower() == "update" or "u":
            value = input("Would you like to update the member name, ideology or band membership? ")
            if value.lower() == "member name" or value.lower() == "name" or value.lower() == "n":
                new_member_name = input("Please enter the new name of the member. ")
                print("Now accessing the database, please wait...")
                update_function(type="update_member_name", member_name=member_name, new_member_name=new_member_name)
                return

            if value.lower() == "ideology" or value.lower() == "i":
                ideology = input("Please enter the new ideology of the member. ")
                print("Now accessing the database, please wait...")
                update_function(type="update_member_ideology", member_name=member_name, ideology=ideology)
                return

            if value.lower() == "band membership" or value.lower() == "membership" or value.lower() == "b" or value.lower() == "band" or value.lower() == "m":
                value = input("Would you like to remove band membership('remove'), add band membership('add'), change the year they joined a band ('joined'), or the year they left a band ('left')? ")
                band_name = input("Please enter the name of the band. ")
                if value.lower() == "add" or value.lower() == "add band membership" or value.lower() == "a":
                    print("Now accessing the database, please wait...")
                    update_function(type="add_member_band_membership", member_name=member_name, band_name=band_name)
                    return
                
                
                while True:
                    check = name_check(band_name)
                    if check == True:
                        break
                    else:
                        band_name = input("This band isn't in the database. Check your spelling and enter it again. Press Q to quit. ")
                        if band_name.lower() == "q" or band_name.lower() == "quit":
                            return
                        else:
                            continue
                if value.lower() == "remove" or value.lower() == "remove band membership" or value.lower() == "r":
                    print("Now accessing the database, please wait...")
                    update_function(type="remove_member_band_membership", member_name=member_name, band_name=band_name)

                if value.lower() == "joined" or value.lower() == "join" or value.lower() == "j" or value.lower() == "year joined":
                    joined = input("Please enter the new year that they joined the band. ")
                    print("Now accessing the database, please wait...")
                    update_function(type="update_joined_year", member_name=member_name, band_name=band_name, joined=joined)

                if value.lower() == "left" or value.lower() == "leave" or value.lower() == "l" or value.lower() == "year left":
                    left = input("Please enter the new year that they left the band. ")
                    print("Now accessing the database, please wait...")
                    update_function(type="update_left_year", member_name=member_name, band_name=band_name, left=left)
                else:
                    return

            else:
                return 

        else:
            return

    else:
        return
def search():
    pass