import time
from datetime import datetime


def ft_progress(lst):
    start_time = time.time()
    bar_length = 20
    eta = 0
    delta = None
    refresh_rate = len(lst) / 20
    for i in range(len(lst)):
        ratio = float(i + 1) / len(lst)
        bar = ("=" * int(ratio * (bar_length - 1))) + ">"
        percent = int(round(ratio * 100))
        now = time.time()
        elapsed = round(now - start_time, 2)
        if delta is not None:
            eta = delta * (len(lst) - i - 1)
        print("ETA: {:.2f}s [ {}%] [{}".format(
            eta, str(percent), bar + '] ' +
            str(i + 1) + '/' + str(len(lst)) +
            '| elapsed time ' + str(elapsed) + 's' + '\033[1A\r'))
        yield i
        if delta is None or (i % refresh_rate) == 0:
            delta = time.time() - now


# if __name__ == "__main__":
#     listy = range(100, 200)
#     ret = 0
#     for elem in ft_progress(listy):
#         ret += (elem + 3) % 5
#         time.sleep(0.01)
#     print()
#     print(ret)
#     listy = range(3333)
#     ret = 0
#     for elem in ft_progress(listy):
#         ret += elem
#         time.sleep(0.005)
#     print()
#     print(ret)


# src: https://
# stackoverflow.com/questions/7342529/how-do-you-write-over-an-echoed-line
# https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
