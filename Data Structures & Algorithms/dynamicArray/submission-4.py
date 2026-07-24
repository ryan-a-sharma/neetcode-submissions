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

        for i in range(len(self.array)):
            if self.array[i] is None:
                self.array[i] = n
                return

    def popback(self) -> int:
        for i in range(len(self.array) - 1, -1, -1):
            if self.array[i] is not None:
                value = self.array[i]
                self.array[i] = None
                return value

    def resize(self) -> None:
        self.array += [None] * len(self.array)

    def getSize(self) -> int:
        for i in range(len(self.array)):
            if self.array[i] is None:
                return i

        return len(self.array)

    def getCapacity(self) -> int:
        return len(self.array)