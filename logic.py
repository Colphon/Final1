import csv
import re

def checkID(input) -> str:
    '''
    Function that checks if the voter id is seven characters long and alphanumeric. A TypeError is raised otherwise.
    If the id is already listed in data.csv, a NameError is raised.
    :param input: The id of the voter.
    '''
    id_eligible = re.match('^[a-zA-Z0-9]{7}$',input)
    if id_eligible:
        id = input.lower()
        with open('data.csv', 'r', newline='') as review:
            for line in review.readlines():
                match = re.match(id, line)
                if match:
                    raise NameError
        return id

    else:
        raise TypeError
def checkvote(input_vote, name) -> str:
    '''
    Function that checks who the voter voted for and returns that person. If nobody was selected, a ValueError is raised.
    Additionally, if a voter chooses the write-in option and doesn't provide a first and last name
    (or uses non-alphabet characters (except for the period used in a middle initial)), a SyntaxError is raised.
    :param input_vote: The person the voter voted for denoted as a value from 0-4 (0 means a radiobutton was not selected).
    :param name: The person the voter wrote down if they picked the write-in option. Is '' otherwise.
    '''

    if input_vote == 1:
        return 'Bianca T. Sparrow - D'
    elif input_vote == 2:
        return 'Edward M. Green - R'
    elif input_vote == 3:
        return 'Felicia F. Soot - L'
    elif input_vote == 4:
        name_check = re.match('^[A-Za-z]+( [A-Za-z]\\.)? [A-Za-z]+$', name)
        if name_check:
            return name
        else:
            raise SyntaxError

    else:
        raise ValueError

def submitvote(identification, candidate) -> None:
    '''
    Function that writes the id of the voter and the candidate they voted for to data.csv.
    :param identification: The id of the voter.
    :param candidate: The candidate the voter voted for.
    '''
    with open('data.csv', 'a', newline='') as stuffout:
        contentout = csv.writer(stuffout)
        contentout.writerow([identification, candidate])

