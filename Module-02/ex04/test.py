from my_minipack import logger
from my_minipack import loading
import time

if __name__ == "__main__":
    print("----------my_minipack.logger----------")
    machine = logger.CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
        machine.make_coffee()
        machine.add_water(70)
    print("----------my_minipack.loading----------")
    listy = range(100, 200)
    ret = 0
    for elem in loading.ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
