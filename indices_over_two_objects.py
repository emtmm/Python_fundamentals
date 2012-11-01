def count_matches(s1, s2):
    ''' (str, str) -> int

    return the number of positions in s1 that contain the
    same character at the corresponding position of s2

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2

    '''

    num_matches = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches +1

    return num_matches

def sum_items(list1, list2):
    ''' (list of number, list of number) -> list of number

    return a new list in which each item is the sum of the items at the
    corresponding position of list1 and list2

    Precondition: len(list1) == len(list2)

    >>> sum_items([1, 2, 3], [2, 4, 2])
    [3, 6, 5]
    '''

    sum_list = []

    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list


def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list
    
    Return a new list in which each item is a 2-item list with the string from the
    corresponding position of list1 and the int from the corresponding position of list2.
    
    Precondition: len(list1) == len(list2)
    
    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''
    
    pairs = []
    for i in range(len(list1)):
       pairs.append([list1[i], list2[i]])
        
    return pairs
