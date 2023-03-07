Phonebook = {1111: 'Layla',
             2222: 'Mohammed'}  # Dictionary using numbers as keys


def searching():
    search = input('Type number: ')  # input from user
    try:
        search = int(search)  # checking if input is only numbers and integer, then doing searching
        if search in Phonebook.keys():
            print('This number is for', Phonebook[search])
        else:
            print('Sorry, this number and its owner is not available')
    except ValueError:  # if input is not numbers and integer only
        print('This number is invalid')


searching()  # calling function to start the code
