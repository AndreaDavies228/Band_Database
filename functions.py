from queries import *

def selection():
    selection = False
    while selection == False:
        value = input("\nWould you like to add an entry, update an entry, or search the database? \nPlease enter 'A', 'U', or 'S'. Enter 'Q' to quit. ")
        if value == "A" or value == "a" or value == "Add" or value == "add":
            selection = "A"
            return selection
        if value == "U" or value == "u" or value == "Update" or value == "update":
            selection = "U"
            return selection
        if value == "S" or value == "s" or value == "Search" or value == "s":
            selection = "S"
            return selection
        if value == "Q" or value == "q" or value == "Quit" or value == 'quit':
            selection = "Q"
            return selection
        else:
            print("\nInvalid input. Please select Add, Update, Search or Quit.")



def update():
    while True:
        value1 = input("\nWould you like to update a band or a band member? Enter 'C' to cancel. ")
    
        if value1.lower() == "band" or value1.lower() == "b":
            while True:
                band_name = input("\nPlease enter the name of the band you want to update. ")
            
                band_id = name_check("band", band_name)
                if band_id != False:
                    break
                else:
                    band_name = input("\nCheck your spelling and enter the band again. Enter 'C' to cancel. ")
                    if band_name.lower() == "c" or band_name.lower() == "cancel":
                        return
                    else:
                        continue

            while True:
                value = input("\nWould you like to delete the band, or update band information. \nEnter 'D' or 'U' or 'C' to cancel. ")
            
                if value.lower() == "delete" or value.lower() == "d":
                    print("\nNow accessing the database, please wait...\n")
                    update_function(type="delete_band", band_name=band_name, band_id=band_id)
                    return
                
                if value.lower() == "update" or value.lower() == "u":
                    while True:
                        value = input("\nWould you like to update the band name, ideology or logo? Enter 'B', 'I', 'L' or 'C' to cancel. " )
                    
                        if value.lower() == "band name" or value.lower() == "name" or value.lower() == "b" or value.lower() == "n":
                            new_band_name = input("\nPlease enter the new band name. ")
                            print("\nNow accessing the database, please wait...\n")
                            update_function(type="update_band_name", band_name=band_name, new_band_name=new_band_name, band_id=band_id)
                            return

                        if value.lower() == "ideology" or value.lower() == "i":
                            ideology = input("\nPlease enter the new band ideology. ")
                            print("\nNow accessing the database, please wait...\n")
                            update_function(type="update_band_ideology", band_name=band_name, ideology=ideology, band_id=band_id)
                            return

                        if value.lower() == "logo" or value.lower() == "l":
                            logo = input("\nPlease enter the new link to the band logo. ")
                            print("\nNow accessing the database, please wait...\n")
                            update_function(type="update_band_logo", band_name=band_name, logo=logo, band_id=band_id)
                            return
                        
                        if value.lower() == "c" or value.lower() == "cancel":
                            print("\nCancelling...")
                            return

                        else:
                            print("\nInvalid option.")
                            continue               


                if value.lower() == "c" or value.lower() == "cancel":
                            print("\nCancelling...")
                            return

                else:
                    print("\nInvalid option.")
                    continue  


        if value1.lower() == "member" or value1.lower() == "m" or value1.lower() == "band member":
        
            while True:
                member_name = input("\nPlease enter the name of the member name you want to update. ")
            
                member_id = name_check("member", member_name)
                if member_id != False:
                    break
                else:
                    member_name = input("\nCheck your spelling and enter the band member again. Enter 'C' to cancel. ")
                    if member_name.lower() == "c" or member_name.lower() == "cancel":
                        return
                    else:
                        continue      
            
            
            while True:
                value = input("\nWould you like to delete the band member, or update band member information. Enter 'D' or 'U'. ")  
            
                if value.lower() == "delete" or value.lower() == "d":
                    print("\nNow accessing the database, please wait...\n")
                    update_function(type="delete_member", member_name=member_name, member_id=member_id)
                    return
                
                if value.lower() == "update" or value.lower() == "u":
                    while True:
                        value = input("\nWould you like to update the member name, ideology or band membership? ")
                     
                        if value.lower() == "member name" or value.lower() == "name" or value.lower() == "n":
                            new_member_name = input("\nPlease enter the new name of the member. ")
                            print("\nNow accessing the database, please wait...\n")
                            update_function(type="update_member_name", member_name=member_name, new_member_name=new_member_name, member_id=member_id)
                            return

                        if value.lower() == "ideology" or value.lower() == "i":
                            ideology = input("\nPlease enter the new ideology of the member. ")
                            print("\nNow accessing the database, please wait...\n")
                            update_function(type="update_member_ideology", member_name=member_name, ideology=ideology, member_id=member_id)
                            return

                        if value.lower() == "band membership" or value.lower() == "membership" or value.lower() == "b" or value.lower() == "band" or value.lower() == "m":
                            while True:
                                value = input("\nWould you like to remove band membership('remove'), add band membership('add'), change the year they joined a band ('joined'), or the year they left a band ('left')? Enter 'C' to cancel. ")
                            
                                if value.lower() in ["add", "add band membership", "a", "remove", "remove bad membership", "r", "joined", "join", "j", "year joined", "left", "leave", "l", "year left"]:
                                    band_name = input("\nPlease enter the name of the band. ")
                                    
                                    while True:
                                        band_id = name_check("band", band_name)
                                        if band_id != False:
                                            break
                                        else:
                                            band_name = input("\nCheck your spelling and enter the band name again. Enter 'C' to cancel. ")
                                            if band_name.lower() == "c" or band_name.lower() == "cancel":
                                                return
                                            else:
                                                continue

                                    if value.lower() == "add" or value.lower() == "add band membership" or value.lower() == "a":
                                        print("\nNow accessing the database, please wait...\n")
                                        update_function(type="add_member_band_membership", member_name=member_name, band_name=band_name, band_id=band_id, member_id=member_id)
                                        return
                                    
                                    if value.lower() == "remove" or value.lower() == "remove band membership" or value.lower() == "r":
                                        print("\nNow accessing the database, please wait...\n")
                                        update_function(type="remove_member_band_membership", member_name=member_name, band_name=band_name, band_id=band_id, member_id=member_id)
                                        return

                                    if value.lower() == "joined" or value.lower() == "join" or value.lower() == "j" or value.lower() == "year joined":
                                        joined = input("\nPlease enter the new year that they joined the band. ")
                                        print("\nNow accessing the database, please wait...\n")
                                        update_function(type="update_joined_year", member_name=member_name, band_name=band_name, joined=joined, band_id=band_id, member_id=member_id)
                                        return

                                    if value.lower() == "left" or value.lower() == "leave" or value.lower() == "l" or value.lower() == "year left":
                                        left = input("\nPlease enter the new year that they left the band. ")
                                        print("\nNow accessing the database, please wait...\n")
                                        update_function(type="update_left_year", member_name=member_name, band_name=band_name, left=left, band_id=band_id, member_id=member_id)
                                        return
                                
                                if value.lower() == "c" or value.lower() == "cancel":
                                    print("\nCancelling...")
                                    return

                                else:
                                    print("\nInvalid option.")
                                    continue 

                        if value.lower() == "c" or value.lower() == "cancel":
                            print("\nCancelling...")
                            return

                        else:
                            print("\nInvalid option.")
                            continue  

                if value.lower() == "c" or value.lower() == "cancel":
                    print("\nCancelling...")
                    return

                else:
                    print("\nInvalid option.")
                    continue  
            
        if value1.lower() == "c" or value1.lower() == "cancel":
            print("\nCancelling...")
            return

        else:
            print("\nInvalid option.")
            continue 
    
def search():
    while True:
        value = input("\nWould you like to search for a band or a band member? Enter 'C' to cancel. ")
    
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
        
        if value.lower() == "c" or value.lower() == "cancel":
            print("\nCancelling...")
            return

        else:
            print("\nInvalid option.")
            continue 