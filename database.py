""" this module contains a function that
takes the data from the dictionary and
creates a csv file containing all the data"""
import csv
from dict_birthdays import birthdays
import pandas as pd


def database(dictionary):

    p_b = []
    for key, value in dictionary.items():
        p_b.append([key, value])
    df = pd.DataFrame(p_b, columns=["Person", "Birthday"])
    df.to_csv("people_birthday.csv")


database(birthdays)
