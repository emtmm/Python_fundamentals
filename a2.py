import math
def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''

    return dna.__len__()

def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    if dna1.__len__() > dna2.__len__():
        return True
    else:
        return False
    


def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''

    if dna1.find(dna2) != -1:
        return True
    else:
        return False


def is_valid_sequence(sequence):
    '''(str) -> bool

    Return True if and only if the DNA sequence is valid. Lowercase
    characters are not valid

    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('atcg')
    False
    >>> is_valid_sequence('BDCG')
    False
    '''
    not_nucleotides = 0
    for char in sequence:
        if not char in 'ATCG':
            not_nucleotides = not_nucleotides + 1
    if not_nucleotides > 0:
        return False
    else:
        return True

def insert_sequence(dna1, dna2, where):
    '''(str, str, int) -> str

    Return DNA sequence obtained by inserting the second sequence into the first

    >>> insert_sequence('CCGG', 'AT', '2')
    'CCATGG
    '''

    return dna1[:where] + dna2 + dna1[where:]


def get_complement(nucleotide):
    '''(str) -> str

    Return the complement of the given nucleotide
    
    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    '''

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    else:
        return 'C'
    

def get_complementary_sequence(DNA):
    '''(str) -> str

    Return the complementary sequence.

    >>> get_complementary_sequence('TA')
    'AT'
    >>> get_complementary_sequence('ACGTACG')
    TGCATGC
    '''

    complementary_sequence = ''
    for nucleotide in DNA:
        complementary_sequence = complementary_sequence + get_complement(nucleotide)

    return complementary_sequence

