from adding import add_person
from checker import check_person, print_birthdays, return_birthday
import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('people_birthday.csv'))
parser = argparse.ArgumentParser(description='this program will check if the name you put is inside our database of known people or their birthday. If the names have more than one space, wrap them around quotes ("")')
parser.add_argument("name", help = "input the name of a known person or birthday")
parser.add_argument("-a", "--add", action = "store_true", help = "add a new guitarist or band")
args = parser.parse_args()
answer = args.name


if args.add:
    add_person(answer)
elif check_person(answer):
    print("The birthday of ", answer, "is ", db["Birthday"].loc[db["Person"].str.lower() == answer.lower()].values[0])
else:
    response = input (answer + " is not present in our database. Would you like to add him? (yes or no) -> ")
    if response == "yes":
        add_person(answer)
    else:
        print("No worries!")
