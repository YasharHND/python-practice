class NaturalEvenNumbers:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.current = 2
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        out = self.current
        self.current += 2
        return out


for i in NaturalEvenNumbers(10):
    print(i)
