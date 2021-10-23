# This would be a working solution, however the the dereferencing from id to object returns a segmentation fault...

import ctypes

class Node():
    def __init__(self, val):
        self.val = val
        self.npx = 0

class XORLinkedList():
    def __init__(self, node):
        self.head = node
        self.tail = node
        # self.__nodes = [node]

    def get(self, index):
        prev_id = 0
        node = self.head

        for i in range(index):
            next_id = prev_id ^ node.npx

            if next_id:
                prev_id = id(node)
                print(next_id)
                node = ctypes.cast(next_id, ctypes.py_object).value
            else:
                return False
        
        return node.val


    def add(self, element):
        self.tail.npx = id(element) ^ self.tail.npx
        element.npx = id(self.tail)
        self.tail = element

        # self.__nodes.append(element)

        

if __name__ == "__main__":
    x = XORLinkedList(Node("1"))
    x.add(Node("2"))
    x.add(Node("3"))
    print("Head: " + x.head.val)
    print(x.get(1))
    print("Tail: " + x.tail.val)
