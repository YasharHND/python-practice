import os


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


# Sample using iterator
# Listing directories and files under the current working directory
path = os.getcwd()
_, dir_names, file_names = next(iter(os.walk(path)))

print("directories:", dir_names)
print("files:", file_names)
