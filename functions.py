from queries import *

def selection():
    selection = False
    while selection == False:
        value = input("\nWould you like to add an entry, update an entry, or search the database? Please press 'A', 'U', or 'S'. Press 'Q' to quit. ")
        if value == "A" or value == "a" or value == "Add" or value == "add":
            selection = "A"
            print("\nYou have selected 'Add'.")
            return selection
        if value == "U" or value == "u" or value == "Update" or value == "update":
            selection = "U"
            print("\nYou have selected 'Update'.")
            return selection
        if value == "S" or value == "s" or value == "Search" or value == "s":
            selection = "S"
            print("\nYou have selected 'Search'.")
            return selection
        if value == "Q" or value == "q" or value == "Quit" or value == 'quit':
            print("\nThank you for using the band database. We hope to see you again soon.")
            exit()
        else:
            print("Invalid input. Please select Add, Update, Search or Quit.")

def add():
    value = input("Would you like to add a band or a band member? Press 'C' to cancel. ")
    if value == "band" or value == "Band" or value == "b" or value == "B":
        band_name = input("\nPlease enter the name of the band. ")
        ideology = input("Please enter the ideology of the band. ")
        logo = input("Please enter a URL link to the band's logo. If you don't have a link please enter 'None'. ")
        while True:
            confirm = input(f"\n{band_name.title()} with ideology {ideology.title()} will be added with logo: {logo}. Press 'Y' to confirm and 'N' to cancel. ")
            if confirm.lower() == "y" or confirm.lower() == "yes":
                print("\nNow accessing the database, please wait.")
                if logo == "none" or logo == "None" or logo == "n" or logo == "N":
                    add_band(band_name, ideology)
                    break
                else:
                    add_band(band_name, ideology, logo)
                    break
            if confirm.lower() == "n" or confirm.lower() == "no":
                return
            else:
                print("Invalid input. Enter 'Y' or 'N' to confirm or cancel.")
                continue
    
        value2 = input("\nWould you also like to add band members for this band? ")
        if value2 == "Yes" or value2 == "yes" or value2 == "Y" or value2 == "y":
            while True:
                name = input("\nPlease enter the name of the band member. ")
                ideology = input("Please enter the ideology of the band member. If you don't know please enter 'None'. ")
                join_year = input("Please enter the year they joined the band. If you don't know please enter 'None'. ")
                leave_year = input("Please enter the year they left the band. If you don't know please enter 'None'. ")
                while True:
                    confirm = input(f"\n{name.title()} with ideology {ideology.title()} will be added as a member of {band_name.title()}, with join year: {join_year} and leave year: {leave_year}. Press 'Y' to confirm and 'N' to cancel. ")
                    if confirm.lower() == "y" or confirm.lower() == "yes":
                        if ideology == "none" or ideology == "None" or ideology == "n" or ideology == "N":
                            ideology = "NULL"
                        if join_year == "none" or join_year == "None" or join_year == "n" or join_year == "N":
                            join_year = "NULL"
                        if leave_year == "none" or leave_year == "None" or leave_year == "n" or leave_year == "N":
                            leave_year = "NULL"
                        print("\nNow accessing the database, please wait...\n")
                        add_member(name, band_name, ideology, join_year, leave_year)
                        break
                    if confirm.lower() == "n" or confirm.lower() == "no":
                        break
                    else:
                        print("Invalid input. Enter 'Y' or 'N' to confirm or cancel.")
                        continue
                more = input("\nWould you like to enter another band member?")
                if more.lower() == "y" or more.lower() == "yes":
                    continue
                else:
                    break
                
        else:
            return    

    if value.lower() == "member" or value.lower() == "band member" or value.lower() == "m":
        name = input("\nPlease enter the name of the band member. ")
        band_name = input("Please enter the name of the band they belong to. ")
        ideology = input("Please enter the ideology of the band member. If you don't know please enter 'None'. ")
        join_year = input("Please enter the year they joined the band. If you don't know please enter 'None'. ")
        leave_year = input("Please enter the year they left the band. If you don't know please enter 'None'. ")
        while True:
            confirm = input(f"\n{name.title()} with ideology {ideology.title()} will be added as a member of {band_name.title()}, with join year: {join_year} and leave year: {leave_year}. Press 'Y' to confirm and 'N' to cancel. ")
            if confirm.lower() == "y" or confirm.lower() == "yes":
                if ideology == "none" or ideology == "None" or ideology == "n" or ideology == "N":
                    ideology = "NULL"
                if join_year == "none" or join_year == "None" or join_year == "n" or join_year == "N":
                    join_year = "NULL"
                if leave_year == "none" or leave_year == "None" or leave_year == "n" or leave_year == "N":
                    leave_year = "NULL"
                print("\nNow accessing the database, please wait...\n")
                add_member(name, band_name, ideology, join_year, leave_year)
                break
            if confirm.lower() == "n" or confirm.lower() == "no":
                return
            else:
                print("Invalid input. Enter 'Y' or 'N' to confirm or cancel.")
                continue
    
    else:
        print("Invalid input. Cancelling...")
        return
        

