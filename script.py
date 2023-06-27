#!/usr/bin/env python3

from functions import *

print("Welcome to the band database.")
#language = set_language()
selection = selection()
                                        
if selection == "A":
  add()
if selection == "U":
  update()
  print("This has not been implemented yet")
if selection == "S":
  search()
  print("This has not been implemented yet")

print("Thank you for using the band database")
exit()



