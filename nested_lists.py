def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float

    return the average of the grades in asn_grades

    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0

    '''

    total = 0

    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)

def contains(value, lst):
    ''' (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    '''

    found = False  # We have not yet found value in the list.

    for i in range(len(lst)):
       for j in range(len(lst[i])):
           if lst[i][j] == value:
               found = True

    return found
