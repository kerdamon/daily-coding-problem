'''
Took me: 38 min
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    '''
    n is number of elements in the tree
    Time complexity: O(n)
    Space complexity: O(1)
    '''

    if node is None:
        return ''

    serialized_left = ''
    serialized_string = ''
    serialized_right = ''

    serialized_string = node.val

    if node.left is not None:
        serialized_left = serialize(node.left)
    else:
        serialized_left = 'None'

    if node.right is not None:
        serialized_right = serialize(node.right)
    else:
        serialized_right = 'None'

    return serialized_string + ' ' + serialized_left  + ' ' + serialized_right

def deserialize(string):
    '''
    n is number of elements in the tree
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    
    deserialize.nodes = string.strip().split(' ')

    if len(deserialize.nodes) == 0:
        return None

    val = deserialize.nodes[0]
    deserialize.nodes = deserialize.nodes[1:]

    if val == 'None':
        return None

    return Node(val, deserialize(' '.join(deserialize.nodes)), deserialize(' '.join(deserialize.nodes)))
    
deserialize.nodes = []

def test():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

if __name__=='__main__':
    test()
