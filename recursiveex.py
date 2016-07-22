def print_num (c, n):
    if c <= n:
        print c
        print_num(c + 1, n)
print_num(1, 10)

def hello_name (n):
    names = ['Matthew', 'Toby', 'Kyle', 'Carolyn', 'Regan']
    if n <= len(names):
        print 'Hello %s' % names[n - 1]
        hello_name(n + 1)
hello_name(1)

class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

one = LLNode(1)
two = LLNode(2)
one.next = two
three = LLNode(3)
two.next = three
four = LLNode(4)
three.next = four

def ll_lookup(node, target):
    if node.data == target:
        print 'This is the right data: %s' %node.data
        return node.data
    elif node.next == None:
        return node.next
    else:
        print 'This is the wrong data: %s' % node.data
        ll_lookup(node.next, target)


ll_lookup(one, 4)
