class GotCharacter:
    """Class GotCharacter
    Args:
        first_name: string = None
        is_alive: bool = True
    """
    def __init__(self, first_name: str = None, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """Class Stark

    Args:
        first_name: string = None
        is_alive: bool = True
    Attributes:
        family_name: string = "Stark"
        house_words: string = "Winter is Coming"
    """
    def __init__(self, first_name: str = None, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        '''prints the House words'''
        print(self.house_words)

    def die(self):
        '''changes the value of is_alive to False'''
        self.is_alive = False

    def __str__(self):
        txt = "I'm {} ".format(self.first_name) \
            + "from {} house\n".format(self.family_name) \
            + "House words: {}\n".format(self.house_words)
        if (self.is_alive is True):
            txt = txt + "I'm alive"
        else:
            txt = txt + "I'm dead"
        return txt


if __name__ == "__main__":
    arya = Stark("Arya")
    print(arya.__dict__)
    print("\n")
    arya.print_house_words()
    print("\n")
    print(arya)
    print("\n")
    arya.die()
    print(arya)
    print("\n")
    print(arya.__doc__)
    print("\n")
    print(GotCharacter.__doc__)
