

def convert_word_to_int(word):
    """

    Parameters
    ----------
    word (str) : word to be replaced, key of the dictionary

    Returns
    -------

    """
    word_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'zero': 0, 0: 0}
    return word_dict[word]