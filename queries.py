
import psycopg2
from psycopg2 import Error
import config2
from tabulate import tabulate



def add_member(name, band, ideology, join_year, leave_year):
    name = name.title()
    band = band.title()
    ideology = ideology.title()
    new_band = False
    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        cursor.execute(f"select exists(select 1 from bands where name = '{band}')")
        band_exists = cursor.fetchall()

        running = True
        while running == True:
            if band_exists == [(False,)]:
                print("\nThis band doesn't exist in the database yet. The band needs to be added first.")
                new_band_check = input("Would you like to add the band now? ")
                if new_band_check.lower() == "y" or new_band_check.lower() == "yes":
                    new_band = band
                else:
                    print("\nCancelling...")
                running = "False"
                break

            cursor.execute(f"SELECT id, name, ideology from members WHERE name % '{name}' ORDER BY similarity(name, '{name}') DESC LIMIT 3;")
            results = cursor.fetchall()
            if results != []:
                print("\nThe database already contains some similar band members:")
                output_results = [x[1:] for x in results ]
                listed_results = [(i,)+(x) for i, x in enumerate(output_results, 1)]
                print(tabulate(listed_results, headers = ['Member No.', 'Name', 'Ideology'], tablefmt = 'psql'))
                while True:
                    check = input("\nDo you still want to add this band member? For details on which bands these members belong to press 'D' for 'details'. ")
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
                        print("\nInvalid input. Please press 'Y' or 'N'. ")
                        continue

            

            #needs error handling for existing combination
            cursor.execute(f"INSERT INTO members (name, ideology) VALUES ('{name}', '{ideology}')")

            cursor.execute(f"INSERT INTO bands_members (band_id, member_id) VALUES ( (SELECT id from bands WHERE bands.name = '{band}'), (SELECT id from members WHERE members.name = '{name}') );")
            if join_year == "NULL" and leave_year == "NULL":
                print(f"You have added the band member {name}, with the ideology '{ideology} as a member of {band}'.")
            if join_year == "NULL" and leave_year != "NULL":
                cursor.execute(f"INSERT INTO timeframes (bands_members_id, left_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.name = '{band}') and bands_members.member_id = (SELECT id from members WHERE members.name = '{name}')), {leave_year} );")
                print(f"You have added the band member {name}, with the ideology '{ideology}' who left {band} in {leave_year}.")
            if join_year != "NULL" and leave_year == "NULL":
                cursor.execute(f"INSERT INTO timeframes (bands_members_id, joined_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.name = '{band}') and bands_members.member_id = (SELECT id from members WHERE members.name = '{name}')), {join_year} );")
                print(f"You have added the band member {name}, with the ideology '{ideology}' who joined {band} in {join_year}.")
            if join_year != "NULL" and leave_year != "NULL":
                cursor.execute(f"INSERT INTO timeframes (bands_members_id, joined_year, left_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.name = '{band}') and bands_members.member_id = (SELECT id from members WHERE members.name = '{name}')), {join_year}, {leave_year} );")
                print(f"You have added the band member {name}, with the ideology '{ideology}' who joined {band} in {join_year} and left in {leave_year}.")
            connection.commit()
            running = False
            break
        
    except (Exception, Error) as error:
        print("\nError while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database has been closed.")
    return new_band

