
import psycopg2
from psycopg2 import Error

def add_band(name, ideology, logo=False):
    try:
        connection = psycopg2.connect(user="huomhxoy",
                                    password="m6RnaMWGNxrURmWMSS_WWK3eiLwO93BY",
                                    host="snuffleupagus.db.elephantsql.com",
                                    port="5432",
                                    database="huomhxoy")

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