def update():
    value1 = input("Would you like to update a band or a band member? Press 'C' to cancel. ")

    if value1.lower() == "band" or value1.lower() == "b":
        band_name = input("\nPlease enter the name of the band you want to update. ")
        while True:
            check = name_check("band", band_name)
            if check == True:
                break
            else:
                band_name = input("This band isn't in the database. Check your spelling and enter it again. Press Q to quit. ")
                if band_name.lower() == "q" or band_name.lower() == "quit":
                    return
                else:
                    continue

        value = input("Would you like to delete the band, or update band information. Press 'D' or 'U'. ")
        if value.lower() == "delete" or value.lower() == "d":
            print("\nNow accessing the database, please wait...\n")
            update_function(type="delete_band", band_name=band_name)
            return
        
        if value.lower() == "update" or value.lower() == "u":
            value = input("Would you like to update the band name, ideology or logo? " )
            if value.lower() == "band name" or value.lower() == "name" or value.lower() == "n":
                new_band_name = input("\nPlease enter the new band name. ")
                print("\nNow accessing the database, please wait...\n")
                update_function(type="update_band_name", band_name=band_name, new_band_name=new_band_name)
                return

            if value.lower() == "ideology" or value.lower() == "i":
                ideology = input("\nPlease enter the new band ideology. ")
                print("\nNow accessing the database, please wait...\n")
                update_function(type="update_band_ideology", band_name=band_name, ideology=ideology)
                return

            if value.lower() == "logo" or value.lower() == "l":
                logo = input("\nPlease enter the new link to the band logo. ")
                print("\nNow accessing the database, please wait...\n")
                update_function(type="update_band_logo", band_name=band_name, logo=logo)
                return

            else:
                print("Invalid option. Cancelling...")
                return               


        else:
            print("Invalid option. Cancelling...")
            return


    if value1.lower() == "member" or value1.lower() == "m" or value1.lower() == "band member":
    
        member_name = input("\nPlease enter the name of the member name you want to update. ")
        while True:
            check = name_check("member", member_name)
            if check == True:
                break
            else:
                member_name = input("This band member isn't in the database. Check your spelling and enter it again. Press Q to quit. ")
                if member_name.lower() == "q" or member_name.lower() == "quit":
                    return
                else:
                    continue      
        
        
        value = input("\nWould you like to delete the band member, or update band member information. Press 'D' or 'U'. ")  
        if value.lower() == "delete" or value.lower() == "d":
            print("\nNow accessing the database, please wait...\n")
            update_function(type="delete_member", member_name=member_name)
            return
        
        if value.lower() == "update" or value.lower() == "u":
            value = input("\nWould you like to update the member name, ideology or band membership? ")
            if value.lower() == "member name" or value.lower() == "name" or value.lower() == "n":
                new_member_name = input("\nPlease enter the new name of the member. ")
                print("\nNow accessing the database, please wait...\n")
                update_function(type="update_member_name", member_name=member_name, new_member_name=new_member_name)
                return

            if value.lower() == "ideology" or value.lower() == "i":
                ideology = input("\nPlease enter the new ideology of the member. ")
                print("\nNow accessing the database, please wait...\n")
                update_function(type="update_member_ideology", member_name=member_name, ideology=ideology)
                return

            if value.lower() == "band membership" or value.lower() == "membership" or value.lower() == "b" or value.lower() == "band" or value.lower() == "m":
                value = input("\nWould you like to remove band membership('remove'), add band membership('add'), change the year they joined a band ('joined'), or the year they left a band ('left')? ")
                band_name = input("\nPlease enter the name of the band. ")
                if value.lower() == "add" or value.lower() == "add band membership" or value.lower() == "a":
                    print("\nNow accessing the database, please wait...\n")
                    update_function(type="add_member_band_membership", member_name=member_name, band_name=band_name)
                    return
                
                
                while True:
                    check = name_check("band", band_name)
                    if check == True:
                        break
                    else:
                        band_name = input("\nThis band isn't in the database. Check your spelling and enter it again. Press Q to quit. ")
                        if band_name.lower() == "q" or band_name.lower() == "quit":
                            return
                        else:
                            continue
                if value.lower() == "remove" or value.lower() == "remove band membership" or value.lower() == "r":
                    print("\nNow accessing the database, please wait...\n")
                    update_function(type="remove_member_band_membership", member_name=member_name, band_name=band_name)
                    return

                if value.lower() == "joined" or value.lower() == "join" or value.lower() == "j" or value.lower() == "year joined":
                    joined = input("\nPlease enter the new year that they joined the band. ")
                    print("\nNow accessing the database, please wait...\n")
                    update_function(type="update_joined_year", member_name=member_name, band_name=band_name, joined=joined)
                    return

                if value.lower() == "left" or value.lower() == "leave" or value.lower() == "l" or value.lower() == "year left":
                    left = input("\nPlease enter the new year that they left the band. ")
                    print("\nNow accessing the database, please wait...\n")
                    update_function(type="update_left_year", member_name=member_name, band_name=band_name, left=left)
                    return
                else:
                    print("Invalid option. Cancelling...")
                    return

            else:
                print("Invalid option. Cancelling...")
                return 

        else:
            print("Invalid option. Cancelling...")
            return
        
    if value.lower() == "c":
        return
    else:
        print("Invalid option. Cancelling...")
        return
    
def search():
    value = input("Would you like to search for a band or a band member? Press 'C' to cancel. ")
    if value.lower() == "band" or value.lower() == "b":
        band_name = input("\nPlease enter the name of the band. ")
        print("\nNow accessing the database, please wait...\n")
        band_search(band_name)
        return

    if value.lower() == "band member" or value.lower() == "member" or value.lower() == "m":
        member_name = input("\nPlease enter the name of the band member. ")
        print("\nNow accessing the database, please wait...\n")
        member_search(member_name)
        return
    
    if value.lower() == "c":
        return

    else:
        print("Invalid option. Cancelling...")
        return