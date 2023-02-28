import random

if __name__ == "__main__":
    try:
        n = random.randint(1, 99)
        print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to \
find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")
        print("What's your guess between 1 and 99?")
        s = input()
        i = 1
        while s != "exit":
            if (s.isdigit() is True and int(s) > 0 and int(s) < 100):
                if int(s) > n:
                    print("Too high!")
                elif int(s) < n:
                    print("Too low!")
                else:
                    if n == 42:
                        print("The answer to the ultimate question of life, \
        the universe and everything is 42.")
                    if i == 1:
                        print("Congratulations! You got it on your first try!")
                    else:
                        print("Congratulations, you've got it!")
                        print("You won in %d attempts!" % i)
                    break
            elif (s.isdigit() is True and (int(s) <= 0 or int(s) >= 100)):
                print("That's not a valid number.")
            else:
                print("That's not a number.")
            print("What's your guess between 1 and 99?")
            s = input()
            i += 1
        if s == "exit":
            print("Goodbye!")
    except Exception:
        print('')
