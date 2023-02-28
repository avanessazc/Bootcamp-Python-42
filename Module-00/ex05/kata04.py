# The kata variable is always a tuple that contains, in the following order:
# • 2 non-negative integer containing up to 2 digits
# • 1 decimal
# • 1 integer
# • 1 decimal
kata = (0, 4, 132.42222, 10000, 12345.67)


if (type(kata) != tuple):
    exit(print("Kata variable is not a Tuple, mais", type(kata)))

def count_digits(num: int):
    count = 0
    while (num != 0):
        num //= 10
        count += 1
    return count

size = len(kata)
if (size == 5):
    if (type(kata[0]) == int and kata[0] >= 0 and count_digits(kata[0]) <= 2 and
            type(kata[1]) == int and kata[1] >= 0 and count_digits(kata[1]) <= 2 and
            type(kata[2]) == float and
            type(kata[3]) == int and
            type(kata[2]) == float):
        print("module_{:0>2d}, ex_{:0>2d} : {:.2f}, {:.2e}, {:.2e}".format(
            kata[0], kata[1], kata[2], kata[3], kata[4]))
    else:
        print("Kata variable does not have the right format")

# print("module_%02d, ex_%02d : %.2f, %.2e, %.2e" %(kata[0], kata[1], kata[2], kata[3], kata[4]))
