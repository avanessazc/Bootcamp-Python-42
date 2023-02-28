# The kata variable is always a tuple that contains 5 non-negative integers. The first
# integer contains up to 4 digits, the rest up to 2 digits.
kata = (2019, 9, 25, 3, 30)

def count_digits(num: int):
    count = 0
    while (num != 0):
        num //= 10
        count += 1
    return count

if (type(kata) != tuple):
    exit(print("Kata variable is not a Tuple, mais", type(kata)))

size = len(kata)
if (size == 5):
    if (count_digits(kata[0]) <= 4 and
            count_digits(kata[1]) <= 2 and
            count_digits(kata[2]) <= 2 and
            count_digits(kata[3]) <= 2 and
            count_digits(kata[4]) <= 2):
        print("%02d/%02d/%04d %02d:%02d" %( kata[1], kata[2], kata[0], kata[3], kata[4]))
        # print("{:0>2d}/{:0>2d}/{:0>4d} {:0>2d}:{:0>2d}".format(
        #     kata[1], kata[2], kata[0], kata[3], kata[4]))
    else:
        print("Kata variable does not have the right format")
