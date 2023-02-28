import sys
import string

morse_code = {'A': '.-',      'a': '.-',
              'B': '-...',    'b': '-...',
              'C': '-.-.',    'c': '-.-.',
              'D': '-..',     'd': '-..',
              'E': '.',       'e': '.',
              'F': '..-.',    'f': '..-.',
              'G': '--.',     'g': '--.',
              'H': '....',    'h': '....',
              'I': '..',      'i': '..',
              'J': '.---',    'j': '.---',
              'K': '-.-',     'k': '-.-',
              'L': '.-..',    'l': '.-..',
              'M': '--',      'm': '--',
              'N': '-.',      'n': '-.',
              'O': '---',     'o': '---',
              'P': '.--.',    'p': '.--.',
              'Q': '--.-',    'q': '--.-',
              'R': '.-.',     'r': '.-.',
              'S': '...',     's': '...',
              'T': '-',       't': '-',
              'U': '..-',     'u': '..-',
              'V': '...-',    'v': '...-',
              'W': '.--',     'w': '.--',
              'X': '-..-',    'x': '-..-',
              'Y': '-.--',    'y': '-.--',
              'Z': '--..',    'z': '--..',
              '0': '-----',   '1': '.----',
              '2': '..---',   '3': '...--',
              '4': '....-',   '5': '.....',
              '6': '-....',   '7': '--...',
              '8': '---..',   '9': '----.'
              }


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        text = " ".join(sys.argv[1:])
        text_morse = []
        for c in text:
            if c == ' ':
                text_morse.append("/")
            elif c in string.punctuation:
                text_morse = "ERROR"
                break
            else:
                text_morse.append(morse_code[c])

        if text_morse != "ERROR":
            text_trans = " ".join(text_morse)
            print(text_trans)
        else:
            print("ERROR")
