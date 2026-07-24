class LinkedList:
    
    def __init__(self):
        self.ll = []
    
    def get(self, index: int) -> int:
        if index >= len(self.ll):
            return -1
        return self.ll[index]

    def insertHead(self, val: int) -> None:
        self.ll = [val] + self.ll

    def insertTail(self, val: int) -> None:
        self.ll += [val]

    def remove(self, index: int) -> bool:
        if index >= len(self.ll):
            print(index, len(self.ll))
            return False
        head = self.ll[:index]
        if len(self.ll[index:]) > 1:
            self.ll = self.ll[index+1:]
            self.ll = head + self.ll
        else:
            self.ll = head

        return True

    def getValues(self) -> List[int]:
        return self.ll
        
