class stack:
    def __init__(self):
        self.store = []

    def push(self, value):
        self.store = self.store + [value]
        return True

    def pop(self):
        if len(self.store) == 0:
            return -1
        value = self.store[-1]
        self.store = self.store[0:-1]
        return value
