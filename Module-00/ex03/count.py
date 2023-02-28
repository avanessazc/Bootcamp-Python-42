import sys
import string


def text_analyzer(text_string=None):
    '''This function counts the number of upper characters, lower characters, \
punctuation and spaces in a given text.'''
    if (text_string is None):
        # text_string = input("What is the text to analyze?\n>> ")
        print("What is the text to analyse?")
        text_string = input(">> ")
    else:
        res = isinstance(text_string, str)
        # print(type(text_string))
        if (res is False):
            print("AssertionError: argument is not a string")
            return
    nbr_of_upper_case_chars = 0
    nbr_of_lower_case_chars = 0
    nbr_of_punctuation_chars = 0
    nbr_of_spaces_chars = 0
    for s in text_string:
        if (s.islower()):
            nbr_of_lower_case_chars = nbr_of_lower_case_chars + 1
        elif (s.isupper()):
            nbr_of_upper_case_chars = nbr_of_upper_case_chars + 1
        elif (s in string.punctuation):
            nbr_of_punctuation_chars = nbr_of_punctuation_chars + 1
        elif (s == " "):
            nbr_of_spaces_chars = nbr_of_spaces_chars + 1
    total = nbr_of_upper_case_chars \
        + nbr_of_lower_case_chars \
        + nbr_of_punctuation_chars \
        + nbr_of_spaces_chars
    print("The text contains", total, "character(s):")
    print("-", nbr_of_upper_case_chars, "upper letter(s)")
    print("-", nbr_of_lower_case_chars, "lower letter(s)")
    print("-", nbr_of_punctuation_chars, "punctuation mark(s)")
    print("-", nbr_of_spaces_chars, "space(s)")


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        # text_string = input("What is the text to analyze?\n>> ")
        print("What is the text to analyse?")
        text_string = input(">> ")
        text_analyzer(text_string)
    elif (len(sys.argv) > 2):
        print("AssertionError: more than one argument are provided")
    else:
        text_analyzer(sys.argv[1])

"""
text_analyzer("Python 2.0, released 2000, introduced \
features like List comprehensions and a garbage collection \
system capable of collecting reference cycles.")
"""

"""
text_analyzer("Python is an interpreted, high-level, \
general-purpose programming language. Created by Guido van \
Rossum and first released in 1991, Python's design philosophy \
emphasizes code readability with its notable use of significant \
whitespace.")
"""
