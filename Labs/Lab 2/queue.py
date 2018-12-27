class queue:
    def __init__(self):
        self.storage = []

    def push(self, a):
        self.storage += [a]
        return True

    def pop(self):
        if len(self.storage) == 0:
            return False
        else:
            a = self.storage[0]
            if len(self.storage) > 1:
                self.storage = self.storage[1:]
            else:
                self.storage = []
            return a

    def s_pop(self):
        if len(self.storage) == 0:
            return False
        value = self.storage[-1]
        self.storage = self.storage[0:-1]
        return value

    def is_empty(self):
        if self.storage.__len__() == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.storage)