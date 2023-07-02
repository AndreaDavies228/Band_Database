
import psycopg2
from psycopg2 import Error
import config2
from tabulate import tabulate

def add_band(name, ideology, logo=False):
    name = name.title()
    ideology = ideology.title()
    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        cursor.execute(f"select exists(select 1 from bands where name='{name}')")
        exists = cursor.fetchall()
        if exists == [(True,)]:
            print("This band already exists in the database.")
        if exists == [(False,)]:
            if logo == False:
                cursor.execute(f"INSERT INTO bands (name, ideology) VALUES ('{name}', '{ideology}')")
                print(f"You have added the band {name}, with the ideology '{ideology}'.")
            else:
                cursor.execute(f"INSERT INTO bands (name, ideology) VALUES ('{name}', '{ideology}')")
                cursor.execute(f"INSERT INTO logos (band_id, logo) VALUES ( (SELECT id from bands WHERE bands.name ='{name}'), '{logo}' );")
                print(f"You have added the band {name}, with the ideology '{ideology}' and a link to their logo.")
            connection.commit()
        
    except (Exception, Error) as error:
        print("Error while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database is closed.")

def add_member(name, band, ideology, join_year, leave_year):
    name = name.title()
    band = band.title()
    ideology = ideology.title()
    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        cursor.execute(f"select exists(select 1 from members where name='{name}')")
        member_exists = cursor.fetchall()
        cursor.execute(f"select exists(select 1 from bands where name='{band}')")
        band_exists = cursor.fetchall()

        while True:
            if band_exists == [(False,)]:
                print("This band doesn't exist in the database yet. Please add the band first.")
                break

            if member_exists == [(False,)]:
                cursor.execute(f"INSERT INTO members (name, ideology) VALUES ('{name}', '{ideology}')")

            if member_exists == [(True,)] and band_exists == [(True,)]:
                cursor.execute(f"select exists(select 1 from bands_members where band_id=(SELECT id from bands WHERE bands.name ='{band}') and member_id=(SELECT id from members WHERE members.name ='{name}'))")
                combo_exists = cursor.fetchall()
                if combo_exists == [(True,)]:
                    print("This band member already exists in the database as a member of this band.")
                    break

            cursor.execute(f"INSERT INTO bands_members (band_id, member_id) VALUES ( (SELECT id from bands WHERE bands.name ='{band}'), (SELECT id from members WHERE members.name ='{name}') );")
            if join_year == "NULL" and leave_year == "NULL":
                print(f"You have added the band member {name}, with the ideology '{ideology} as a member of {band}'.")
            if join_year == "NULL" and leave_year != "NULL":
                cursor.execute(f"INSERT INTO timeframes (bands_members_id, left_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.name ='{band}') and bands_members.member_id = (SELECT id from members WHERE members.name ='{name}')), {leave_year} );")
                print(f"You have added the band member {name}, with the ideology '{ideology}' who left {band} in {leave_year}.")
            if join_year != "NULL" and leave_year == "NULL":
                cursor.execute(f"INSERT INTO timeframes (bands_members_id, joined_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.name ='{band}') and bands_members.member_id = (SELECT id from members WHERE members.name ='{name}')), {join_year} );")
                print(f"You have added the band member {name}, with the ideology '{ideology}' who joined {band} in {join_year}.")
            if join_year != "NULL" and leave_year != "NULL":
                cursor.execute(f"INSERT INTO timeframes (bands_members_id, joined_year, left_year) VALUES ( (SELECT id from bands_members WHERE bands_members.band_id = (SELECT id from bands WHERE bands.name ='{band}') and bands_members.member_id = (SELECT id from members WHERE members.name ='{name}')), {join_year}, {leave_year} );")
                print(f"You have added the band member {name}, with the ideology '{ideology}' who joined {band} in {join_year} and left in {leave_year}.")
            connection.commit()
            break
        
    except (Exception, Error) as error:
        print("Error while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database is closed.")

