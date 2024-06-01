import csv
import re

def checkID(input):
    result = re.match('^[a-zA-Z0-9]{7}$',input)
    if result:
        id = input.lower()
        with open('data.csv', 'r', newline='') as review:
            for line in review.readlines():
                match = re.match(id, line)
                if match:
                    raise NameError
        return id

    else:
        raise TypeError
def checkvote(input_vote, name=''):
    if input_vote == 1:
        return 'Bianca T. Sparrow - D'
    elif input_vote == 2:
        return 'Edward M. Green - R'
    elif input_vote == 3:
        return 'Felicia F. Soot - L'
    elif input_vote == 4:
        name_check = re.match('^[A-Za-z]+( [A-Za-z]\\.)? [A-Za-z]+$', name)
        if name_check:
            print('yay')
            return name
        else:
            raise SyntaxError

    else:
        raise ValueError

def submitvote(identification, candidate):
    with open('data.csv', 'a', newline='') as stuffout:
        contentout = csv.writer(stuffout)
        contentout.writerow([identification, candidate])

