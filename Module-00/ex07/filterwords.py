import sys
import re

if __name__ == "__main__":
    words = []
    filterwords = []

    if (len(sys.argv) != 3 or sys.argv[1].isdigit() is True or
            sys.argv[2].isdigit() is False):
        print("ERROR")
    else:
        text_string = sys.argv[1]
        number = int(sys.argv[2])
        words = re.split(
            r'[!\"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~\s]\s*', text_string)
        filterwords = [ i for i in words  if len(i) > number ]
        print(filterwords)

# src: https://www.geeksforgeeks.org/string-punctuation-in-python/
