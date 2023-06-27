from functions import *
from searches import *

language = set_language()
selection = selection(language)
                                        
if selection == "A":
  add()
if selection == "U":
  update()
if selection == "S":
  search()

print("Thank you for using the band database")
exit()