def name_check(type, name):
    name = name.title()
    print(f"Checking if {name} exists in the database...")
    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        if type == "band":
            cursor.execute(f"select exists(select 1 from bands where name='{name}')")
        if type == "member":
            cursor.execute(f"select exists(select 1 from members where name='{name}')")
        exists = cursor.fetchall()

        
    except (Exception, Error) as error:
        print("Error while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    
    if exists == [(True,)]:
        print("This entry is in the databse.")
        return True
    if exists == [(False,)]:
        return False

def update_function(type, band_name="", new_band_name="", ideology="", logo="", member_name="", new_member_name="", joined="", left=""):
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
            cursor.execute(f"delete from bands where name='{band_name}';")
            print(f"Deleted {band_name}.")
        if type == "update_band_name":
            cursor.execute(f"update bands set name = '{new_band_name}' where name='{band_name}';")
            print(f"Renamed {band_name} to {new_band_name}.")
        if type == "update_band_ideology":
            cursor.execute(f"update bands set ideology = '{ideology}' where name='{band_name}';")
            print(f"Changed ideology for {band_name} to {ideology}.")
        if type == "update_band_logo":
            cursor.execute(f"update logos set logo = '{logo}' where band_id =(SELECT id from bands WHERE bands.name ='{band_name}');")
            print(f"Changed logo for {band_name} to {logo}.")
        if type == "delete_member":
            cursor.execute(f"delete from members where name='{member_name}';")
            print(f"Deleted {member_name}.")
        if type == "update_member_name":
            cursor.execute(f"update members set name = '{new_member_name}' where name='{member_name}';")
            print(f"Renamed {member_name} to {new_member_name}.")        
        if type == "update_member_ideology":
            cursor.execute(f"update members set ideology = '{ideology}' where name='{member_name}';")
            print(f"Changed ideology for {member_name} to {ideology}.")
        if type == "remove_member_band_membership":
            cursor.execute(f"delete from bands_members where band_id=(SELECT id from bands WHERE bands.name ='{band_name}') and member_id=(SELECT id from members WHERE members.name ='{member_name}');")
            print(f"{member_name} is no long connected to {band_name}.")  
        if type == "add_member_band_membership":
            cursor.execute(f"INSERT INTO bands_members (band_id, member_id) VALUES ( (SELECT id from bands WHERE bands.name ='{band_name}'), (SELECT id from members WHERE members.name ='{member_name}')")
            print(f"{member_name} is now connected to {band_name}.") 
        if type == "update_joined_year":
            cursor.execute(f"update timeframes set joined_year = {joined} where bands_members_id='(SELECT id from bands_members WHERE band_id = (SELECT id from bands WHERE bands.name ='{band_name}') and member_id=(SELECT id from members WHERE members.name ='{member_name}'));")
            print(f"Updated the year {member_name} joined {band_name} to {joined}.")  
        if type == "update_left_year":
            cursor.execute(f"update timeframes set left_year = {left} where bands_members_id='(SELECT id from bands_members WHERE band_id = (SELECT id from bands WHERE bands.name ='{band_name}') and member_id=(SELECT id from members WHERE members.name ='{member_name}'));")
            print(f"Updated the year {member_name} left {band_name} to {joined}.")  
        connection.commit()


    except (Exception, Error) as error:
        print("Error while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database is closed.")

def band_search(band_name):
    band_name = band_name.title()

    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        cursor.execute(f"SELECT bands.name, bands.ideology, logos.logo FROM bands LEFT JOIN logos on bands.id = logos.band_id  WHERE name ='{band_name}' ;")
        results = cursor.fetchall()
        if results == []:
            print("This band isn't in the database, please check your spelling and try again.")
        else:
            print("Below are the band details:")
            print(tabulate(results, headers = ['Band', 'Ideology', 'Logo'], tablefmt = 'psql'))
            cursor.execute(f"SELECT members.name, members.ideology, timeframes.joined_year, timeframes.left_year from bands join bands_members on bands.id = bands_members.band_id  join members on bands_members.member_id = members.id join timeframes on timeframes.bands_members_id = bands_members.id WHERE bands.name ='{band_name}';")
            member_results = cursor.fetchall()
            if member_results == []:
                print("No members for this band are in the database.")
            else:
                print("This band contains the following members:")
                print(tabulate(member_results, headers = ['Name', 'Ideology', 'Year Joined', 'Year Left'], tablefmt = 'psql'))
        
    except (Exception, Error) as error:
        print("Error while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database is closed.")



def member_search(member_name):
    member_name = member_name.title()

    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        cursor.execute(f"SELECT name, ideology from members WHERE name ='{member_name}' ;")
        results = cursor.fetchall()
        if results == []:
            print("This band member isn't in the database, please check your spelling and try again.")
        else:
            print("Below are the member details:")
            print(tabulate(results, headers = ['Name', 'Ideology'], tablefmt = 'psql'))
            
            cursor.execute(f"SELECT bands.name, bands.ideology, timeframes.joined_year, timeframes.left_year from members join bands_members on members.id = bands_members.member_id  join bands on bands_members.band_id = bands.id join timeframes on timeframes.bands_members_id = bands_members.id WHERE members.name ='{member_name}';")
            band_results = cursor.fetchall()
            if band_results == []:
                print("There are no bands this member has belonged to in the database.")
            else:            
                print("They have belonged to the following bands:")
                print(tabulate(band_results, headers = ['Band', 'Ideology', 'Year Joined', 'Year Left'], tablefmt = 'psql'))
        
    except (Exception, Error) as error:
        print("Error while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database is closed.")