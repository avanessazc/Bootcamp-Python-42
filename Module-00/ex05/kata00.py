# The kata variable is always a tuple and can only be filled with integer
kata = (19, 42, 21) 

if (type(kata) != tuple):
    exit(print("Kata variable is not a Tuple, mais", type(kata)))

size = len(kata)
if (size == 0):
    exit(print("Empty variable"))

print(f"The {size} numbers are:", ", ".join(map(str, kata)))

# map():
# https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function