def name_check(type, name):
    name = name.title()
    id = False
    print(f"Checking if {name} exists in the database...")
    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        if type == "band":
            cursor.execute(f"select exists(select 1 from bands where name = '{name}')")
        if type == "member":
            cursor.execute(f"select exists(select 1 from members where name = '{name}')")
        exists = cursor.fetchall()
    
        
        if exists == [(False,)]:
            if type == "band":
                cursor.execute(f"select name, ideology from bands where name % '{name}' ORDER BY similarity(name, '{name}') DESC LIMIT 3;")
                similar_bands = cursor.fetchall()
                if similar_bands == []:
                    print("\nThis band is not in the database.")
                if similar_bands != []:
                    print("\nThis band is not in the database. Consider one of these bands instead:")
                    print(tabulate(similar_bands, headers = ['Name', 'Ideology'], tablefmt = 'psql'))
                
            if type == "member":
                cursor.execute(f"select name, ideology from members where name % '{name}' ORDER BY similarity(name, '{name}') DESC LIMIT 3;")
                similar_members = cursor.fetchall()
                if similar_members == []:
                    print("\nThis band member is not in the databse.")
                if similar_members != []:
                    print("\nThis band is not in the database. Consider one of these band members instead:")
                    print(tabulate(similar_members, headers = ['Name', 'Ideology'], tablefmt = 'psql'))
                    
    
        
        if exists == [(True,)]:
            print("\nThis entry is in the databse.")
            if type == "band":
                cursor.execute(f"SELECT bands.id, bands.name, bands.ideology, logos.logo FROM bands LEFT JOIN logos on bands.id = logos.band_id where bands.name = '{name}';")
                band_list = cursor.fetchall()
                
                if len(band_list) == 1:
                    id = band_list[0][0]
                    
            
                if len(band_list) > 1:
                    print("\nThis database contains multiple bands with that name: ")
                    output_results = [x[1:] for x in band_list ]
                    listed_results = [(i,)+(x) for i, x in enumerate(output_results, 1)]
                    band_id_list = [x[0] for x in band_list]
                    
                    print(tabulate(listed_results, headers = ['Band No.', 'Band', 'Ideology', 'Logo'], tablefmt = 'psql'))
                    counter = 0
                    for band_id in band_id_list:
                        counter += 1
                        cursor.execute(f"SELECT members.name, members.ideology, timeframes.joined_year, timeframes.left_year from bands join bands_members on bands.id = bands_members.band_id  join members on bands_members.member_id = members.id join timeframes on timeframes.bands_members_id = bands_members.id WHERE bands.id = '{band_id}';")
                        member_results = cursor.fetchall()
                        if member_results == []:
                            print(f"\nNo members for band No.{counter} are in the database.")
                        else:
                            print(f"\nBand No.{counter} contains the following members:")
                            print(tabulate(member_results, headers = ['Name', 'Ideology', 'Year Joined', 'Year Left'], tablefmt = 'psql'))
                    while True:
                        select_band = input("\nWhich band would you like to update? Please enter the number of the band as a numeral. ")
                        if select_band.lower() == "c" or select_band.lower() == "cancel":
                            print("\nCancelling...")
                            break
                        try:
                            band_number = int(select_band)
                        except:
                            print("\nInvalid input.")
                            continue
                        if band_number >= 1 and len(band_list) >= band_number:
                            id = band_list[band_number-1][0]
                            break
                        else:
                            print("\nInvalid input.")
                            continue

            if type == "member":
                cursor.execute(f"SELECT members.id, members.name, members.ideology, FROM members where members.name = '{name}';")
                member_list = cursor.fetchall()
                
                if len(member_list) == 1:
                    id = member_list[0][0]
                    
            
                if len(member_list) > 1:
                    print("\nThis database contains multiple band members with that name: ")
                    output_results = [x[1:] for x in member_list ]
                    listed_results = [(i,)+(x) for i, x in enumerate(output_results, 1)]
                    member_id_list = [x[0] for x in member_list]
                    
                    print(tabulate(listed_results, headers = ['member No.', 'Name', 'Ideology', 'Logo'], tablefmt = 'psql'))
                    counter = 0
                    for member_id in member_id_list:
                        counter += 1
                        cursor.execute(f"SELECT bands.name, bands.ideology, logos.logo FROM bands LEFT JOIN logos on on bands.id = logos.band_id join bands_members on bands.id = bands_members.band_id  join members on bands_members.member_id = members.id WHERE members.id = '{member_id}';")
                        band_results = cursor.fetchall()
                        if band_results == []:
                            print(f"\nNo members for member No.{counter} are in the database.")
                        else:
                            print(f"\nMember No.{counter} has belonged to the following bands:")
                            print(tabulate(band_results, headers = ['Name', 'Ideology', 'logo'], tablefmt = 'psql'))
                    while True:
                        select_member = input("\nWhich member would you like to update? Please enter the number of the band member as a numeral. ")
                        if select_member.lower() == "c" or select_member.lower() == "cancel":
                            print("\nCancelling...")
                            break
                        try:
                            member_number = int(select_member)
                        except:
                            print("\nInvalid input.")
                            continue
                        if member_number >= 1 and len(member_list) >= member_number:
                            id = member_list[member_number-1][0]
                            break
                        else:
                            print("\nInvalid input")
                            continue
        else:
            return False
        
    except (Exception, Error) as error:
        print("\nError while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    return id

def update_function(type, band_name="", new_band_name="", ideology="", logo="", member_name="", new_member_name="", joined="", left="", band_id="", member_id=""):
    band_name = band_name.title()
    new_band_name = new_band_name.title()
    ideology = ideology.title()
    member_name = member_name.title()
    new_member_name = new_member_name.title()
    
    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()

                       
        if type == "delete_band":
            cursor.execute(f"delete from bands where id = '{band_id}';")
            print(f"Deleted {band_name}.")
        if type == "update_band_name":
            cursor.execute(f"update bands set name = '{new_band_name}' where id = '{band_id}';")
            print(f"Renamed {band_name} to {new_band_name}.")
        if type == "update_band_ideology":
            cursor.execute(f"update bands set ideology = '{ideology}' where id = '{band_id}';")
            print(f"Changed ideology for {band_name} to {ideology}.")
        if type == "update_band_logo":
            cursor.execute(f"update logos set logo = '{logo}' where band_id =(SELECT id from bands WHERE bands.id = '{band_id}');")
            print(f"Changed logo for {band_name} to {logo}.")
        if type == "delete_member":
            cursor.execute(f"delete from members where id = '{member_id}';")
            print(f"Deleted {member_name}.")
        if type == "update_member_name":
            cursor.execute(f"update members set name = '{new_member_name}' where id = '{member_id}';")
            print(f"Renamed {member_name} to {new_member_name}.")        
        if type == "update_member_ideology":
            cursor.execute(f"update members set ideology = '{ideology}' where id = '{member_id}';")
            print(f"Changed ideology for {member_name} to {ideology}.")
        if type == "remove_member_band_membership":
            cursor.execute(f"delete from bands_members where band_id=(SELECT id from bands WHERE bands.id = '{band_id}') and member_id=(SELECT id from members WHERE members.id = '{member_id}');")
            print(f"{member_name} is no long connected to {band_name}.")  
        if type == "add_member_band_membership":
            cursor.execute(f"INSERT INTO bands_members (band_id, member_id) VALUES ( (SELECT id from bands WHERE bands.id = '{band_id}'), (SELECT id from members WHERE members.id = '{member_id}')")
            print(f"{member_name} is now connected to {band_name}.") 
        if type == "update_joined_year":
            cursor.execute(f"update timeframes set joined_year = {joined} where bands_members_id='(SELECT id from bands_members WHERE band_id = (SELECT id from bands WHERE bands.id = '{band_id}') and member_id=(SELECT id from members WHERE members.id = '{member_id}'));")
            print(f"Updated the year {member_name} joined {band_name} to {joined}.")  
        if type == "update_left_year":
            cursor.execute(f"update timeframes set left_year = {left} where bands_members_id='(SELECT id from bands_members WHERE band_id = (SELECT id from bands WHERE bands.id = '{band_id}') and member_id=(SELECT id from members WHERE members.name = '{member_id}'));")
            print(f"Updated the year {member_name} left {band_name} to {joined}.")  
        connection.commit()


    except (Exception, Error) as error:
        print("\nError while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database has been closed.")

def band_search(band_name):
    band_name = band_name.title()

    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        cursor.execute(f"SELECT bands.id, bands.name, bands.ideology, logos.logo FROM bands LEFT JOIN logos on bands.id = logos.band_id  WHERE name % '{band_name}' ORDER BY similarity(name, '{band_name}') DESC LIMIT 3;")
        results = cursor.fetchall()
        if results == []:
            print("\nThere aren't any similar bands in the database, please check your spelling and try again.")
        else:
            print("\nYour search returned the following results:")
            output_results = [x[1:] for x in results ]
            listed_results = [(i,)+(x) for i, x in enumerate(output_results, 1)]
            band__id_list = [x[0] for x in results ]
            
            print(tabulate(listed_results, headers = ['Band No.', 'Band', 'Ideology', 'Logo'], tablefmt = 'psql'))
            counter = 0
            for band_id in band__id_list:
                counter += 1
                cursor.execute(f"SELECT members.name, members.ideology, timeframes.joined_year, timeframes.left_year from bands join bands_members on bands.id = bands_members.band_id  join members on bands_members.member_id = members.id join timeframes on timeframes.bands_members_id = bands_members.id WHERE bands.id = '{band_id}';")
                member_results = cursor.fetchall()
                if member_results == []:
                    print(f"\nNo members for band No.{counter} are in the database.")
                else:
                    print(f"\nBand No.{counter} contains the following members:")
                    print(tabulate(member_results, headers = ['Name', 'Ideology', 'Year Joined', 'Year Left'], tablefmt = 'psql'))
        
    except (Exception, Error) as error:
        print("\nError while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database has been closed.")



def member_search(member_name):
    member_name = member_name.title()

    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        cursor.execute(f"SELECT id, name, ideology from members WHERE name % '{member_name}' ORDER BY similarity(name, '{member_name}') DESC LIMIT 3;")
        results = cursor.fetchall()
        if results == []:
            print("\nThere aren't any similar band members in the database, please check your spelling and try again.")
        else:
            print("\nYour search returned the following results:")
            output_results = [x[1:] for x in results ]
            listed_results = [(i,)+(x) for i, x in enumerate(output_results, 1)]
            member_id_list = [x[0] for x in results ]
            print(tabulate(listed_results, headers = ['Member No.', 'Name', 'Ideology'], tablefmt = 'psql'))
            
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
        
    except (Exception, Error) as error:
        print("\nError while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database has been closed.")