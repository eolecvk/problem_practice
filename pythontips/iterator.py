
class PowTwo:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):

        if self.n <= self.max:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration


class InfIter:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


if __name__ == "__main__":

    oddgen = InfIter()
    print(next(oddgen))
    print(next(oddgen))
    print(next(oddgen))