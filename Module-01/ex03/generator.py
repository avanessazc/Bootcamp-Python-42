from random import random


def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.\
option precise if a action is performed to the substrings before it is yielded.
    shuffle: shuffles the list of words
    unique: returns a list where each word appears only once
    ordered: alphabetically sorts the words.
    """
    if (not isinstance(text, str) or
       (option is not None and
            option not in ['shuffle', 'unique', 'ordered'])):
        # raise ValueError("ERROR")
        yield 'ERROR'
        return

    words = text.split(sep)
    if (option is not None and option == 'shuffle'):
        # https://www.programiz.com/python-programming/methods/list/sort
        words.sort(key=lambda x: random())
    elif (option is not None and option == 'unique'):
        lst = []
        for i, word in enumerate(words):
            if (words[:i].count(word) == 0):
                lst.append(word)
        words = lst
    elif (option is not None and option == 'ordered'):
        words.sort()

    for word in words:
        yield word


if __name__ == "__main__":

    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)
    print('\n')

    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print('\n')

    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print('\n')

    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    print('\n')

    text = 1.0
    for word in generator(text, sep="."):
        print(word)
    print('\n')
