#!/usr/bin/env python3

from functions import *
from add_band import *
from add_member import *

print("Welcome to the band database.")
running = True
while running == True:
  action = selection()
                                        
  if action == "A":
    while True:
      value = input("\nWould you like to add a band or a band member? Enter 'C' to cancel. ")
      if value == "band" or value == "Band" or value == "b" or value == "B":
        band_added = add_band()
        if band_added != False:
          value2 = input("\nWould you also like to add band members for this band? ")
          if value2.lower() == "y" or value2.lower() == "yes":
            while True:
              add_member(band_added)
              value3 = input("\nWould you like to add another band member?")
              if value3.lower() == "y" or value3.lower() == "yes":
                continue
              if value3.lower() == "n" or value3.lower() == "no":
                break
              else:
                print("Invalid input. Please enter 'Y' or 'N'.")
                continue
          if value2.lower() == "n" or value2.lower() == "no":
                break
          else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            continue


        else:
          break

      if value.lower() == "member" or value.lower() == "band member" or value.lower() == "m":
        add_band = add_member()
        if add_band != False:
          add_band(add_band)
        break

      if value.lower() == "c" or value.lower() == "cancel":
          print("\nCancelling...")
          break

      else:
          print("\nInvalid input. ")
          continue
  if action == "U":
    update()
  if action == "S":
    search()
  if action == "Q":
    running = False
    break
  if running == True:
    while True:
      value = input("\nWould you like to perform another action? ")
      if value.lower() == "yes" or value.lower() == "y":
        break
      if value.lower() == "no" or value.lower() == "n":
        running = False
        break
      else:
        print("Invalid input. Please select 'Y' or 'N'.")
        continue
  


if running == False:
  print("\nThank you for using the band database. We hope to see you again soon.")
  exit_check = input("Enter any key to exit. ")
  if exit_check == True:
    exit()



