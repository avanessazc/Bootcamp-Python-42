# The kata variable is always a string whose length is not higher than 42.
kata = "The right format"

if (type(kata) != str):
    exit(print("Kata variable is not a String, mais", type(kata)))
if (len(kata) > 42):
    exit(print("Kata variable length is not higher than 42."))
print(kata.rjust(41, '-'), end="")

# print(kata.ljust(41, '-'))
