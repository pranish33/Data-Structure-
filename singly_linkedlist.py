class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


a = Node(1)
b = Node(2)
c = Node(3)


# implementing singly linklist

a.nextNode = b
b.nextNode = c
