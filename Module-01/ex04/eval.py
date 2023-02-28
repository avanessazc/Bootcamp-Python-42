def check_arguments(coefs, words) -> bool:
    if (not all([isinstance(obj, list) for obj in [coefs, words]])):
        return False
    if (len(coefs) != len(words)):
        return False
    if (not all([isinstance(obj, str) for obj in words])):
        return False
    if (not all([isinstance(obj, (int, float)) for obj in coefs])):
        return False
    return True


class Evaluator():
    def __int__(self):
        pass

    @staticmethod
    def zip_evaluate(coefs, words):
        if (not check_arguments(coefs, words)):
            return (-1)
        res = 0
        for w, c in zip(words, coefs):
            res += len(w) * c
        return (res)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if (not check_arguments(coefs, words)):
            return (-1)
        res = 0
        for i, word in enumerate(words):
            res += len(word) * coefs[i]
        return (res)


# if __name__ == "__main__":
#     words = ["Le", "Lorem", "Ipsum", "est", "simple"]
#     coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
#     print(Evaluator.zip_evaluate(coefs, words))
#     print("-----------------------------------------------------")
#     words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
#     coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
#     print(Evaluator.enumerate_evaluate(coefs, words))
