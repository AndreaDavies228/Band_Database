import psycopg2
from psycopg2 import Error
import config2
from tabulate import tabulate

def add_band(new_band=False):
    new_band_id = False
    if new_band == False:
        band_name = input("\nPlease enter the name of the band. ")
    else:
        band_name = new_band
    name = band_name.title()
    print("\nConnecting to the database to check if similar bands exist in the database. Please wait...")

    try:
        connection = psycopg2.connect(user=config2.user,
                                    password=config2.PW,
                                    host=config2.host,
                                    port=config2.port,
                                    database=config2.database)

        cursor = connection.cursor()
        
        cursor.execute(f"SELECT bands.id, bands.name, bands.ideology, logos.logo from bands LEFT JOIN logos on bands.id = logos.band_id WHERE name % '{name}' ORDER BY similarity(name, '{name}') DESC LIMIT 3;")
        results = cursor.fetchall()
        running = True
        
        if results != []:
            print("\nThe database already contains some similar bands:")
            output_results = [x[1:] for x in results ]
            listed_results = [(i,)+(x) for i, x in enumerate(output_results, 1)]
            print(tabulate(listed_results, headers = ['Band No.', 'Name', 'Ideology', 'Logo'], tablefmt = 'psql'))
            while True:
                check = input("\nDo you still want to add this band? \nFor details on which bands these members belong to enter 'D' for 'details'. ")
                if check.lower() == "y" or check.lower() == "yes":
                    break
                if check.lower() in ["n", "no", "c", "cancel", "q", "quit"]:
                    running = False
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
                    print("\nInvalid input. Please enter 'Y' or 'N'. ")
                    continue

        if results == []:
            print("\nNo similar bands found.")

        if running == True:
            ideology = input("\nPlease enter the ideology of the band. ")
            ideology = ideology.title()
            logo = input("\nPlease enter a URL link to the band's logo. \nIf you don't have a link please enter 'None'. ")
            if logo == "none" or logo == "None" or logo == "n" or logo == "N":
                logo = "None"
            while True:
                confirm = input(f"\n{band_name.title()} with ideology {ideology.title()} will be added with logo: {logo}. Enter 'Y' to confirm and 'N' to cancel. ")
                if confirm.lower() == "y" or confirm.lower() == "yes":
                    break
                if confirm.lower() == "n" or confirm.lower() == "no":
                    running = False
                    
                    break
                else:
                    print("\nInvalid input. Enter 'Y' or 'N' to confirm or cancel.")
                    continue
        
        if running == True:   
            if logo == "None":
                cursor.execute(f"INSERT INTO bands (name, ideology) VALUES ('{name}', '{ideology}')")
                print(f"You have added the band {name}, with the ideology '{ideology}'.")
                connection.commit()
                cursor.execute(f"SELECT id from bands ORDER BY id DESC LIMIT 1")
                new_band_id_tuple = cursor.fetchone()
                new_band_id = new_band_id_tuple[0]
            else:
                cursor.execute(f"INSERT INTO bands (name, ideology) VALUES ('{name}', '{ideology}')")
                cursor.execute(f"INSERT INTO logos (band_id, logo) VALUES ( (SELECT id from bands WHERE bands.name = '{name}'), '{logo}' );")
                print(f"You have added the band {name}, with the ideology '{ideology}' and a link to their logo.")
                connection.commit()
                cursor.execute(f"SELECT id from bands ORDER BY id DESC LIMIT 1")
                new_band_id_tuple = cursor.fetchone()
                new_band_id = new_band_id_tuple[0]
                
                
        
    except (Exception, Error) as error:
        print("\nError while connecting to the database.", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The connection to the database has been closed.")
    return new_band_id