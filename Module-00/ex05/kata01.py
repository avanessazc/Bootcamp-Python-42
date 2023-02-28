# The kata variable is always a dictionary and can only be filled with strings.
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if (type(kata) == dict):
    for k in kata:
        print(k + " was created by " + kata[k])

# src: https://www.askpython.com/python/string/python-format-function#:~:
# text=Python%20Dictionary%20can%20also%20be,a%20value%20to%20be%20formatted.
# &text=The%20key%20is%20passed%20to,key%20by%20it's%20value%2C%20respectively.
