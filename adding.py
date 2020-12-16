
from checker import check_person 
import pandas as pd
import csv

def add_person(person):
    db = pd.DataFrame(pd.read_csv('people_birthday.csv'))
    if check_person(person):
        return print("sorry, but " + person + " is already present in the database, thank you anyway")
    bday = input("Now enter the birthday of this person -> ")
    with open('people_birthday.csv', 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        row = len(db)
        newFileWriter.writerow([row, person, bday])
    return print("Thank you for your contribution!")
    
    
    
   # elif name1 == "g":
    #    if response == "":
   #         name2 = input("Now enter the name of the band -> ")
    #    with open('players_bands.csv', 'a') as newFile:
     #       newFileWriter = csv.writer(newFile)
    #        row = len(db)
    #        newFileWriter.writerow([row, g_or_b, name2 ])
   #     return print("Thank you for your contribution!")
   # else:
  #      return print("you need to input either g or b")