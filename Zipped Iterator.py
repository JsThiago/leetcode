class ZippedIterator:
    a = []
    b = []
    lastUsed = "b"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def next(self):
        if(self.lastUsed == "b" and len(self.a)>0):
            self.lastUsed = "a"
            return self.a.pop(0)
        elif(len(self.b)>0):
            self.lastUsed = "b"
            return self.b.pop(0)
        elif(len(self.a)>0):
            return self.a.pop(0)

    def hasnext(self):
        return len(self.b) > 0 or len(self.a) > 0
        