
import psycopg2
from psycopg2 import Error
from config import *

def add_band(name, ideology, logo=False):
    try:
        connection = psycopg2.connect(user=config_user,
                                    password=config_PW,
                                    host=config_host,
                                    port=config_port,
                                    database=config_database)

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
    try:
        connection = psycopg2.connect(user="huomhxoy",
                                    password="m6RnaMWGNxrURmWMSS_WWK3eiLwO93BY",
                                    host="snuffleupagus.db.elephantsql.com",
                                    port="5432",
                                    database="huomhxoy")

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

def name_check(name):
    print("Checking entry exists in database...")
    try:
        connection = psycopg2.connect(user=config_user,
                                    password=config_PW,
                                    host=config_host,
                                    port=config_port,
                                    database=config_database)

        cursor = connection.cursor()
        cursor.execute(f"select exists(select 1 from bands where name='{name}')")
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
    try:
        connection = psycopg2.connect(user=config_user,
                                    password=config_PW,
                                    host=config_host,
                                    port=config_port,
                                    database=config_database)

        cursor = connection.cursor()

        if type == "delete_band":
            cursor.execute(f"delete from bands where name='{band_name}'")
            print(f"Deleted {band_name}.")
        if type == "update_band_name":
            cursor.execute(f"update bands name = '{new_band_name}' where name='{band_name}'")
            print(f"Renamed {band_name} to {new_band_name}.")
        if type == "update_band_ideology":
            cursor.execute(f"update bands ideology = '{ideology}' where name='{band_name}'")
            print(f"Changed ideology for {band_name} to {ideology}.")
        if type == "update_band_logo":
            cursor.execute(f"update logos logo = '{logo}' where band_id =(SELECT id from bands WHERE bands.name ='{band_name}')")
            print(f"Changed logo for {band_name} to {logo}.")
        if type == "delete_member":
            cursor.execute(f"delete from members where name='{member_name}'")
            print(f"Deleted {member_name}.")
        if type == "update_member_name":
            cursor.execute(f"update members name = '{new_member_name}' where name='{member_name}'")
            print(f"Renamed {member_name} to {new_member_name}.")        
        if type == "update_member_ideology":
            cursor.execute(f"update members ideology = '{ideology}' where name='{member_name}'")
            print(f"Changed ideology for {member_name} to {ideology}.")
        if type == "remove_member_band_membership":
            cursor.execute(f"delete from bands_members where band_id=(SELECT id from bands WHERE bands.name ='{band_name}') and member_id=(SELECT id from members WHERE members.name ='{member_name}')")
            print(f"{member_name} is no long connected to {band_name}.")  
        if type == "add_member_band_membership":
            cursor.execute(f"INSERT INTO bands_members (band_id, member_id) VALUES ( (SELECT id from bands WHERE bands.name ='{band_name}'), (SELECT id from members WHERE members.name ='{member_name}')")
            print(f"{member_name} is now connected to {band_name}.") 
        if type == "update_joined_year":
            cursor.execute(f"update timeframes joined_year = {joined} where bands_members_id='(SELECT id from bands_members WHERE band_id = (SELECT id from bands WHERE bands.name ='{band_name}') and member_id=(SELECT id from members WHERE members.name ='{member_name}'))")
            print(f"Updated the year {member_name} joined {band_name} to {joined}.")  
        if type == "update_left_year":
            cursor.execute(f"update timeframes left_year = {left} where bands_members_id='(SELECT id from bands_members WHERE band_id = (SELECT id from bands WHERE bands.name ='{band_name}') and member_id=(SELECT id from members WHERE members.name ='{member_name}'))")
            print(f"Updated the year {member_name} left {band_name} to {joined}.")  


    except (Exception, Error) as error:
        print("Error while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database is closed.")
