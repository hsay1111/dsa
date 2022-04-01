class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def parse_tuple(data):
    #print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def tree_to_tuple(tree):
    #print(tree.left.key, tree.key, tree.right.key)    
    if isinstance(tree, TreeNode):
        if (tree.left != None or tree.right != None):
            tree = (tree_to_tuple(tree.left), tree.key, tree_to_tuple(tree.right))
        else:
            print('shit')
            tree = tree.key
    return tree


def display_keys(node, space='\t', level=0):
    #print(node.key if node else None, level)
    
    #if node is empty
    if node is None:
        print(space*level + 'o')
        return 
    
    #if the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    #if the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)
          
def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left) +
            [node.key] +
            traverse_in_order(node.right))

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) +tree_size(node.right)

def diameter(node):
    if node is None:
        return 0
    
    return max(tree_height(node.left) + tree_height(node.right),max(diameter(node.left), diameter(node.right)))


##node0 = TreeNode(3)
##node1 = TreeNode(4)
##node2 = TreeNode(5)
##node0.left = node1
##node0.right = node2
##tree = node0
##print(tree.key)
##print(tree.left.key)
##print(tree.right.key)

tree2 = parse_tuple(((1,3,None), 2, ((None,3,4), 5, (6,7,8))))
print(tree_to_tuple(tree2))
display_keys(tree2, '  ')
print(traverse_in_order(tree2))
#print(tree_height(tree2))
#print(tree_size(tree2))
print(diameter(tree2))
