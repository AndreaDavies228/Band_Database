#!/usr/bin/env python3

from functions import *

print("Welcome to the band database.")

while True:
  action = selection()
                                          
  if action == "A":
    add()
  if action == "U":
    update()
  if action == "S":
    search()
  value = input("\nWould you like to perform another action? ")
  if value.lower() == "no" or value.lower() == "n":
    break

print("\nThank you for using the band database. We hope to see you again soon.")
exit_check = input("Press any key to exit. ")
if exit_check == True:
  exit()



