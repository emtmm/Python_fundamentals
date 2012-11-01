'''A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
'''


def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'BOX')
    True
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'MATA')
    False
    '''
    for word_in_list in wordlist:
        if word_in_list == word:
            return True
        else:
            return False


def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    ''XSOB'
    '''
    word = ''
    for letter_list in board[row_index]:
        i = 0
        for letter in letter_list:
            word = word + letter[i]
            i = i + 1
 

    return word


def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2)
    'TO'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'AX'
    '''
    word = ''
    for letter_list in board:
        word = word + letter_list[column_index]
    return word
        


def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    '''

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    '''
    for letter_list in board:
        for column_index in range(len(letter_list)):
            if word in make_str_from_column(board, column_index):
                return True
                    
    return False


def board_contains_word(board, word):
    '''(list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'INK')
    False
    '''
    if board_contains_word_in_column(board, word):
        return True
    elif board_contains_word_in_row(board, word):
        return True
    else:
        return False


def word_score(word):
    '''(str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character in word
                 7-9: 2 points per character in word
                 10+: 3 points per character in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('METAMORPHIC')
    33
    '''
    points = 0
    if len(word) < 3:
        points = len(word) * 0
    elif len(word) >= 3 and len(word) <= 6:
        points = len(word) * 1
    elif len(word) >= 7 and len(word) <= 9:
        points = len(word) * 2
    elif len(word) >= 10:
        points = len(word) * 3

    return points


def update_score(player_info, word):
    '''([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    '''

    player_info[1] = player_info[1] + word_score(word)


def num_words_on_board(board, words):
    '''(list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'XSO', 'SOB', 'TO'])
    4
    '''
    counter = 0
    for words_board in words:
        if board_contains_word(board, words_board):
            counter = counter + 1

    return counter

def read_words(words_file):
    ''' (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    '''
    words_list = []
    for line in words_file:
        words_list.append(line.strip('\n'))
        
    return words_list
   


def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    '''

    board = []
    line = board_file.readline()
    while line != '':
        #print (line)
        letters_list = []
        for letters in line:
            #print (letters)
            if letters != '\n':
                letters_list.append(letters)            
            #print (letters_list)
        board.append(letters_list)
        line = board_file.readline()
    return board
    
    
