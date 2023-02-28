import time
from random import randint
import os


def log(funct):
    USERNAME = os.getenv("USER") or os.getenv("USERNAME") or "user"
    DESCRIPTION = funct.__name__.replace('_', ' ').title()

    def inner_function(*args, **kwargs):
        # https://www.programiz.com/python-programming/methods/built-in/open
        with open("machine.log", 'a') as logs_file:
            logs_file.write("(%s)Running: %-19s" %(USERNAME, DESCRIPTION))
            start_time = time.time()
            return_value = funct(*args, **kwargs)
            exec_time = time.time() - start_time
            unit = "s"
            if (exec_time < 0.5):
                unit = "ms"
                exec_time *= 1000
            logs_file.write("[ exec-time = %.3f %s ]\n" %(exec_time, unit))
        return (return_value)
    return (inner_function)


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
        machine.make_coffee()
        machine.add_water(70)
