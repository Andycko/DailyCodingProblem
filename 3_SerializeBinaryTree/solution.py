class Node:
    """
    Given class from challange
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):        
    global res
    res += node.val + " "
    if node.left:                 
        serialize(node.left)
    else:
        res += str(node.left) + " "
    if node.right:
        serialize(node.right)
    else:
        res += str(node.right) + " "

    return res

def deserialize(pickle):
    def helper(arr):
        global t
        if arr[t] == 'None':
            t += 1
            return None

        node = Node(arr[t])
        t += 1
        node.left = helper(arr)
        node.right = helper(arr)
        return node    

    return helper(pickle.split())

t = 0
res = ""
root = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left'), Node('right.right')))
# root = Node('root', Node('left'), Node('right'))
serialized = serialize(root)
print(deserialize(serialized).right.val)
