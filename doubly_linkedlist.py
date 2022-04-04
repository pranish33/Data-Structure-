""" Imlementation of doubly linkedlist using python"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.prevNode = a
b.nextNode = c
c.prevNode = b
