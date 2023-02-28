class TinyStatistician:

    @staticmethod
    def mean(x) -> float:
        length = len(x)
        if (length == 0):
            return None
        return (sum(x) / length)

    @staticmethod
    def median(x) -> float:
        length = len(x)
        if length == 0:
            return None
        x = sorted(x)
        if (length % 2 != 0):
            m = x[round(length / 2)]
            return float(m)
        else:
            m = x[round(length / 2) - 1] + x[round(length / 2)]
            m = m / 2
            return float(m)

    @staticmethod
    def quartiles(x) -> float:
        length = len(x)
        if length == 0:
            return None
        x = sorted(x)
        i = int((25 / 100) * length)
        q1 = x[i]
        i = int((75 / 100) * length)
        q3 = x[i]
        return ([float(q1), float(q3)])

    @staticmethod
    def var(x) -> float:
        length = len(x)
        if length == 0:
            return None
        tmp = 0
        x_mean = TinyStatistician.mean(x)
        for i in range(length):
            tmp += (x[i] - x_mean) ** 2
        return (tmp / length)

    @staticmethod
    def std(x) -> float:
        length = len(x)
        if length == 0:
            return None
        return (TinyStatistician.var(x) ** 0.5)


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.median(a))
    # Expected result: 42.0
    print(tstat.quartiles(a))
    # Expected result: [10.0, 59.0]
    print(tstat.var(a))
    # Expected result: 12279.439999999999
    print(tstat.std(a))
    # Expected result: 110.81263465868862
