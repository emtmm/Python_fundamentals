def averages(grades):
    ''' (list of list of number) -> list of float

    Return a new list in which item is the average of the grades in the inner
    list at the correspondent position grades.

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []

    for grades_list in grades:
        #calculate the average of grades_list and append
        #to averages

        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total / len(grades_list))

    return averages

