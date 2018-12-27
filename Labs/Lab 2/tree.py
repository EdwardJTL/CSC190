from queue import queue


class tree:
    def __init__(self, x):
        self.store = [x, []]
        self.level = 0

    def AddSuccessor(self, x):
        if not isinstance(x, tree):
            return False
        else:
            self.store[1] = self.store[1] + [x]
        return True

    def level_check(self, n):
        self.level = n+1
        for i in self.store[1]:
            i.level_check(self.level)
        return True

    def Print_DepthFirst(self):
        self.level_check(-1)
        self.print_self()
        return True

    def print_self(self):
        blank = ""
        for i in range(0, self.level, 1):
            blank += "  "
        print '%s %s' % (blank, str(self.store[0]))
        for i in self.store[1]:
            i.print_self()
        return True

    def Get_LevelOrder(self):
        return_list = []
        process_queue = queue()
        process_queue.push(self)
        while not process_queue.is_empty():
            item = process_queue.pop()
            return_list = return_list + [item.store[0]]
            for i in item.store[1]:
                process_queue.push(i)
        return return_list

    def ConvertToBinaryTree(self):
        from binary_tree import binary_tree
        q = queue()
        root = binary_tree(self.store[0])
        for i in self.store[1]:
            node = i.ConvertToBinaryTree()
            q.push(node)
        while q.length() > 1:
            a = q.s_pop()
            b = q.s_pop()
            b.AddRight(a)
            q.push(b)
        child = q.pop()
        if isinstance(child,binary_tree):
            root.AddLeft(child)
        return root
