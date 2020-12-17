""" this module has 3 functions that interact
with the database to print the whole database,
return the specific birthday of a certain person,
and check if a known person given as an input by the
user is present in the database"""
import csv
import pandas as pd


def print_birthdays():
    print('Welcome to the birthday dictionary.' +
          'We know the birthdays of these people:')
    db = pd.DataFrame(pd.read_csv('people_birthday.csv'))
    return print(db)


def return_birthday(name):
    name = name.lower()
    db = pd.DataFrame(pd.read_csv('people_birthday.csv'))
    people = db["Person"].str.lower()
    if name in people.values:
        return print('{}\'s birthday is {}.'.format(name,
                     db["Birthday"].loc[people == name].values[0]))
    else:
        return print('Sadly, we don\'t have {}\'s birthday.'
                     .format(name))


def check_person(person):
    person = person.lower()
    db = pd.DataFrame(pd.read_csv('people_birthday.csv'))
    people = db["Person"].str.lower()
    if person in people.values:
        return True
    return False
