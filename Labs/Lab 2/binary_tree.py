from queue import queue

class binary_tree:
    def __init__(self, x):
        self.store = [x, 0, 0]

    def AddLeft(self, x):
        if not isinstance(x, binary_tree):
            return False
        else:
            if self.store[1] != 0:
                if isinstance(self.store[1],binary_tree):
                    r = self.store[1].AddLeft(x)
                    return r
                else:
                    return False
            else:
                self.store[1] = x
                return True

    def AddRight(self, x):
        if not isinstance(x, binary_tree):
            return False
        else:
            if self.store[2] != 0:
                if isinstance(self.store[2],binary_tree):
                    r = self.store[2].AddRight(x)
                    return r
                else:
                    return False
            else:
                self.store[2] = x
                return True

    def print_tree(self, x):
        blank = ""
        for i in range(0, x, 1):
            blank += "   "
        print blank + str(self.store[0])
        for i in [1, 2]:
            if isinstance(self.store[i], binary_tree):
                self.store[i].print_tree(x + 1)
        return True

    def Get_LevelOrder(self):
        r_list = []
        process_queue = queue()
        process_queue.push(self)
        while not process_queue.is_empty():
            item = process_queue.pop()
            r_list = r_list + [item.store[0]]
            for i in item.store[1:]:
                if isinstance(i,binary_tree):
                    process_queue.push(i)
        return r_list



    def ConvertToTree(self):
        if isinstance(self.store[2],binary_tree):
            return [False,0]
        new = self.double_gen_tree()
        tree = new[0]
        return [True, tree]


    def double_gen_tree(self):
        from tree import tree
        q = queue()
        root = tree(self.store[0])
        if isinstance(self.store[2], binary_tree):
            node = self.store[2].double_gen_tree()
            q.push(node[0])
            while not node[1].is_empty():
                sib = node[1].pop()
                q.push(sib)
        if isinstance(self.store[1], binary_tree):
            node = self.store[1].double_gen_tree()
            root.AddSuccessor(node[0])
            while not node[1].is_empty():
                sib = node[1].pop()
                root.AddSuccessor(sib)
        return [root, q]
