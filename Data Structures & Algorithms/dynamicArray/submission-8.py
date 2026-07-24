class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == len(self.arr):
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        x = self.arr[self.size]
        self.arr[self.size] = None
        return x

    def resize(self) -> None:
        self.arr += [None] * len(self.arr)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.arr)