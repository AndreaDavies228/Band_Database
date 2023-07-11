import psycopg2
from psycopg2 import Error
import config2
from tabulate import tabulate

def add_member(band_id=False):
    add_to_band = True
    add_band = False
    name = input("\nPlease enter the name of the band member. ")
    print("\nConnecting to the database to check if similar band members exist in the database. Please wait...")
    if name:
        name = name.title()
        try:
            connection = psycopg2.connect(user=config2.user,
                                        password=config2.PW,
                                        host=config2.host,
                                        port=config2.port,
                                        database=config2.database)

            cursor = connection.cursor()
            #check if member exists
            cursor.execute(f"SELECT id, name, ideology from members WHERE name % '{name}' ORDER BY similarity(name, '{name}') DESC LIMIT 3;")
            results = cursor.fetchall()
            running = True
            
            if results != []:
                print("\nThe database already contains some similar band members:")
                output_results = [x[1:] for x in results ]
                listed_results = [(i,)+(x) for i, x in enumerate(output_results, 1)]
                print(tabulate(listed_results, headers = ['Member No.', 'Name', 'Ideology'], tablefmt = 'psql'))
                while True:
                    check = input("\nDo you still want to add this band member as a new entry? \nChanges to existing band members should be done instead using the update option. \nFor details on which bands these members belong to enter 'D' for 'details'. ")
                    if check.lower() == "y" or check.lower() == "yes":
                        break
                    if check.lower() in ["n", "no", "c", "cancel", "q", "quit"]:
                        running = False
                        break
                    if check.lower() == "d" or check.lower() == "details":
                        member_id_list = [x[0] for x in results ]
                        counter = 0
                        for member_id in member_id_list:
                            counter += 1
                            cursor.execute(f"SELECT bands.name, bands.ideology, timeframes.joined_year, timeframes.left_year from members join bands_members on members.id = bands_members.member_id  join bands on bands_members.band_id = bands.id join timeframes on timeframes.bands_members_id = bands_members.id WHERE members.id = '{member_id}';")
                            band_results = cursor.fetchall()
                            if band_results == []:
                                print(f"\nThere are no bands that member No.{counter} has belonged to in the database.")
                            else:            
                                print(f"\nMember No.{counter} has belonged to the following bands:")
                                print(tabulate(band_results, headers = ['Band', 'Ideology', 'Year Joined', 'Year Left'], tablefmt = 'psql'))
                        continue
                    else:
                        print("\nInvalid input. Please enter 'Y', 'N' or 'D'. ")
                        continue

            if results == []:
                print("\nThere are no similar band members already in the database.")
            
            if running == True:
                
                if band_id == False:
                    entered_band_name = False
                    while entered_band_name == False:
                        band_name = input("\nPlease enter the name of the band they belong to. \nIf you don't want them to belong to a band, please enter 'None'. ")
                        if band_name.lower() == "none" or band_name.lower() == "n":
                            add_to_band = False
                            entered_band_name = True
                        
                        elif band_name:
                            cursor.execute(f"SELECT bands.id, bands.name, bands.ideology, logos.logo from bands LEFT JOIN logos on bands.id = logos.band_id WHERE name % '{band_name}' ORDER BY similarity(name, '{band_name}') DESC LIMIT 3;")
                            results = cursor.fetchall()
                            running = True
                            
                            if results != []:
                                print("\nThe database contains the following matches:")
                                output_results = [x[1:] for x in results ]
                                listed_results = [(i,)+(x) for i, x in enumerate(output_results, 1)]                        
                                print(tabulate(listed_results, headers = ['Band No.', 'Name', 'Ideology', 'Logo'], tablefmt = 'psql'))
                            
                                while True:
                                    check = input("\nDo you want to add them to one of these existing bands, or first add a new band? \nFor an existing band enter the band's number as a numeral, for a new band enter 'New'. Otherwise for no band enter 'None'. \nFor details on which bands these members belong to enter 'D' for 'details'. ")
                                    
                                    try:
                                        band_number = int(check)
                                        if band_number >= 1 and len(results) >= band_number:
                                            band_id = results[band_number-1][0]
                                            entered_band_name = True
                                            break
                                        else:
                                            print("\nInvalid number. Please select a different input")
                                            continue                                
                                        
                                    except:
                                        if check.lower() == "new":
                                            add_band = band_name
                                            return add_band
                                        
                                        if check.lower() in ["none", "no", "c", "cancel", "q", "quit"]:
                                            while True:
                                                no_band_check = input("\nWould you still like to add the member without a band? ")
                                                if no_band_check.lower() == "yes" or no_band_check.lower() == "y":
                                                    add_to_band = False
                                                    entered_band_name = True
                                                    break
                                                if no_band_check.lower() == "no" or no_band_check.lower() == "n":
                                                    running = False
                                                    entered_band_name = True
                                                    break
                                            if running == False:
                                                break
                                        

                                            
                                        if check.lower() == "d" or check.lower() == "details":
                                            band_id_list = [x[0] for x in results ]
                                            counter = 0
                                            for band_id in band_id_list:
                                                counter += 1
                                                cursor.execute(f"SELECT members.name, members.ideology, timeframes.joined_year, timeframes.left_year from members join bands_members on members.id = bands_members.member_id  join bands on bands_members.band_id = bands.id join timeframes on timeframes.bands_members_id = bands_members.id WHERE bands.id = '{band_id}';")
                                                band_results = cursor.fetchall()
                                                if band_results == []:
                                                    print(f"\nThere are members for band No.{counter} in the database.")
                                                else:            
                                                    print(f"\nBand No.{counter} has had the following members:")
                                                    print(tabulate(band_results, headers = ['Band', 'Ideology', 'Year Joined', 'Year Left'], tablefmt = 'psql'))
                                            continue
                                        else:
                                            print("\nInvalid input. Please enter a numeral for a band, 'New' to add a new band, 'No' to add the member without linking to a band or 'C' to cancel. ")
                                            continue
                            else:
                                while True:
                                    print("\nThis band doesn't exist in the database yet. The band needs to be added first.")
                                    new_band_check = input("Would you like to add the band now? ")
                                    if new_band_check.lower() == "y" or new_band_check.lower() == "yes":
                                        add_band = band_name
                                        entered_band_name = True
                                        return
                                    else:
                                        print("\nCancelling...")
                                        break

                        else:
                            print("\nYou need to enter a band name.")
                            

                if running == True:
                    ideology = input("\nPlease enter the ideology of the band member. If you don't know please enter 'None'. ")
                    if ideology == "none" or ideology == "None" or ideology == "n" or ideology == "N" or ideology == "":
                        ideology = "None"
                    else:
                     ideology = ideology.title()
                    if add_to_band == True:
                        while True:
                            join_year = input("\nPlease enter the year they joined the band. If you don't know please enter 'None'. ")
                            if join_year.lower() == "none" or join_year.lower() == "n":
                                join_year = "None"
                                break
                            try:
                                join_year = int(join_year)
                                if join_year >1900 and join_year <2050:
                                    break
                                else:
                                    print("\nPlease enter a valid year")
                                    continue  
                            except:
                                print("\nYear needs to be a number.")
                                continue
                        while True:
                            leave_year = input("\nPlease enter the year they left the band. If you don't know please enter 'None'. ")
                            if leave_year.lower() == "none" or leave_year.lower() == "n":
                                leave_year = "None"
                                break
                            try:
                                leave_year = int(leave_year)
                                if leave_year >1900 and leave_year <2050 and leave_year > join_year:
                                    break
                                else:
                                    print("\nPlease enter a valid year")
                                    continue  
                            except:
                                print("\nYear needs to be a number.")
                                continue

                    if add_to_band ==True:
                        while True:
                            confirm = input(f"\n{name.title()} with ideology {ideology.title()} will be added as a member of {band_name.title()}, with join year: {join_year} and leave year: {leave_year}. Enter 'confirm' or 'cancel'. ")
                            if confirm.lower() == "y" or confirm.lower() == "yes" or confirm.lower() == "confirm":
                                if ideology == "None":
                                    ideology = "NULL"
                                if join_year == "none" or join_year == "None" or join_year == "n" or join_year == "N" or join_year == "":
                                    join_year = "NULL"
                                if leave_year == "none" or leave_year == "None" or leave_year == "n" or leave_year == "N" or leave_year == "":
                                    leave_year = "NULL"
                                break
                                
                            if confirm.lower() == "n" or confirm.lower() == "no" or confirm.lower() == "cancel":
                                print("\nCancelling...")
                                running = False
                                break
                            else:
                                print("\nInvalid input. Enter 'Y' or 'N' to confirm or cancel.")
                                continue
                    if add_to_band == False:
                        while True:
                            confirm = input(f"\n{name.title()} with ideology '{ideology.title()}' will be added. Enter 'Confirm' or 'Cancel'. ")
                            if confirm.lower() == "y" or confirm.lower() == "yes" or confirm.lower() == "confirm":
                                if ideology == "none" or ideology == "None" or ideology == "n" or ideology == "N" or ideology == "":
                                    ideology = "NULL"
                                break
                                
                            if confirm.lower() == "n" or confirm.lower() == "no" or confirm.lower() == "cancel":
                                print("n\Cancelling...")
                                running = False
                                break
                            else:
                                print("\nInvalid input. Enter 'confirm' or 'cancel'.")
                                continue

                
                    
            
                    cursor.execute(f"INSERT INTO members (name, ideology) VALUES ('{name}', '{ideology}')")
                    if add_to_band == True:
                        cursor.execute(f"SELECT name from bands WHERE id = {band_id}")
                        get_band_name = cursor.fetchone()
                        band = get_band_name[0]
                        cursor.execute(f"INSERT INTO bands_members (band_id, member_id) VALUES ( (SELECT id from bands WHERE bands.id = '{band_id}'), (SELECT id from members WHERE members.name = '{name}') );")
                        if join_year == "NULL" and leave_year == "NULL":
                            print(f"You have added the band member {name}, with the ideology '{ideology} as a member of {band}'.")
                        if join_year == "NULL" and leave_year != "NULL":
                            cursor.execute(f"INSERT INTO timeframes (bands_members_id, left_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.id = '{band_id}') and bands_members.member_id = (SELECT id from members WHERE members.name = '{name}')), {leave_year} );")
                            print(f"You have added the band member {name}, with the ideology '{ideology}' who left {band} in {leave_year}.")
                        if join_year != "NULL" and leave_year == "NULL":
                            cursor.execute(f"INSERT INTO timeframes (bands_members_id, joined_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.id = '{band_id}') and bands_members.member_id = (SELECT id from members WHERE members.name = '{name}')), {join_year} );")
                            print(f"You have added the band member {name}, with the ideology '{ideology}' who joined {band} in {join_year}.")
                        if join_year != "NULL" and leave_year != "NULL":
                            cursor.execute(f"INSERT INTO timeframes (bands_members_id, joined_year, left_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.id = '{band_id}') and bands_members.member_id = (SELECT id from members WHERE members.name = '{name}')), {join_year}, {leave_year} );")
                            print(f"You have added the band member {name}, with the ideology '{ideology}' who joined {band} in {join_year} and left in {leave_year}.")
                    else:
                        print(f"You have added the band member {name}, with the ideology '{ideology}'.")
                    connection.commit()
        
            
                
                
                    
        except (Exception, Error) as error:
            print("\nError while connecting to the database.", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("The connection to the database has been closed.")
        return add_band
    else:
        print("You need to enter a member name.")
