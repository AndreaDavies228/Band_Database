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
  value = input("Would you like to perform another action? ")
  if value.lower() == "no" or value.lower() == "n":
    break

print("Thank you for using the band database. We hope to see you again soon.")
exit()



