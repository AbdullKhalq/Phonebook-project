# A simple phonebook project made by AbdulKhaliq Alhassan as part of completing Python 101 on Satr.codes

import math  # To find number of digits in number without converting to string which is slower

Phonebook = {1111111111: "Layla",
             2222222222: "Mohammed",
             3333333333: "Manal"}  # Dictionary using numbers as keys


def searching():
    search = int(input("Type number: "))  # input from user
    if int(math.log10(search)) + 1 == 10:
        if search in Phonebook.keys():
            print(f"This number is for {Phonebook[search]}")
        else:
            print("Sorry, the number was not found")
    else:
        print("Invalid number")


searching()  # calling function to start the code
