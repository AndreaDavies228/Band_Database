#!/usr/bin/env python3

from functions import *

print("Welcome to the band database.")
running = True
while running == True:
  action = selection()
                                          
  if action == "A":
    add()
  if action == "U":
    update()
  if action == "S":
    search()
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
  

print("\nThank you for using the band database. We hope to see you again soon.")
exit_check = input("Press any key to exit. ")
if exit_check == True:
  exit()



