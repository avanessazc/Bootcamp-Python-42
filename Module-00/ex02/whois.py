import sys

if __name__ == "__main__":
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument are provided")
    elif (len(sys.argv) == 2):
        # if (sys.argv[1].isdigit() is False):
        #     print("AssertionError: argument is not an integer")
        try:
            num = int(sys.argv[1])
            if (num == 0):
                print("I'm Zero.")
            elif (num % 2):
                print("I'm Odd.")
            else:
                print("I'm Even.")
        except ValueError:
            print("AssertionError: argument is not an integer")
