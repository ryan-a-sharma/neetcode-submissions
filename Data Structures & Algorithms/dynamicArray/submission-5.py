class DynamicArray:

    def __init__(self, capacity: int):
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()

        self.array[self.getSize()] = n

    def popback(self) -> int:
        x = self.array[self.getSize() - 1]
        self.array[self.getSize() - 1] = None
        return x

    def resize(self) -> None:
        self.array += [None] * len(self.array)

    def getSize(self) -> int:
        for i in range(len(self.array)):
            if self.array[i] is None:
                return i

        return len(self.array)

    def getCapacity(self) -> int:
        return len(self.array)