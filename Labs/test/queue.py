class queue:
    def __init__(self):
        self.store = []

    def store(self,n):
        self.store += [n]
        return True

    def retrieve(self):
        if len(self.store) != 0:
            x = self.store[0]
            self.store = self.store[1:]
            return x
        else:
            return False