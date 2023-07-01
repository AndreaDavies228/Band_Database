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
    print("This has not been implemented yet")
  value = input("Would you like to perform another action? ")
  if value.lower() == "no" or value.lower() == "n":
    break

print("Thank you for using the band database")
exit()



