import random

class BTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "BTreeNode(%r)" % self.data

def bst_insert(node, new_node):
    if node.data > new_node.data:
        if node.left is None:
            node.left = new_node
        else:
            bst_insert(node.left, new_node)
    else:
        if node.right is None:
            node.right = new_node
        else:
            bst_insert(node.right, new_node)

def bst_pre_order_traverse(node, fn, level=0):
    if node is None:
        return
    fn(node, level)
    bst_pre_order_traverse(node.left, fn, level + 1)
    bst_pre_order_traverse(node.right, fn, level + 1)

root_node = BTreeNode(59)
numbers = [57, 13, 65, 6, 44, 29, 21, 82, 96, 95, 71]
for i in numbers:
    bst_insert(root_node, BTreeNode(i))

def printit(node, level):
    print node.data

bst_pre_order_traverse(root_node, printit)


def bst_lookup(tree_node, target):
    if tree_node.data == target:
        print 'We found the data: %s' % tree_node.data
        return tree_node.data
    else:
        if tree_node.data > target:
            print 'Moving left'
            return bst_lookup(tree_node.left, target)
        elif tree_node.data < target:
            print 'Moving right'
            return bst_lookup(tree_node.right, target)
print bst_lookup(root_node, 29)

def bst_in_order_traversal(tree_node):
    if tree_node.left:
        bst_in_order_traversal(tree_node.left)
    print tree_node.data
    if tree_node.right:
        bst_in_order_traversal(tree_node.right)
bst_in_order_traversal(root_node)


def bst_min(tree_node):
    if tree_node.left:
        return bst_min(tree_node.left)
    else:
        print tree_node.data
        return tree_node.data
print bst_min(root_node)
