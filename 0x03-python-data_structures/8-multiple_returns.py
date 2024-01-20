#!/usr/bin/python3

def multiple_returns(sentence):
    """ returns two things:
        length of a string and its first character

        Args:
            sentence: the sentence

        Returns:
            tuple with:
            1- the length of the sentence
            2- the first letter of the senetence
        """

    length_string = len(sentence)

    if length_string == 0:
        first_char = None
    else:
        first_char = sentence[0]

    tuple_sentence = (length_string, first_char)

    return (tuple_sentence)
