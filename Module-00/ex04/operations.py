import sys
import decimal

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("AssertionError: too many arguments")
    elif len(sys.argv) < 3:
        print("Usage: python operations.py <number1> <number2>\n\
    Example:\n\
        python operations.py 10 3")
    # elif sys.argv[1].isdigit() is False or sys.argv[2].isdigit() is False:
    #     print("AssertionError: only integers")
    else:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])

            print("Sum:       " + str(a + b))
            print("Differ:    " + str(a - b))
            print("Product:   " + str(a * b))
            if b == 0:
                print("Quotient:  ERROR (division by zero)")
                print("Remainder: ERROR (modulo by zero)")
            else:
                print("Quotient:  " + str(
                    decimal.Decimal(a) / decimal.Decimal(b)))
                print("Remainder: " + str(a % b))
        except ValueError:
            print("AssertionError: only integers")
