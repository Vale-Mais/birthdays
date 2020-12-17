""" the module contains a single function that lets the user add the name of a known person and its birthday"""
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
    
    
    
   